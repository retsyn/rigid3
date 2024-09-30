'''
testing.py
Created: Tuesday, 30th July 2024 9:37:29 am
Matthew Riche
Last Modified: Tuesday, 30th July 2024 9:38:32 am
Modified By: Matthew Riche
'''

import unittest
import maya.cmds as cmds

# Make sure munit test is around somewhere.
try:
    import munittest as muni
except ImportError:
    raise ImportError(f"MUnitTest is not pathed.  Can't run these tests.")

print(f"MUnitTest was found at {muni.__file__}")

