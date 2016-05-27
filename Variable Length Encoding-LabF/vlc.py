"""
description: An implementation of a Variable Length Coding
file: vlc.py
language: python3
Author: Chirag Kular
"""

import math
from symbol import Symbol
from node import Node
from heap import Heap


def freqcmp(n1, n2):
    '''
    Simple comparison function for frequencies of symbols
    :param n1: Instance of Node 1
    :param n2: Instance of Node 2
    :return: True if n1 is less than n2
    '''
    return n1.total_freq < n2.total_freq

def readData(file):
    """
    Reads the data from the file instance and store in the dictionary
    :param file: Instance of input file
    :return:dictionary name
    """
    # Dictionary to store unique character(key) & their frequency(Value)
    char_freq = dict()
    for line in file:
        line = line.strip()
        # Read each character of the line
        for character in line:
            if character not in char_freq:
                char_freq[character] = 1
            else:
                char_freq[character] += 1
    return char_freq

def createHeap(char_freq_dict):
    """
    Creating the heap object and storing the values in heap
    by reading data from dictionary

    :param char_freq_dict: Dictionary with all the unique characters & its frequencies
    :return: List of all the symbol objects
    """

    # Creating Object of Heap Class
    minh = Heap(freqcmp)
    all_symbol_Obj = []
    for key in char_freq_dict:
        # Creating symbol object for every character
        new_symbol = Symbol(key, char_freq_dict[key])
        all_symbol_Obj.append(new_symbol)

        # Creating node object for every character
        new_node = Node([new_symbol], char_freq_dict[key])
        minh.insert(new_node)

    while len(minh) > 1:
        n1 = minh.pop()
        n2 = minh.pop()

        # Taking code from node1 symbol list and prepending '0' to the codeword
        for i in n1.symbol_list:
            i.codeword = '0' + i.codeword
        # Taking code from node2 symbol list and prepending '1' to the codeword
        for i in n2.symbol_list:
            i.codeword = '1' + i.codeword
        # Combing symbol list and adding their frequency and creating a new node
        new_node = Node(n1.symbol_list + n2.symbol_list, n1.total_freq + n2.total_freq)
        minh.insert(new_node)
    return all_symbol_Obj


def printOutput(all_symbol_obj):
    """
    Prints the output in specific format.
    Also calculates & prints Average VLC code word length and
    fixed code word length required for the given input file
    :param all_symbol_obj:  List of all symbol objects
    :return:
    """
    num = 0
    den = 0

    # If symbol list is empty, then no output
    if not all_symbol_obj:
        print("No Output")
    else:
        print("Variable Length Code Output")
        print("------------------------------------------------")
        for x in all_symbol_obj:
            print('Symbol : %2s  ' % x.name, end='')
            print("CodeWord : %8s  " %x.codeword,end='')
            print("Freqency : %5d" %x.frequency)
            num += len(x.codeword)*x.frequency
            den += x.frequency
        try:
            avg_vlc_code_length = num/den
            print("\nAverage VLC codeword length : ", avg_vlc_code_length, " bits per symbol")
            fixed_code_length = math.ceil(math.log(len(all_symbol_obj)))
            print("Average Fixed length codeword length :", fixed_code_length, " bits per symbol")
        except ZeroDivisionError:
            print("Attempt to Divide by Zero")


def main():
    """
    Prompts the user for the input file and then series of functions are invoked
     to read data, then creating heap, then printing output
    :return:
    """

    try:
        file_name = input("Enter the File name :")
        file = open(file_name)
        char_freq_dict = readData(file)
        all_symbol_obj = createHeap(char_freq_dict)
        printOutput(all_symbol_obj)
    except FileNotFoundError:
        print("File not Found")


if __name__ == '__main__':
    main()