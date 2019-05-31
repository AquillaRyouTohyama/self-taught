#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:57:58 2019

@author: Mac
"""

words = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']

new_words = []

for word in words:
    word += ' '
    new_words.append(word)

result =  ''.join(new_words)[:-3] + '.'
print(result)
