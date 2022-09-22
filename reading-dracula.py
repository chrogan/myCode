#!/usr/bin/env python3
"""Spooky Loopin Exercise"""

def main():
    #initialize the amount of vampires
    vampires = 0
    
    #opens dracula file for reading
    file = open('dracula.txt', 'r')

    #reads each line in dracula.txt
    for line in file:

        #makes everything lowercase for matching 
        line = line.lower()

        #prints out each line with the word 'vampire'
        if 'vampire' in line:
            vampires += 1
            print(line)

    #displays the total number of lines with vampire        
    print(f"\nThere are {vampires} references to 'vampire' in this document.")
    
    #REMEMBER TO CLOSE THE FILE!!!
    file.close()


if __name__ == "__main__":
    main()

