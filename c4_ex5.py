#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:21:29 2019

@author: Mac
"""

def str2float(string):
    try:
        return float(string)
    except :
        print('Could not convert the string to a float.')

print(str2float('12234.455'))

