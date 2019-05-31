#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:52:17 2019

@author: Mac
"""

class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

a_rider = Rider('Aquilla')
a_horse = Horse('passer', a_rider)
print(a_horse.rider.name)
