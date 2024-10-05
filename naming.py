'''
naming.py
Created: Thursday, 3rd October 2024 10:31:40 am
Matthew Riche
Last Modified: Thursday, 3rd October 2024 10:32:04 am
Modified By: Matthew Riche
'''

import maya.cmds as cmds
from typing import List
import re

def add_prefix(target_node: str, prefix: str) -> str:
    """Adds a prefix to a node's name.

    Args:
        target_node (str): Node to rename.
        prefix (str): string prefix to add.

    Returns:
        str: The new name (As well as renaming 'in-place')
    """    
    # This effectively undoes things like "long name" if provided.
    current_name = cmds.ls(target_node)[0]
    new_name = prefix + current_name
    cmds.rename(target_node, new_name, ignoreShape=0)
    return new_name


def add_suffix(target_node: str, suffix: str) -> str:
    """Adds a suffix to a node's name.

    Args:
        target_node (str): Node to rename.
        suffix (str): string suffix to add.

    Returns:
        str: The new name (As well as renaming 'in-place')
    """    
    # This effectively undoes things like "long name" if provided.
    current_name = cmds.ls(target_node)[0]
    new_name = current_name + suffix
    cmds.rename(target_node, new_name, ignoreShape=0)
    return new_name


def batch_rename(target_node_list: list[str], char_seq: str):
    """Renames all the items in the given list to what is defined by the character sequence.
    The "#" appearing in the character sequence will then be turned into enumeration with
    appropriate padding.

    Args:
        target_node_list (list[str]): _description_
        char_seq (str): _description_

    Raises:
        ValueError: If the character sequence doesn't have exactly one cluster of '#'.
        NameError: If the character sequence begins with '#'-- illegal in Maya.
    """    

    count = 0
    # Use the number of # to determine how much zero padding is required.
    hashgroups = re.findall(r'#+', char_seq)
    if(len(hashgroups) != 1):
        raise ValueError (f"The sequence \"{char_seq}\" does not have (at most) one group of '#'.")
    padding = len(hashgroups[0])

    if(char_seq[0] == '#'):
        raise NameError (f"Character sequence can't start with a number in Maya.")

    pre_token = char_seq.split(hashgroups[0])[0]
    post_token = char_seq.split(hashgroups[0])[-1]

    for node in target_node_list:
        count += 1
        cmds.rename(node, pre_token + str(count).zfill(padding) + post_token)



        