#!/usr/bin/env python3
""" This code is an example of use in conditionals logic and while loops practice for project1"""

def main():
    #displays the script's purpose
    print("This python course has been pretty fun!\n")
    print("Based on how you're doing so far, what grades do you think you'll have on your 3 projects?")
    

    quit = ''
    count = 0
    scores = 0.0
    grade = 0.0
    #run this loop as long as the user does type 'q'
    while (quit !='q'):

        #instruct the user to hit 'q' at anypoint to quit of the program
        print("\nIf you no longer want to test out scores, just hit the 'q' key to exit the program.\n")

        #asks user for a numerical score
        while count < 3:
            project = input("Please enter a score from  0-100 for a project: ")
            
            #if the score is a number turn it into a float and add up the inputs
            try:
                project = float(project)
                scores = scores + project
                count = count + 1

            #if the input is not a number
            except:
                    #if the input is 'q' exit the program
                if project == 'q':
                    print("\n\n Okay bye....")
                    quit = 'q'
                    break
                    #if weird input, try again
                else:
                     print("Please enter numeric digits")

        #takes the average of the scores
        grade = scores / 3
        #if input is not a number between 1-100
        if grade >= 0 and grade <= 100:
        
            #the following are scores and their associated grades
            if grade >= 89.5:
                print(f"\nWow, a grade of {grade} is pretty great! You have an 'A'")
                
            elif grade>=79.5 and grade<89.5:
                print(f"\nYour grade would be {grade}, you would have a 'B'. Not bad!!")
                
            elif grade>=69.5 and grade<79.5:
                print(f"\nWith a score of {grade}, you would have a 'C'. I guess you pass :/")
                 
            elif grade>=59.5 and grade<69.5:
                print(f"\nWith a score of {grade}, you would have a 'D'.  You got some work to do :(")
                
            else:
                 print(f"\nWith a score of {grade}, you FAIL! Big fat 'F' for you.  Reconsider your line of work lol")
                
    #tells the user that they are dumb
        else:
            print("\nSomeone needs to learn to read. Directions say enter between 1-100.")
        count = 0


if __name__=="__main__":
    main()
