'''
controls.py
Created: Saturday, 17th September 2022 11:20:53 am
Matthew Riche
Last Modified: Sunday, 18th September 2022 2:55:30 pm
Modified By: Matthew Riche
'''

import maya.cmds as cmds
import os


class CurveData:
    def __init__(self, node=None, sel=False):
        """Data that represents the shape of a nurbsCurve, and methods to capture and rebuild it 
        where needed.
        """        

        self.pos_vectors = []
        self.degree = None
        self.knots = None
        self.form = None
        self.curve_node = None
        self.curve_shape = None
        # Formerly, we'd capture curves during init automatically.  Now it must be flagged, so the 
        # UI can own a curve instance and reset it at will.
        if((node is not None) or (sel == True)):
            self.capture_curve(node=node, sel=sel)


    def capture_curve(self, node=None, sel=False):
        """Captures and reads the data of a curve.

        Args:
            node (str, optional): The in-scene name of a nurbsCurve. Defaults to None.
            sel (bool, optional): Whether or not to use selection. Defaults to False.

        Raises:
            Exception: _description_
        """        
        if(node is not None):
            if(cmds.objectType(node) == 'nurbsCurve'):
                self.curve_shape = self.get_curve_shape(node)[0]
                self.learn_curve(self.curve_shape)
            else:
                raise TypeError ("String {} isn't a nurbsCurve.")
        elif(sel):
            print("Learning curve from selection...")
            node = self.get_curve_shape()[0]
            if(cmds.objectType(node) != 'nurbsCurve'):
                raise TypeError ("{} is not a nurbsCurve.".format(node))
            self.curve_shape = node
            self.learn_curve(self.curve_shape)
        else:
            raise Exception ("Requires either node string or selection to be true.")


    @staticmethod
    def get_curve_shape(nodename=None):
        """Given the name of a transform node, return the names of the shape nodes.

        Args:
            nodename (str, optional): Specific node name in scene of transform.  Using default will test
                selection in scene instead. Defaults to None.

        Raises:
            Exception: If specified or selected node is not of type transform.
            Exception: If the shape node found is not of type nurbsCurve.
            Exception: If the given transform node had no children at all.

        Returns:
            list: All shape nodes found beneath the given transform.
        """    
        
        # Fall back on selection if default args are provided.
        if(nodename == None):
            try:
                nodename = cmds.ls(sl=True)[0]
            except IndexError:
                raise Exception ("No objects in selection.")
        # Sanitize this data-- we want the selection to be a transform, and the shape to be a nurbscurve
        if(cmds.objectType(nodename) != 'transform'):
            raise Exception ("nodename doesn't point to a transform node.")
        shapenodes = cmds.listRelatives(nodename, shapes=True)
        if(shapenodes):
            for shape in shapenodes:
                if(cmds.objectType(shape) != 'nurbsCurve'):
                    raise TypeError ("Shape node called {} is not of type nurbsCurve".format(shape))
            return shapenodes
        else:
            raise Exception ("Given transform didn't have a shape child.")

    def learn_curve(self, curve_shape_node):
        """Captures of relevant data needed to recreate this curve shape later.  Stores attribute data
        in a dictionary, for remaking in-situ or saving as a json file.

        Args:
            curve_shape_node (str): In-scene string name of a nurbsCurve shape node.

        Raises:
            Exception: If a list or any non-str type is passed.
            Exception: If the shape node passed is not a nurbsCurve type.

        Returns:
            dict: dictionary of all the required attributes.
        """    

        if(type(curve_shape_node) is not str):
            raise Exception ("Must be single string representing shape node.")
        elif(cmds.objectType(curve_shape_node) != 'nurbsCurve'):
            raise TypeError ("Type in scene of {} is not 'nurbsCurve'.".format(curve_shape_node))
        # Read and store the point data from a curve:
        cv_indices = cmds.getAttr(curve_shape_node + '.controlPoints', mi=True)
        print(curve_shape_node)
        pos_vectors = []
        for i in cv_indices:
            # By casting this to a list, we give ourselves the ability to assign items later, which
            # helps with our mirroring.
            next_vec = list(cmds.getAttr(curve_shape_node + '.cv[' + str(i) + ']')[0])
            pos_vectors.append(next_vec)
        # Create the curve info node and connect it to the shape to read data.
        curve_info_node = cmds.createNode('curveInfo', n='RIGID_TEMP_curveInfo')
        cmds.connectAttr(curve_shape_node + '.worldSpace', curve_info_node + '.inputCurve')
        # Store other necessary attribute data.
        knots = cmds.getAttr(curve_info_node + '.knots')[0]
        degree = cmds.getAttr(curve_shape_node + '.degree')
        form = cmds.getAttr(curve_shape_node + '.form')
        # Prep dict to return:
        self.pos_vectors = pos_vectors
        self.knots = knots
        self.degree = degree
        self.form = form
        # Scene cleanup of temporary utility nodes.
        cmds.delete(curve_info_node)
        print("Read nurbsCurve attributes for {}".format(curve_shape_node))

    def build(self):
        """Build the curve in the scene based on the captured data.

        Raises:
            Exception: If any piece of data is missing, it'll crash.
        """        

        # Make sure we have content to build:
        for data in [self.form, self.pos_vectors, self.knots, self.degree]:
            if(data is None):
                raise Exception ("Cannot build curve with lacking curve data")
        # Create the curve node based on it.
        print(self)
        self.curve_node = cmds.curve(
            per = False,
            p = self.pos_vectors,
            k = self.knots,
            d = self.degree
        )
        self.curve_shape = self.get_curve_shape(self.curve_node)
        if(self.form > 0):
            cmds.closeCurve(self.curve_shape, ch=False, rpo=True)

    def mirror(self, axis='x'):
        """Mirror the control vertices' position along a given axis.

        Args:
            axis (str, optional): Value characters are 'x', 'y', 'z' depend on the axis to reverse.
                Defaults to 'x'.

        Raises:
            Exception: If a bad char is supplied to axis.
        """        
        print("AXIS IS {}".format(axis))
        axis_names = ('x', 'y', 'z')
        if(axis not in axis_names):
            raise Exception ("Axis must be 'x', 'y', or 'z'.")
        # Turn the given axis from 'x','y','z' to [0, 1, 2] for use in the next part.
        ind = axis_names.index(axis)
        print("INDEX IS {}".format(ind))
        # Negate the value of the position vector (based on axis)
        for i in range(len(self.pos_vectors)):
            self.pos_vectors[i][ind] = (-self.pos_vectors[i][ind])

    def replace(self, node=None):
        """Builds this curve and makes it the child selected or specified controller.  Deletes the 
        former shape node.

        Args:
            node (str, optional): The string name of the transform node to target.  If none, will 
                read the scene selection. Defaults to None.

        Raises:
            Exception: If the targeted node (by arg or by selection) is not a transform.
        """        

        if(node is None):
            node = cmds.ls(sl=True)[0]
            if(cmds.objectType(node) != 'transform'):
                raise Exception ("Targeted node must be a transform.")

        old_shape = self.get_curve_shape(node)
        self.build()
        cmds.parent(self.curve_shape, node, s=True, r=True)
        cmds.delete(self.curve_node)
        cmds.delete(old_shape)

    @staticmethod
    def copy(mirror=False):
        """Copies from first selection to second selection and installs the curves beneath.

        Args:
            mirror (bool, optional): optionally mirrors x if true.. Defaults to False.

        Raises:
            Exception: If two valid targets aren't selected.
        """        

        selections = cmds.ls(sl=True)
        if(len(selections) != 2):
            raise Exception ("Must select two transforms with nurbCurve shapes beneath.")
        data = CurveData()
        shape_to_copy = data.get_curve_shape(selections[0])[0]
        data.learn_curve(shape_to_copy)
        print(data)
        if(mirror):
            data.mirror()
        data.replace(node=selections[1])

    def as_dict(self):

        for data_point in [self.degree, self.knots, self.form]:
            if(data_point is None):
                raise TypeError ("CurveData contained NoneType data.")

        if(self.pos_vectors == []):
            raise ValueError ("No point data in CurveData.")
        
        return ({
                'pos_vectors':self.pos_vectors, 
                'degree':self.degree, 
                'knots':self.knots, 
                'form':self.form
                })

    def from_dict(self, dict):
        """Given a dictionary, populate the data.

        Args:
            dict (dict): Dictionary that must contain pos_vectors, degre, knots, and form.

        Raises:
            Exception: If the provided dict doesn't contain all of the necessary entries.
        """        

        # Fix data from the legacy file-type:
        if('points' in dict):
            print("Legacy dat 'points' found.")
            dict['pos_vectors'] = dict['points']
        if('per' in dict):
            print("legacy data 'per' found.")
            if(dict['per'] == False or dict['per'] == 'false'):
                dict['form'] = 0
            elif(dict['per'] == True or dict['per'] == 'true'):
                dict['form'] = 2

        # Check that data isn't empty
        for data_key in ['degree', 'knots', 'form']:
            if(dict[data_key] is None):
                raise TypeError ("Dictionary contained NoneType data.")
        if(dict['pos_vectors'] == []):
            raise ValueError ("'pos_vectors' was an empty list.")

        for attr_name in ['pos_vectors', 'degree', 'knots', 'form']:
            if(attr_name not in dict):
                raise Exception ("Provided dictionary doesn't have the right contents.")
        
        self.pos_vectors = dict['pos_vectors']
        self.degree = dict['degree']
        self.knots = dict['knots']
        self.form = dict['form']


    def __str__(self):
        return ("Cvs: {}\nDegree: {}\nKnots: {}\nPeriodic: {}".format(
            self.pos_vectors, self.degree, self.knots, self.form))

    def __len__(self):
        return len(self.pos_vectors)
    

def colour_shapenode(rgb: tuple, target: str):
    # verify the rgb value is sane:
    if(len(rgb) != 3):
        raise IndexError("rgb was provided wrong number of values.")
    for vector in rgb:
        if(type(vector) not in ['float', 'int', 'double']):
            raise ValueError("Value given in rgb \"{vector}\" is not a number.")

    # Todo: add rgb    
    
        
    

# TODO change override colour of shape node, based on side token prefix.

# TODO safely change scale of components.
