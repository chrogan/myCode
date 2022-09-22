#!/usr/bin/env python3 

""" This script is used an example of using for loops challenge"""

def main():
    #given
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    #prints each index
    for farm in farms:
        print(f"The {farm.get('name')} has: ")
        
        for stuff in farm.get('agriculture'):
            print(f" {stuff.capitalize()}")

    
if __name__ == "__main__":
    main()

