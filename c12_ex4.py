#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:54:08 2019

@author: Mac
"""

class Hexagon:
    def __init__(self, sl_1, sl_2, sl_3, sl_4, sl_5, sl_6):
        self.side_length_1 = sl_1
        self.side_length_2 = sl_2
        self.side_length_3 = sl_3
        self.side_length_4 = sl_4
        self.side_length_5 = sl_5
        self.side_length_6 = sl_6
        
        
    def calculate_perimeter(self):
        return self.side_length_1 + \
            self.side_length_2 + self.side_length_3 + \
            self.side_length_4 + self.side_length_5 + \
            self.side_length_6 

hexagon = Hexagon(6.2, 4.3, 5.3, 7.1, 2.5, 4.4)
print(hexagon.calculate_perimeter())
