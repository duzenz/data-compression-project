from __future__ import print_function
from string import ascii_lowercase

SYMBOL_TABLE = list(ascii_lowercase)


class MoveToFront:

    def move_to_front_code(self, text):
        sequence, pad = [], SYMBOL_TABLE[::]
        for char in text:
            index = pad.index(char)
            sequence.append(index)
            pad = [pad.pop(index)] + pad
        return sequence

    def move_to_front_decode(self, sequence):
        chars, pad = [], SYMBOL_TABLE[::]
        for index in sequence:
            char = pad[index]
            chars.append(char)
            pad = [pad.pop(index)] + pad
        return ''.join(chars)
