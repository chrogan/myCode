#!/usr/bin/env python3
""" This code is an example of use in conditionals logic"""

def main():
    #displays what we are talking about
    print("This python course has been pretty fun!\n")
    print("If we received a grade on how you've done so far, what do you think you would have?")
    
    #asks user for a numerical score
    score = int(input("Please enter a score from 0-100: "))
    
    #if input is not a number between 1-100
    if score >=0 and score <=100:
        
        #the following are scores and their associated grades
        if score >= 90:
            print(f"\nWow, a score of {score} is pretty great! You have an 'A'")

        elif score>=80 and score<90:
            print(f"\nIf you had a score of {score}, you would have a 'B'. Not bad!!")
    
        elif score>=70 and score<80:
            print(f"\nWith a score of {score}, you would have a 'C'. I guess you pass :/")

        elif score>=60 and score<70:
            print(f"\nWith a score of {score}, you would have a 'D'.  You got some work to do :(")

        else:
            print(f"\nWith a score of {score}, you FAIL! Big fat 'F' for you.  Reconsider your line of work lol")
    
    #tells the user that they are dumb
    else:
        print("\nSomeone needs to learn to read. Directions say enter between 1-100.")

if __name__=="__main__":
    main()
