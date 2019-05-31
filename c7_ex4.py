#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:02:35 2019

@author: Mac
"""

a_list= [3, 4, 2, 5, 3, 4, 1, 3, 5]
cnt = 0

while True:
    ans = input('Type a number. (q : end)')
    if ans == str(a_list[cnt]):
        print('正解！')
        break
    elif ans == 'q':
        break
    elif ans not in ['1','2','3','4','5','6','7','8','9','0']:
        print('数字を入力するか、qで終了します。')
        cnt = (cnt+1) % 9
        continue
    else:
        print('不正解')
        cnt =(cnt+1) % 9

