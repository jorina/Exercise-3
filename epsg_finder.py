#!/usr/bin/env python3
'''epsg_finder.py

A script which refers to the datum based 
on the user's EPSG value input .
Written by Seppo Karvinen on 23.09.2016 [DDMMYYYY]

Usage: ./epsg_finder.py
'''


user_value = input("What is the EPSG value of the input shapefile? \n")

if user_value == "4326":
    print ("EPSG value 4326 corresponds to WGS84.")
elif user_value == "3067":
    print("EPSG value 3067 corresponds to ETRS-TM35FIN.")
elif user_value == "2392":
    print("EPSG value 2392 corresponds to KKJ / Finland Zone 2.")
else:
    print("There are so many spatial references... I don’t know them all, sorry.")