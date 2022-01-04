#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")

#If statment matching expected config
if hostname == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config.")
#If statement matches but in other than expected format 
elif hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname does not match expected config.")
#If statement doesn't match mtg
elif hostname != "mtg":
    print("Wrong..., try again with mtg")
#Exiting script notification

print("Exiting script")
