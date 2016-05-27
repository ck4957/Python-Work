"""
description: An implementation of a Symbol Class for Variable Length Coding
file: symbol.py
language: python3
Author: Chirag Kular
"""


class Symbol:

    __slots__ = 'name', 'frequency', 'codeword'

    def __init__(self, name, frequency, codeword=''):
        self.name = name
        self.frequency = frequency
        self.codeword = codeword
