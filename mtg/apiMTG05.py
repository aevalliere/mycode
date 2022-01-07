#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    #create resp
    resp = requests.get(f"{API}sets")

    #dump json
    cardsets = resp.json().get("sets")

    for cardset in cardsets:
        print(cardset)

if __name__ == "__main__":
    main()

