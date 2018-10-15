#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:58:26 2018

@author: vlad
"""

def double(x):
    if type(x)==list:
        return (x+x,[2*y for y in x])
    return (x, 2*x)


x = 3.
print(double(x) == (3., 6.))
print(x == 3.)

z = [3]
print(double(z) == ([3, 3], [6]))
print(z == [3])

w = [1, 2, 3]
print(double(w) == ([1, 2, 3, 1, 2, 3], [2, 4, 6]))
print(w == [1, 2, 3])
