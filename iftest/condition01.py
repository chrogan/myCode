#!/usr/bin/env python3

""" This script is an example of testing if statements"""

def main():
    #create string
    hostname = input('What value should we set for hostname?')
    hostname = hostname.lower()

    #testing if logic
    if hostname == 'mtg':
        print("The hostname is indeed MTG")
        print('hostname matches the expected configuration')
    print("Exiting script, Thank you!")

if __name__=="__main__":
    main()

