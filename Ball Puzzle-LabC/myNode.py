"""
Nodes
file: myNode.py
author: Sean Strout
author: Arthur Nunes-Harwitt
"""

from rit_lib import *

# Create a new class to represent an empty node
class EmptyNode(struct): 	                
    _slots = ()                      

# Create an object that represents an empty node
EMPTY_NODE = EmptyNode()

class Node(struct):
    _slots = ((object, 'data'), ((EmptyNode, 'Node'), 'next') )
    
