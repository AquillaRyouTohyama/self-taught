#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:10:08 2019

@author: Mac
"""

class Square:
    def __init__(self, sl):
        self.side_length = sl
    
    def calculate_perimeter(self):
        return self.side_length * 4

    def change_size(self, dif):
        self.side_length += dif
        
square = Square(12)
print(square.calculate_perimeter())
square.change_size(-3)
print(square.calculate_perimeter())
