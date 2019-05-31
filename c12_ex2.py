#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:43:21 2019

@author: Mac
"""

import math

class Circle:
    def __init__(self, r):
        ''' r: 半径 '''
        self.radius = r
    
    def area(self):
        return self.radius **2 * math.pi

circle = Circle(24.6)
print(circle.area())

