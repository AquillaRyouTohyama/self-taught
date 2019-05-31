#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:45:40 2019

@author: Mac
"""

inp1 = input('type document name :')
inp2 = input('type parson name :')

string = '私は昨日{}を書いて、{}に送った。'
print(string.format(inp1, inp2))
