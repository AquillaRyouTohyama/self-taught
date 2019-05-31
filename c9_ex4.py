#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:57:08 2019

@author: Mac
"""

import csv

list = [['トップ ガン', 'リスキー ビジネス', 'マイノリティ レポート'], 
        ['タイタニック', 'ザ レベナント', 'インセプション'],
        ['トレーニング デイ', 'マン オン ファイア', 'フライト']]

with open('c9_ex4.csv', 'w', encoding='utf-8') as f:
    for row in list:
        w = csv.writer(f, delimiter=',')
        w.writerow(row)


        