#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:55:18 2019

@author: Mac
"""

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2
    

class Square:
    def __init__(self, sl):
        self.side_length = sl
    
    def calculate_perimeter(self):
        return self.side_length * 4

rectangle = Rectangle(3, 4)
square = Square(4)
print(rectangle.calculate_perimeter(), square.calculate_perimeter())
