#!/usr/bin/env python3

"""This script checks if a file is a .zip"""
import zipfile

def main():
    file = input("Which file would you like to check?\n   ")

    if zipfile.is_zipfile(file):
        print("Ippity pippity, this is a zippity")

    else:
        print("bibbity bobbity this is a floppity")

if __name__ == "__main__":
    main()


