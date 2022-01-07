#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    #Creating resp to simplify future cardset step
    resp = requests.get(f"{API}sets")
    #Creating cardsets to pythonize json
    cardsets = resp.json().get("sets")

    with open("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets:
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

if __name__ == "__main__":
    main()

