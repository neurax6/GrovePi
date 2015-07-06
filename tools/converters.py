__author__ = 'neuraxis'

from ctypes import *

def hextofloat(s):
    i = int(s, 16)  # Hex to int
    cp = pointer(c_int(i))  # Int to C int
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value  # dereference the pointer, get the float
