# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:46:46 2020

@author: SATHWIK
"""


def long(list):
    a= len(list[0])
    print("len(list[0])",a)
    b= len(list[1])
    print("len(list[1])",b)
    c= len(list[2])
    print("len(list[2])",c)
    if a>b:
        if a>c:
            return a
    elif b>c:
            return b
    else:
            return c