"""
description: An implementation of a Node class for Variable Length Coding
file: node.py
language: python3
Author: Chirag Kular
"""


class Node:
    __slots__ = 'symbol_list','total_freq'

    def __init__(self, symbol_obj, total_freq):

        self.symbol_list = symbol_obj
        self.total_freq = total_freq
