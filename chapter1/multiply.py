# -*- coding: utf-8 -*-
from __future__ import print_function
import random
from timeit import default_timer as timer

"""
python multiply.py
multiply function time:  0.000167479386347
simple multiplication time:  5.16825462454e-06

thus main library python function is faster
"""


def multiply(y, z):
    """
    return the product yz.
    """
    c = 3
    if z == 0:
        return 0
    else:
        # return(multiply(cy, floor(z/c)) + y · (z mod c))
        return(multiply(c*y, z//c) + y * (z % c))
    
if __name__ == "__main__":
    y = random.getrandbits(128)
    z = random.getrandbits(128)
    
    start = timer()
    a = multiply(y,z)
    end = timer()
    print("multiply function time: ", end - start)
    
    start = timer()
    b = y * z
    end = timer()
    print("simple multiplication time: ", end - start)
