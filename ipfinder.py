#!/usr/bin/env python3

import netifaces

def main ():
    for x in netifaces.interfaces():
        #Deets
        print('\n********Details of Interface - ' + x + ' ********')
        try:
            #MAC Addresses
            print('MAC: ', end = '')
            print((netifaces.ifaddresses(x)[netifaces.AF_LINK])[0]["addr"])
            #IP Addresses
            print('IP: ', end = '')
            print((netifaces.ifaddresses(x)[netifaces.AF_INET])[0]["addr"])
        except:
            print('Could not collect adapter information') #prints an error message

main()
