"""
Stack interface.
file: myStack.py
author: Sean Strout
"""

from myNode import *
    
def emptyStack(node):
    """Is the stack empty?"""
    return node == EMPTY_NODE             

def push(node, element):
    """Add an element to the top of the stack"""
    return Node(element, node)
    
def top(node):
    """Return top element on stack.  Does not change stack"""
    if emptyStack(node):
        raise IndexError("top of empty stack") 
    return node.data

def pop(node):
    """Remove the top element in the stack.  Returns new top"""
    if emptyStack(node):
        raise IndexError("pop on empty stack") 
    return node.next
        
def size(node):                                         
    """Return the # of elements including this node"""  
    if emptyStack(node):                                
        return 0                                        
    else:                                               
        return 1 + size(pop(node))                      

######
def test():

    print("An empty stack")
    s = EmptyNode() # From myNode.py
    print(s)
    print()

    print("Add a few elements, any type supported")
    s = push( s, True )
    s = push( s, int(2) )
    s = push( s, "Three" )
    s = push( s, 4.0 )
    print("  ",s)
    print()

    print("Pop one")
    s = pop( s )
    print("  ",s)
    print()

    print("Add one more")
    s = push( s, '5' )
    print("  ",s)
    print()

    print("Final Stack")
    print("  Top:",top(s))
    print("  Size:",size(s))
    print("  ",s)

if __name__ == "__main__":
    test()
