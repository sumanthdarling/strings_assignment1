# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:48:36 2020

@author: SATHWIK
"""


def remove(string,n):
    first= string[:n]
    last= string[n+1:]
    return first+last
string= str("enter the string:")
n= int(input("enter the index of charactyer to remove"))
print("modefied string",remove(string,n))