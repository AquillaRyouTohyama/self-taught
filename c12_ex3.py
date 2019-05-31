#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:47:45 2019

@author: Mac
"""

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
    
    def area(self):
        return self.bottom * self.height * 0.5

triangle = Triangle(15, 7.3)
print(triangle.area())

