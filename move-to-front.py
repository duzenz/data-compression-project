from __future__ import print_function
from string import ascii_lowercase
 
SYMBOLTABLE = list(ascii_lowercase)

def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence
 
def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)
 
 
encode = move2front_encode('aaafhhimst', SYMBOLTABLE)

print(encode)

decode = move2front_decode(encode, SYMBOLTABLE)

print(decode)
