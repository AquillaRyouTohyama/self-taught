#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:57:08 2019

@author: Mac
"""

import csv

list = [['Top Gun', 'Risky Business', 'Minority Report'], 
        ['Titanic', 'The Revenant', 'Inception'],
        ['Training Day', 'Man on Fire', 'Flight']]

with open('c9_ex3.csv', 'w', encoding='utf-8') as f:
    for row in list:
        w = csv.writer(f, delimiter=',')
        w.writerow(row)


        