#!/usr/bin/env python3

"""This script will be used for advanced lists challenge"""

def main():
    #created a list with animals < 3 letters
    list = ['Fox','Fly','Ant','Bee','Cod','Cat']
    list2 = ['Fox Fly Ant Bee Cod Cat']

    #iterate over each item in list and display
    for i in list:
        print(i)

    #displays the entire list
    print(*list, sep =',')
    print(list2)

if __name__ == "__main__":
    main()

