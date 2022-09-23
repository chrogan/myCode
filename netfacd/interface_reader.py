#!/usr/bin/env python3
import netifaces

def print_mac(i):
    print('MAC: ', end='') # This print statement will always print MAC without an end of line
    print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address

def print_ip(i):
    print('IP: ', end='')  # This print statement will always print IP without an end of line
    print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address


def main():
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print_mac(i)
            print_ip(i)
        except:
            print('Could not collect adapter information :(')


if __name__ == "__main__":
    main()
