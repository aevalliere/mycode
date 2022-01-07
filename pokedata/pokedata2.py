#!/usr/bin/env python3

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    #define excel file
    excel_file = 'pokedex-translated.xls'

    poke_df = pd.read_excel(excel_file, index_col=2)
    
    #List strongest attack then chart it
    print("\nThe 10 pokemon with the highest attack are:\n")
    sorted_by_attack = poke_df.sort_values(["Attack"], ascending=False)    
    print(sorted_by_attack.head(10))
    sorted_by_attack['Attack'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/attackhigh.png", bbox_inches='tight')

    #Weakest
    print("\nThe 10 pokemon with the lowest attack are:\n")
    sorted_by_attack_low = poke_df.sort_values(["Attack"], ascending=True)
    print(sorted_by_attack_low.head(10))
    sorted_by_attack_low['Attack'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/attacklow.png", bbox_inches='tight')

    #Strongest defense
    print("\nThe 10 pokemon with the highest defense are:\n")
    sorted_by_defense = poke_df.sort_values(["Defense"], ascending=False)
    print(sorted_by_defense.head(10))
    sorted_by_defense['Defense'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/defensehigh.png", bbox_inches='tight')
    
    #Weakest
    print("\nThe 10 pokemon with the lowest defense are:\n")
    sorted_by_defense_low = poke_df.sort_values(["Defense"], ascending=True)
    print(sorted_by_defense.head(10))
    sorted_by_defense_low['Defense'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/defenselow.png", bbox_inches='tight')

    #Fastest speed
    print("\nThe 10 pokemon with the highest speed are:\n")
    sorted_by_speed = poke_df.sort_values(["Speed"], ascending=False)
    print(sorted_by_speed.head(10))
    sorted_by_speed['Speed'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/speedhigh.png", bbox_inches='tight')
    
    #Weakest
    print("\nThe 10 pokemon with the lowest speed are:\n")
    sorted_by_speed_low = poke_df.sort_values(["Speed"], ascending=True)
    print(sorted_by_speed_low.head(10))
    sorted_by_speed_low['Speed'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/attackhigh.png", bbox_inches='tight')

    

if __name__ == "__main__":
    main()
