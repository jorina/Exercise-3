#!/usr/bin/env python3
'''make_flag.py

A script designed to create a flag with nested 'for' loops.

Written by Seppo Karvinen on 25.09.2016 [DDMMYYYY]
with some peer support by Hanna.

Usage: ./make_flag.py
'''

star = '*'
line = '-'

for i in range(5):
    for char in star:
        for char2 in line:
            if (i<3):
                text = (7 * star)
                flag = (text + 12 * line)
                print(flag)
            else:
                flag = (19 * line)
                print(flag)