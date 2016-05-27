"""
description:Ball puzzle where each can contains color balls of their respective cans.
[i.e. Red can will contain red ball after the puzzle is solved]
file: ballPuzzle.py
language: python3
author: Chirag Kular
"""
from ballPuzzle_animate import *
from myStack import *


def moveBall(from_can, to_can):
    """
    This function is used to move the ball from the 'fromCan' to 'toCan'
    :param fromCan: the can from which the ball is popped
    :param toCan: the can in which the ball is pushed
    :return: Modified stack objects of fromCan and toCan
    """
    temp = top(from_can)
    from_can = pop(from_can)
    to_can = push(to_can, temp)
    return from_can, to_can

0
def puzzle_Solver(colorBalls):
    """
    This function is used to move different color balls in their respective color cans
    :param colorBalls: Different color balls
    :return: Total Moves required to solve the puzzle
    """
    countMoves = 0
    # Counts the total moves to solve the puzzle
    red_can = EmptyNode()
    # Red Can will contains red balls after the puzzle is solved.
    blue_can = EmptyNode()
    # Blue Can will contains blue balls after the puzzle is solved.
    green_can = EmptyNode()
    # Green Can will contains green balls after the puzzle is solved.
    for x in colorBalls:
        # Initially all the balls are stored in the Red Cans
        red_can = push(red_can, x)
        
    while not emptyStack(red_can):
        # Pop the ball untill the red can becomes empty
        current_ball = top(red_can)
        if current_ball == 'G':
            # If current ball is Green, push it in green can if stack is empty
            if emptyStack(green_can):
                red_can, green_can = moveBall(red_can, green_can)
                stackList = [red_can, green_can, blue_can]
                animate_move(stackList, 0, 1)
                countMoves += 1
            else:
                # Else if top of green can is different color pop untill its not green
                # and then push the current ball in the green can
                while not emptyStack(green_can) and top(green_can) != 'G':
                    green_can, blue_can = moveBall(green_can, blue_can)
                    stackList = [red_can, green_can, blue_can]
                    animate_move(stackList, 1, 2)
                    countMoves += 1
                red_can, green_can = moveBall(red_can, green_can)
                stackList = [red_can, green_can, blue_can]
                animate_move(stackList, 0, 1)
                countMoves += 1
        elif current_ball == 'B':
            # If current ball is Blue, push it in blue can if stack is empty
            if emptyStack(blue_can):
                red_can, blue_can = moveBall(red_can, blue_can)
                stackList = [red_can, green_can, blue_can]
                animate_move(stackList, 0, 2)
                countMoves += 1
            else:
                # Else if top of blue can is different color pop untill its not blue
                # and then push the current ball in the blue can
                while not emptyStack(blue_can) and top(blue_can) != 'B':
                    blue_can, green_can = moveBall(blue_can, green_can)
                    stackList = [red_can, green_can, blue_can]
                    animate_move(stackList, 2, 1)
                    countMoves += 1
                red_can, blue_can = moveBall(red_can, blue_can)
                stackList = [red_can, green_can, blue_can]
                animate_move(stackList, 0, 2)
                countMoves += 1
        else:
            # Else if current ball is red, then push it in the green can
            red_can, green_can = moveBall(red_can, green_can)
            stackList = [red_can, green_can, blue_can]
            animate_move(stackList, 0, 1)
            countMoves += 1

    while not emptyStack(green_can) and top(green_can) == 'R':
        # While top of green can is red, pop it and push it in the red can
        # and increment count_moves
        green_can, red_can = moveBall(green_can, red_can)
        stackList = [red_can, green_can, blue_can]
        animate_move(stackList, 1, 0)
        countMoves += 1
    while not emptyStack(blue_can) and top(blue_can) == 'R':
        # While top of blue can is red, pop it and push it in the red can
        # and increment count_moves
        blue_can, red_can = moveBall(blue_can, red_can)
        stackList = [red_can, green_can, blue_can]
        animate_move(stackList, 2, 0)
        countMoves += 1
    return countMoves


def main():
    """
    Main function prompts the user for the color balls and the 
    puzzle_solver function is called which returns the total moves and prints it
    :return:
    """
    balls = input("Enter the initial balls for the RedCan : ")
    print(balls)
    animate_init(balls)
    total_moves = puzzle_Solver(balls)
    print("Total number of moves required to solve the puzzle:", total_moves)
    input("Press Enter to Quit")
    animate_finish()
    #GBRBGGBR

if __name__ == '__main__':
    main()