'''
build.py
Created: Thursday, 22nd September 2022 9:37:53 am
Matthew Riche
Last Modified: Tuesday, 22nd November 2022 2:35:07 pm
Modified By: Matthew Riche
'''


import maya.cmds as cmds
from . import nodework as nw

class BuildIdiom:
    def __init__(self):
        """Build idiom where we store node data about what we are altering, so we can undo, or 
        document the process cleanly.
        """        
        self.selected_nodes = None
        self.placers = None
        self.created_nodes = None
        self.affected_nodes = None

    def unbuild(self):
        """Uses affected nodes and created nodes lists to undo the construction of the idiom.

        Raises:
            ValueError: If no nodes were stored in created nodes.
        """        

        if(self.created_nodes):
            for node in self.created_nodes:
                cmds.delete(node)
        else:
            raise ValueError ("No created nodes are stored in this idiom.")

    def select_affected(self):
        """Select nodes in the 'affected_nodes' list in scene.

        Raises:
            ValueError: If no altered nodes are stored.
        """        
        
        if(self.affected_nodes):
            # TODO might be nice to iterate through the list 1x1 to individually call out missing.
            cmds.select(self.affected_nodes, r=True)
        else:
            raise ValueError ("No altered nodes are stored in this idiom.")

    def build(self):
        """Where the build happens.  It's generally super'd by specific build modules.
        """        
        if(len(cmds.ls(sl=True)) > 0):
            self.selected_nodes = cmds.ls(sl=True)
            print("Stored selected nodes:\n{}".format(self.selected_nodes))

    def post_build(self, created=None, affected=None):
        """Runs after builds have taken place, storing things in the scene that were affected.

        Args:
            created (list, optional): List of str names of created nodes. Defaults to None.
            affected (list, optional): List of str names of affected nodes. Defaults to None.
        """        
        if(affected):
            self.affected_nodes = affected
            print("Stored affected nodes:\n{}".format(self.affected_nodes))

        if(created):
            self.created_nodes = created
            print("Storing created nodes:\n{}".format(self.created_nodes))


class RibbonJoints(BuildIdiom):
    def __init__(self):
        """Creates joints beneath long lists of transforms like follicles, to assist in building 
        ribbons.

        Raises:
            ValueError: If the selection has varied types of node, indicating likely a mistake.
        """        
        super().__init__()
        
        self.selected_nodes = cmds.ls(sl=True)
        # Get the type of the first node:
        match_type = cmds.objectType(self.selected_nodes[0])
        # Sanitize selection:
        for node in self.selected_nodes:
            if(cmds.objectType(node) != match_type):
                raise ValueError ("Selection has varied types of node.")

        self.build()

    def build(self):
        super().build()

        # These are the nodes I will permit building beneath:
        accepted_nodes = ['follicle', 'locator', 'transform']

        created_joints = []
        affected_nodes = []
        for follicle_node in self.selected_nodes:            
            # Double check that the selected node is something legitimate:
            if(cmds.objectType(nw.get_shape(follicle_node)) in accepted_nodes):
                # Selection must be cleared in order to not confuse joint creation.
                cmds.select(cl=True)
                # Create a new joint at origin:
                new_joint = cmds.joint(p=(0,0,0))
                created_joints.append(new_joint)
                # Move the joint to the exact transformation as the follicle_node and parent it.
                cmds.matchTransform(new_joint, follicle_node)
                cmds.parent(new_joint, follicle_node)
                affected_nodes.append(follicle_node)
            else:
                continue
        
        # New joints are added to created list, and anything that has a new child is affected.
        self.post_build(created=created_joints, affected=affected_nodes)

class SimpleFK(BuildIdiom):
    def __init__(self, trans=False):
        """Build a simple FK, rotation only unless otherwise specified, using a null trans and 
        Direct connection to FK.

        Args:
            trans (bool, optional): Whether or not to hook up the transform. Defaults to False.
        """        
        super().__init__()
        self.build(trans)

    def build(self, cons_trans):
        """Runs the build of the simple FK
        """        
        super().build()

        selected_joint = cmds.ls(sl=True)[0]
        rot_order = cmds.getAttr(selected_joint + '.rotateOrder')
        ctrl_name = selected_joint.rpartition('_')[0]
        nurbs_name = cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n=ctrl_name + '_ctrl' )[0]
        cmds.delete(nurbs_name, ch=True)
        cmds.setAttr(nurbs_name + '.rotateOrder', rot_order)
        new_group = cmds.group(nurbs_name, n=ctrl_name + '_null')
        cmds.setAttr(new_group + '.rotateOrder', rot_order)
        cmds.matchTransform(new_group, selected_joint, piv=True, pos=True, rot=True)
        cmds.connectAttr(nurbs_name + '.r', selected_joint + '.r')
        print("Connected {} rotate to {} rotate.".format(nurbs_name, selected_joint))
        if(cons_trans):
            cmds.connectAttr(nurbs_name + '.t', selected_joint + '.t')
            print("Connected {} translate to {} translate.".format(nurbs_name, selected_joint))

        self.post_build(created = [nurbs_name, new_group], affected=selected_joint)


class SimpleIK(BuildIdiom):
    def __init__(self, joints=[]):
        super().__init__()

        self.selected_nodes = [jnt for jnt in cmds.ls(sl=True) if cmds.nodeType(jnt) == 'joint']
        jnt_count = len(self.selected_nodes)

        # Would kill for 3.10's match case.
        if(jnt_count == 3):
            self.build(self.selected_nodes, 3)
        elif(jnt_count == 2):
            self.build(self.selected_nodes, 2)
        else:
            raise ValueError("Select either 2 or 3 joints.")

    def build(self, joints, type):
        super().build()
        
        if(type == 3):
            self.build_ik_leg(joints)
        elif(type == 2):
            self.build_ik_lever(joints)
        else:
            raise ValueError("Unhandled IK build type.")

        