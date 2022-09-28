#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""

#imports to read api and change time formatting
import requests
import datetime    
#import to search city and country from coords
import reverse_geocoder as rg

#API URL
URL= "http://api.open-notify.org/iss-now.json"
def main():

    #converts api to json
    resp= requests.get(URL).json()
    
    print("CURRENT LOCATION OF THE ISS:")
    
    #pulls 'epoch' time from json
    time_ugly = resp['timestamp']

    #changes epoch time to readable time
    date_time = datetime.datetime.fromtimestamp(time_ugly)
    
    #longitude and latitude from json
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']

    coords_tuple = (lat,lon)
    
    #search returns ordered list
    result = rg.search(coords_tuple)

    #pull data from search
    city  = result[0]['name']
    country = result[0]['cc']
    print(f"{city}, {country}")
    #displays readable time, longitude, and latitude
    print(f"Timestamp: {date_time}")
    print(f"Lon: {resp['iss_position']['longitude']}")
    print(f"Lat: {resp['iss_position']['latitude']}")

if __name__ == "__main__":
    main()
