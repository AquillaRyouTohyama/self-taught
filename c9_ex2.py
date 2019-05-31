#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:54:07 2019

@author: Mac
"""

Name = input("What's your Name? ")

with open('name.txt', 'w', encoding='utf=8') as f:
    f.write(Name)
