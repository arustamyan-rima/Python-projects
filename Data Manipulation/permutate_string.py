
"""
Write a function permutate_string(), which returns a
random permutation of a name.
Use the shuffle method of the random module.

Parameters: name
Return value: string
stefan = fetsan

"""
import random

def permutate_string(string):
    l = [c for c in string]
    random.shuffle(l)
    return "".join(l)


print(permutate_string('hallo'))