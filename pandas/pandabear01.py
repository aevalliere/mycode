#!/usr/bin/env python3

#imports
import pandas as pd

def main():
    #define file
    excel_file = 'movies.xls'

    #create data frame object
    movies = pd.read_excel(excel_file)

    #show first five rows of data frame
    print(movies.head())

    #Choose first column "Title" as index
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    #DF has 5 rows and 25 cols, print top 10 in DF
    print(movies_sheet1.head())

    # export 5 movies from the top dataframe to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")

    # export 5 movies from the top of the dataframe to json
    movies_sheet1.head(5).to_json("5movies.json")

    # export 5 movies from the top of the dataframe to csv
    movies_sheet1.head(5).to_csv("5movies.csv")

if __name__ == "__main__":
    main()
