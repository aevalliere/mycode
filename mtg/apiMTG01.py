#!/usr/bin/env python3

#imports at top
import requests

#define main function
def main():
    """Runtime code"""
    
    #create resp, request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    #display methods available
    print(dir(resp))

if __name__ == "__main__":
    main()
