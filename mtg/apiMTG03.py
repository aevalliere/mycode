#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

#setting up main function
def main():
    resp = requests.get(f"{API}sets")
    print(resp.json())

if __name__ == "__main__":
    main()

