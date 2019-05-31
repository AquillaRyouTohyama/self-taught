#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:07:50 2019

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
    square_list = []
    
    def __init__(self, sl):
        self.side_length = sl
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.side_length * 4
