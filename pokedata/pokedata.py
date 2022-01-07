#!/usr/bin/env python3

#import pandas for data writing
import pandas as pd


def main():
    #turn pokedex.txt to a excel file
    df = pd.read_csv("pokedex.txt")

    #writeout to excel
    df.to_excel("pokedex-translated.xls")

main()

