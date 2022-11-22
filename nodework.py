'''
nodework.py
Created: Tuesday, 22nd November 2022 10:19:08 am
Matthew Riche
Last Modified: Tuesday, 22nd November 2022 10:19:12 am
Modified By: Matthew Riche
'''
# Common operations for manipulating and comprehending nodes in maya.  Main stuff I miss my PyMel.


import maya.cmds as cmds

def get_shape(node):
    """Grab the shape node of a transform or similar.

    Args:
        node (str): String name of a node in-scene.

    Raises:
        ValueError: If the node doesn't exist.
        TypeError: If the node doesn't have a shape (or is a shape.)

    Returns:
        str: string name of the shape node.
    """    

    # Verify this node exists in the scene:
    if(cmds.ls(node) == []):
        raise ValueError ("No node called {} exists in the scene.".format(node))

    shape = cmds.listRelatives(node, shapes=True)
    if shape:
        return shape
    else:
        raise TypeError ("This node doesn't have it's own shape.")