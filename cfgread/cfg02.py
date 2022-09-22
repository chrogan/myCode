#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

#display the whole file 
file = configfile.read()

#makes the file into a list with each line
list = file.splitlines()
 
#displays that list
print(list)

#always close the file
configfile.close()
