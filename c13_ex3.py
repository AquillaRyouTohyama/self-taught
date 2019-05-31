#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:31:35 2019

@author: Mac
"""

class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        return 'I am a shape.'

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2
   

class Square(Shape):
    def __init__(self, sl):
        self.side_length = sl
    
    def calculate_perimeter(self):
        return self.side_length * 4

rectangle = Rectangle(3, 4)
square = Square(4.5)
print(rectangle.what_am_i(), rectangle.calculate_perimeter())
print(square.what_am_i(),square.calculate_perimeter())
