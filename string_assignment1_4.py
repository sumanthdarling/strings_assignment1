# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:47:39 2020

@author: SATHWIK
"""


def swape(str1,str2):
    new_a= str2[:2]+str1[2:]
    new_b= str1[:2]+str2[2:]
    
    return new_a+ ' '+new_b
print(swape("abc","xyz"))