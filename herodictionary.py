#!/usr/bin/env python3

#To get characters name
char_name = input("What character would you like to know about? (batman, flash, or superman): ")

#To get statistic you want to look up
char_stat = input("What statistic would you like to look up? (speed, strength, intelligence): ")

#Set up dictionary
superhero = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

#Print dictionary results
print(char_name + "\'s", char_stat, "is:",  superhero[char_name][char_stat])
