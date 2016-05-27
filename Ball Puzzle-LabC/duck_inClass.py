"""
duck.py
author: Erika Mesh
description: A linkable node class representing a duck that can change 
                into a goose (based on James Heliotis' LinkedNode)
"""
import random

class LinkedDuck:

    __slots__ = "name", "isGoose", "prevDuck", "nextDuck"

    def __init__( self, name, prevDuck = None, nextDuck = None ):
        """ Create a new duck and optionally link it to existing ones.
            param name: the name of this duck (string)
            param prevDuck: the duck linked before this one
            param nextDuck: the duck linked after this one
        """
        self.prevDuck = prevDuck
        self.nextDuck = nextDuck
        self.name = name

        # All Ducks start, by default, as Ducks.
        self.isGoose = False

    def __str__( self ):
        """ Return a string representation of the contents of
            this duck: it's name and a "*" if it is currently
            acting like a goose
        """
        result = self.name
        if self.isGoose:
            result += "*"
        return result

    def __repr__( self ):
        """ Return a string that, if evaluated, would recreate
            this duck and the duck to which it is linked.
        """
        next = "None"
        if self.nextDuck != None:
            next = self.nextDuck.name

        prev = "None"
        if self.prevDuck != None:
            prev = self.prevDuck.name

        return "LinkedDuck(" + repr( self.name ) + "," + \
            repr( self.isGoose ) + "," + repr( prev ) + "," \
            + repr( next ) + ")\n"

    def addDuck( self, newDuck ):
        """Add the new duck after me (pushing out the one
            currently after me if needed
        """
        ###########################
        ### IMPLEMENT ME
        ###########################

        if self is None:
            self = newDuck
        else:
            self.nextDuck = newDuck
            newDuck.prevDuck = self

    def moveBefore( self, newNext ):
        """Remove self from current position in the linked
            list and add after the given duck
        """
        ###########################
        ### IMPLEMENT ME
        ###########################
        # Removing self from its current position
        self.prevDuck.nextDuck = self.nextDuck
        self.nextDuck.prevDuck = self.prevDuck

        # Adding the self after newNext
        self.prevDuck = newNext
        self.nextDuck = newNext.nextDuck
        self.nextDuck.prevDuck = self
        newNext.nextDuck = self




    def makeAngry( self ):
        """ Make this duck so angry it turns into a goose and
            honks at it's friends for a while before getting
            back in line as an angry goose. The last duck 
            honked at will be angry at getting displaced 
            and the process continues until there are no ducks
            left to honk at - only angry geese.
        """
        if self.isGoose:
            print("How did this happen? I'm already a goose?!")
        else:
            print()
            self.isGoose = True
            ducksLeft = self.ducks_to_end()
            if ducksLeft > 0:
                honksLeft = random.randint(1,ducksLeft)
                nextTarget = self
                print(self.name,"is angry enough to honk at", \
                    honksLeft,"ducks!")
    
                # Run around the circle until I'm done honking at the ducks
                while honksLeft > 0:
                    # Move to the next target
                    nextTarget = nextTarget.nextDuck

                    # If this is a duck, the honk "counts"
                    if not nextTarget.isGoose:
                        honksLeft -= 1

                    # Honk at everyone though
                    print("   ",self.name+": HONK!",nextTarget)
    
                # I'm tired, but more honking needs to happen, make someone
                # else angry
                if honksLeft == 0:
                    # To make the next duck angry, I'm going to sit in 
                    # front of him!
                    self.moveBefore(nextTarget)
                    print("  New pecking order:")
                    self.print_to_end()

                    # Make the next duck angry!
                    nextTarget.makeAngry()
            else:
                print(self.name,"is angry but there are no more "+\
                    "ducks to honk at!")
                print()

    def print_to_end( self, start = None ):
        """ Print out each duck/goose from me to the end (or back to myself)
        """

        if self is start:
            pass
        else:
            print("   -",self)
            if start == None:
                start = self
            self.nextDuck.print_to_end(start)

    def ducks_to_end( self, start = None ):
        """ Count how many ducks from this one to a duck whose link is None
                (or until getting back to myself)
            return: the length of the list (counting only ducks) 
                starting at this duck
        """
        ###########################
        ### IMPLEMENT ME
        ###########################

        if self is start:
            #print("in if self, start",self, start)
            return 0
        else:
            if start == None:
                start = self
            if self.isGoose:
                return self.nextDuck.ducks_to_end(start)
            else:
                return 1 + self.nextDuck.ducks_to_end(start)

def test():
    # How many ducks should we test with?
    D = int(input("Enter the number of ducks [2,12]:"))

    # Make a list of connected ducks
    names = ["Albert","Barry","Clyde","Dewey","Eli","Frank", \
        "Gus","Huey","Igor","Jerry","Kyle","Louie"]
    ducks = []
    ducks.append(LinkedDuck(names[0]))
    for n in range(1,D):
        ducks.append(LinkedDuck(names[n]))

    # Connect the ducks together
    for n in range(1,len(ducks)):
        ducks[n-1].addDuck(ducks[n])

    # Connect the ends to form a circle
    ducks[len(ducks)-1].addDuck(ducks[0])

    # Print them all
    print("-- All Ducks --")
    ducks[0].print_to_end()
    print()

    # Make the middle duck angry!
    print("-- Make Middle Duck Angry --")
    ducks[len(ducks)//2].makeAngry()
    print()

if __name__ == "__main__":
    test()

