'''
skin.py
Created: Friday, 11th October 2024 10:47:32 am
Matthew Riche
Last Modified: Friday, 11th October 2024 10:47:35 am
Modified By: Matthew Riche
'''

import maya.cmds as cmds
from . import nodework as nw

class SkinClusterNotFoundError(Exception):
    """Raised when a skin cluster is not found on the source geometry."""
    pass


def find_skin_cluster(node: str) -> str:
    """Returns the attached skinCluster of a given node.

    Args:
        node (str): In scene node name.

    Returns:
        str: Skin Cluster node name.  Returns None if no cluster is found.
    """    

    print(f"Checking connections of {node} for skinClusters...")
    skin_cluster = None
    for history_node in cmds.listHistory(node):
        if(cmds.nodeType(history_node) == 'skinCluster'):
            skin_cluster = history_node
            break
    if(skin_cluster is None):
        return None
    else:
        return skin_cluster
    

def find_influences(skin_cluster: str) -> list:
    """Creates a list of all influences of provided skinCluster.

    Args:
        skin_cluster (str): A skinCluster to check.

    Raises:
        TypeError: If the provided string doesn't reference a skinCluster.
        ValueError: If the skinCluster has no existing influences.

    Returns:
        list: All influences associated with given skinCluster.
    """    

    if(cmds.nodeType(skin_cluster) != 'skinCluster'):
        raise TypeError(f"{skin_cluster} is not a skinCluster.")
    
    infs = cmds.skinCluster(skin_cluster, q=True, inf=True)
    if(infs == []):
        raise ValueError(f"{skin_cluster} has in influences somehow.")
    else:
        return infs


def copy_skinweights(source_geo: str, target_geos: list):
    """Copies any found skinCluster from the source geo to everything in the target list.

    Args:
        source_geo (str): Node name of source geo.
        target_geos (list): Node names of target geos.

    Raises:
        ValueError: Geo from source or target isn't in the scene.
        TypeError: Provided node name isn't a mesh.
        SkinClusterNotFoundError: If there's no skinCluster found on the source.
    """    

    # Sanitize input-- does it exist, right type, has skincluster.
    all_geos = target_geos + [source_geo]
    for geo in all_geos:
        print(f"Working {geo}")
        if(cmds.objExists(geo) == False):
            raise ValueError (f"{geo} isn't found in the scene or is not unique.")
        if(cmds.nodeType(nw.get_shape(geo)) != 'mesh'):
            raise TypeError (f"{geo} isn't a mesh.")
    source_cluster = find_skin_cluster(source_geo)
    if(source_cluster is None):
        raise SkinClusterNotFoundError(f"No skinCluster found on {source_geo}")
    joint_infs = find_influences(source_cluster)
    
    # Begin the copy from sock to targets:
    print(f"Copying weights from {geo} to unskinned meshes...")
    count = 0
    for geo in target_geos:
        if(find_skin_cluster(geo) is None):
            destination_skin = cmds.skinCluster(geo, joint_infs, omi=False, tsb=False)[0]
        else:
            print(f"{geo} already has a skin cluster, skipping this geo.")
            continue

        print(f"Copying {source_cluster} to {destination_skin}")
        cmds.copySkinWeights(ss=source_cluster, ds=destination_skin, noMirror=True, sm=True)
        count += 1

    print(f"Done copying {source_cluster} from {source_geo} to {count} meshes.")



