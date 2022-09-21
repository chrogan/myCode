#!/usr/bin/env python3

""" This script is used to show how to move and rename files or folders"""

import shutil # shell utilities will be used to move files
import os # provides access to low level os operations (agnostic to flavor of OS)

def main():
    #changing into the mycode directory
    os.chdir('/home/student/mycode/')

    #moving raynor file to ceph_storage folder
    shutil.move('raynor.obj', 'ceph_storage/')
    
    #ask the user for a new name for a file
    xname = input('What is the new name for kerrigan.obj? ')
    
    #the .move method will also override a current file
    #the following code takes the input from the user and overrides the name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()
