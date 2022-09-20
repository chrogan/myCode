#!/usr/bin/env python3
import random
""" This script is used to challenge the use of lists"""

def main():
    #lists of our wordbank and student names
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    #added 4 to our word bank
    wordbank.append(4)

    #user decides if they want to submit a name, number, or pick random
    case = input("Would you like to pick submit a name, number, or choose randomly?\n")

    #different outputs based on original user input
    if case == "name":
        entered_name = input("Please enter a name\n")
        print(f"{entered_name} is the name you've chosen.\nWow, couldn't have chosen something better?")

    elif case == "number":
        num = int(input("Please enter a number between 0 - 18\n"))
        student_name = tlgstudents[num]
        print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    else:
        other_student = tlgstudents[random.randint(0,18)]
        print(f"{other_student} is our other student that likes to uses spaces.\nThey also like to eat crayons.")


if __name__ == "__main__":
    main()
