'''
controls.py
Created: Saturday, 17th September 2022 11:20:53 am
Matthew Riche
Last Modified: Saturday, 17th September 2022 11:20:57 am
Modified By: Matthew Riche
'''

import maya.cmds as cmds

class CurveData:
    def __init__(self):
        """Data that represents the shape of a nurbsCurve, and methods to capture and rebuild it 
        where needed.
        """        

        self.pos_vectors
        self.degree
        self.knots
        self.form

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
                    raise Exception ("Shape node called {} is not of type nurbsCurve".format(shape))
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
            raise Exception ("Type in scene of {} is not 'nurbsCurve'.".format(curve_shape_node))

        # Read and store the point data from a curve:
        cv_indices = cmds.getAttr(curve_shape_node + '.controlPoints', mi=True)
        pos_vectors = []
        for i in cv_indices:
            next_vec = cmds.getAttr(curve_shape_node + '.cv[' + str(i) + ']')[0]
            pos_vectors.append(next_vec)

        # Create the curve info node and connect it to the shape to read data.
        curve_info_node = cmds.createNode('curveInfo', n='RIGID_TEMP_curveInfo')
        cmds.connectAttr(curve_shape_node + '.worldSpace', curve_info_node + '.inputCurve')

        # Store other necessary attribute data.
        knots = cmds.getAttr(curve_info_node + '.knots')
        degree = cmds.getAttr(curve_shape_node + '.degree')
        form = cmds.getAttr(curve_shape_node + '.form')

        # Prep dict to return:
        self.pos_vectors = pos_vectors
        self.knots = knots
        self.degree = degree
        self.form = form

        # Scene cleanup of temporary utility nodes.
        cmds.delete(curve_info_node)

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
        self.curve_node = cmds.curve(
            per = self.form,
            p = self.pos_vectors,
            k = self.knots,
            d = self.degree
        )

# TODO build a function to install a new curve's shape beneath given transform.

# TODO build a function to mirror the components of a curve shape node.

# TODO change override colour of shape node, based on side token prefix.

# TODO safely change scale of components.
