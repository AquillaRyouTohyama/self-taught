#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:03:15 2019

@author: Mac
"""

my_Home = (35.1938023, 136.9369374)

my_Working_place = (35.1797853, 136.9083329)

my_data = {'自宅': my_Home, '職場': my_Working_place}

key = input('1:自宅、　２：職場　選んでください。：')

if key == '1':
    key = '自宅'
    print(my_data[key])
elif key == '2':
    key = '職場'
    print(my_data[key])
else:
    print('表示できません')
