#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"

        ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

# search for all movies containing string and type
def movie_lookup_with_type(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    typesearch = input("Please Choose a type from the following: MOVIE, SERIES, OR EPISODE\n").lower()
    if typesearch in ['movie','series','episode']:
        try:
            # begin constructing API
            api = f"{OMDBURL}apikey={mykey}&s={searchstring}&type={typesearch}"

            ## open URL to return 200 response
            resp = requests.get(api)
            ## read the file-like object decode JSON to Python data structure
            return resp.json()
        except:
         return False
    else:
        print("Sorry :/  Invalid input type")

# search for all movies containing string and year
def movie_lookup_with_year(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""

    year_search = input("Please enter the year you would like to search by:\n ")
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}&y={year_search}"

         ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False



# search for all movies containing string and type
def movie_lookup_with_type_and_year(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    typesearch = input("Please Choose a type from the following: MOVIE, SERIES, OR EPISODE\n").lower()
    if typesearch in ['movie','series','episode']:
        year_search = input("Please enter the year you would like to search by:\n ") 
        try:
            # begin constructing API
            api = f"{OMDBURL}apikey={mykey}&s={searchstring}&type={typesearch}&y={year_search}"

            ## open URL to return 200 response
            resp = requests.get(api)
            ## read the file-like object decode JSON to Python data structure
            return resp.json()
        except:
         return False
    else:
        print("Sorry :/  Invalid input type")



def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL, TYPE TEXT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR,TYPE) VALUES (?,?,?)",(data.get("Title"), data.get("Year"),data.get("Type")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    
    cursor = conn.execute("SELECT * from MOVIES")
    for row in cursor:
        print("MOVIE = ", row[0])
        print("YEAR = ", row[1])

def main():

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            Please select one of the following number:
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            3) Search for Movies by a specific year
            4) Search for Movies by type and year
            99) Exit """)

            answer = input("> ") # collect an answer for testing

        # testing the answer
        if answer in ["1", "2","3","4"]:
            # All searches require a string to include in the search
            searchstring = input("Search all movies in the OMDB. What would you like to search for?\n ")

            if answer == "1":
                resp = movielookup(mykey, searchstring)
            elif answer == "2":
                resp = movie_lookup_with_type(mykey,searchstring)
            elif answer == "3":
                resp = movie_lookup_with_year(mykey,searchstring)
            elif answer == "4":
                resp = movie_lookup_with_type_and_year(mykey,searchstring)



            #"continue" can restart the while loop
            if resp:
                # display the results
                resp = resp.get("Search")
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()
