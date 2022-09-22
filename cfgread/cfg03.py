#!/usr/bin/env python3


input_file = input("Please enter a file name to read: ")

## create file object in "r"ead mode
with open(input_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

