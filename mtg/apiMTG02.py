#!/usr/bin/env python
"""Author: Alex Valliere

    Description: A script to interact with an open API"""
    
#imports
import requests

#define base api
API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""
    resp = requests.get(f"{API}sets")
    
    #Display the methods available to our new project
    print(dir(resp))
    
if __name__ == "__main__":
    main()
    3
