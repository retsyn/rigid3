'''
file_ops.py
Created: Sunday, 18th September 2022 8:39:37 pm
Matthew Riche
Last Modified: Sunday, 18th September 2022 8:40:11 pm
Modified By: Matthew Riche
'''

import json
import os
import maya.cmds as cmds


def get_path():
    """Get the parent path of the installation dir.

    Returns:
        str: parent path folder.
    """    
    mod_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(mod_path)

    return parent_path


def dump_to_file(dict, path):
    """Given a single dict, dump to a .json file at the given path.

    Args:
        dict (dict): Any dict data.
        path (str): The path to write the .json.

    Returns:
        bool: Returns whether or not the write was a success.
    """    

    try:
        with open(path, 'w') as json_file:
            json.dump(dict, json_file)
        return True

    except FileExistsError:
        print("FAILED TO WRITE {}".format(path))
        return False


def read_from_file(path):
    """Given a path, read the data found within if it's .json.

    Args:
        path (str): Full path to file.

    Returns:
        dict: Data read from .json.
    """    
    try:
        file = open(path)
        data = json.load(file)

        file.close()

        return data
    except FileNotFoundError:
        print("FAILED TO READ {}".format(path))
        return None