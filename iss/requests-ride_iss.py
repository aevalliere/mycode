#!/usr/bin/python3

import requests

space = 'http://api.open-notify.org/astros.json'

def main():
    """Runtime code"""

    #Calling webservice
    iss = requests.get(space)
    
    #Convert json to python
    groundctrl = iss.json()

    #Display data
    print("\nConverted Python Data")
    print(groundctrl)

    print("\nPeople in space: ", groundctrl['number'])
    people = groundctrl['people']
    print(people)

if __name__ == "__main__":
    main()

