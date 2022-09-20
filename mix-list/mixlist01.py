#!/usr/bin/env python3

#created a list with IP, port, and state
my_list = [ "192.168.0.5", 5060, "UP" ]

#prints out the first item in the list
print("The first item in the list (IP): " + my_list[0])

#prints out the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

#prints out the third item in the list
print("The last item in the list (state): " + my_list[2] )

#challenge list
iplist = [5030,"80", 55, "10.0.0.1","10.20.30.1", "ssh"]

#displays only the ip addresses from iplist
print(f"{iplist[3]} and {iplist[4]} are the only IP addresses in the list provided")




