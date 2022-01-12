#!/usr/bin/python3

#Accepts arguments from the command line
import argparse
#Makes http requests
import requests
#Works with data in lots of formats
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():
    #Make http requests
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = iitems.json()
    #create a list to store searched words
    matchedwords = []

    #loop through data
    for item in items.get("results"):
        if args.searchword in item.get('name'):
            matchedwords.append(item.get('name'))

    finished list = matchedwords.copy()

    matchedwords ={}

