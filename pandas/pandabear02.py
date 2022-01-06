#!/usr/bin/env python3

import pandas as pd

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    #define xls name
    excel_file = 'movies.xls'

    #Choose first column
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet1.head())

    #grabbing more sheets
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet3.head())

    #combine all into one
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # number rows and columns
    print(movies.shape)

    #toss dupes
    movies.drop_duplicates(inplace=True)

    print (movies.shape)

    #sort by gross
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    #Top ten grossing movies
    print(sorted_by_gross.head())

    #stacked bar
    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")

    #save as stackedbar.png
    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')

if __name__ == "__main__":
    main()
