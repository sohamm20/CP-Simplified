# Python3 program to do modular division

from math import gcd

def modDivide(a, b, m):

    g = gcd(b, m)
    if g != 1:
        raise Exception("Division not defined")
        
    return (a * pow(b, m - 2, m)) % m

# This code is Contributed by Soham Mirikar
