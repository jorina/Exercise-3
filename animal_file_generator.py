#!/usr/bin/env python3
'''animal_file_generator.py

A script designed for batch prosessing with a 'for' loop.

Written by Seppo Karvinen on 25.09.2016 [DDMMYYYY]
with some peer support by Hanna.

Usage: ./animal_file_generator.py
'''

basename = 'Animal'
filenames = ''

for i in range(31):
    print (basename + '_' + str(i))
    
for i in range(31):
    filenames = (basename + '_' + str(i) + '.shp')
    print (filenames)