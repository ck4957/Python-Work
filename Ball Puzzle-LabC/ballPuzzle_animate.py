"""
This program animates the colored ball juggling puzzle.
It has an animate_init() function to create the initial
setup with all balls in the first (red) can.
Then it has an animate_move() function, which takes the list of
stacks as well as integers indicating the from and to stacks,
and moves the top ball appropriately.

NOTE:  students need to follow the interface for these functions,
that is provide the expected inputs to the functions, 
but do not need to change anything in the functions.  

Author:  Aaron Deever

file:  ballPuzzle_animate.py
"""

from turtle import *
from myStack import *
        
def animate_init(ballColors):
    """
    This function initializes the canvas for the ball puzzle animation.
    input: ballColors :  string indicating ball colors. It is assumed
    the string contains only the values R,G,B, otherwise an error is raised.

    The ballColors string must be no more than length 50 and must be nonempty.

    output: the initial drawing has all balls in the first can
    """
    
    setup(620,620)  # bdy of 10 pixels on each edge of 600x600 main area
    setworldcoordinates(-10,-10,610,610)
    speed(0)
    hideturtle()
    ps = 2
    pensize(ps)

    # determine the allowable radius of each ball
    num = len(ballColors)

    if num > 50:
        bye()
        raise ValueError("Puzzle graphics only handle up to 50 balls.")
    elif num == 0:
        bye()
        raise ValueError("Must have at least one ball.")
    
    diameter = 550 / num
    if(diameter > 150):
        diameter = 150   # maximum we allow
    rad = diameter / 2
    
    # draw the cans
    up()
    fd(100-rad-ps)
    lt(90)
    fd(20)

    # first can
    down()
    fd(550)
    bk(550)
    rt(90)
    fd(diameter + 2*ps)
    lt(90)
    fd(550)

    # cans two and three
    for i in range(2):
        up()
        rt(90)
        fd(200-diameter-2*ps)
        rt(90)
        down()
        fd(550)
        lt(90)
        fd(diameter+2*ps)
        lt(90)
        fd(550)

    up()
    bk(550)
    rt(90)
    bk(400 + rad + ps)
    pensize(1)

    # leaves us in the middle of the base of the first can,
    # facing east, pen up

    # now populate the first can
    down()
    for i in range(len(ballColors)):
        if((ballColors[i] == 'R')):
            fillcolor('red')
        elif((ballColors[i] == 'G')):
            fillcolor('green')
        elif((ballColors[i] == 'B')):
            fillcolor('blue')
        else:
            raise ValueError("Input string must contain only R,G,B.")

        begin_fill()
        circle(rad)
        end_fill()

        up()
        lt(90)
        fd(diameter)
        rt(90)
        down()

    # now jump below the cans for labels
    up()
    home()
    fd(80)
    write('RED',font=('Arial', 16, 'normal'))
    fd(190)
    write('GREEN', font=('Arial', 16, 'normal'))
    fd(205)
    write('BLUE', font=('Arial', 16, 'normal'))
    
    
    # now get back to the middle base of first can
    up()
    home()
    fd(100)
    lt(90)
    fd(20)
    rt(90)
           

def animate_move(stackList, fromCan, toCan):
    """
    Precondition - move is legal.
    Precondition:  THIS FUNCTION ASSUMES THAT THE STACKS HAVE ALREADY
    BEEN ADJUSTED ACCORDING TO THE MOVE THAT
    IT IS ABOUT TO ANIMATE.  IT DOES NOT ADJUST THE STACKS!!!
    THIS FUNCTION SHOULD BE CALLED
    IMMEDIATELY AFTER THE MOVE IS PERFORMED. 

    Precondition - the turtle is facing east in the middle of the
    base of the first can.

    Postcondition = turtle is placed back where it started.

    Note:  need to recompute the sizes used during initialization
    """

    # deduce ball size based on total number of balls
    canSize = [size(stackList[0]), size(stackList[1]), size(stackList[2])]

    num = sum(canSize)

    diameter = 550 / num
    if(diameter > 150):
        diameter = 150   # maximum we allow
    rad = diameter / 2

    # erase from fromCan
    fd(200*fromCan)
    lt(90)
    fd(diameter * canSize[fromCan])
    rt(90)
    down()
    pensize(3)
    fillcolor('white')
    pencolor('white')
    begin_fill()
    circle(rad)
    end_fill()
    pensize(1)

    # move to first can
    up()
    lt(90)
    back(diameter * canSize[fromCan])
    rt(90)
    bk(200*fromCan)

    # move to toCan
    fd(200*toCan)
    lt(90)
    fd(diameter * (canSize[toCan]-1))
    rt(90)
    down()
    pencolor('black')
    val = top(stackList[toCan])
    if(val == 'R'):
        fillcolor('red')
    elif(val == 'G'):
        fillcolor('green')
    else:
        fillcolor('blue')
    begin_fill()
    circle(rad)
    end_fill()

    # move to first can
    up()
    lt(90)
    back(diameter * (canSize[toCan]-1))
    rt(90)
    bk(200*toCan)

def animate_finish():
    bye()
    
    
