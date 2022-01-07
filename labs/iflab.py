#!/usr/bin/env python3

#Escape the maze game
print("You have been teleported into a maze you must now escape") 

def text():
    #First path routes
    while True:
        path = input("\nYou are presented with three paths. To the left a long winding cobble stone path, to the center a path that follows a dark and gloomy ocean, and to the right a path that takes you into a cold misty forest. Which do you choose? (Left, Center, or Right)").capitalize()
        if path == "Left":
            print("\nYou continue along the cobble stone path.")
            break
        elif path == "Center":
            print("\nA giant whale leaps out of the water and drags you to a watery grave. Try again.")
        elif path == "Right":
            print("\nYou continue towards the wooded path... leaves crunching with each step you take.")
            break
        else:
            print("\nA spirit descends to harvest your soul for being unable to follow directions. Try again.")

    #Path left continuation
    while path == "Left":
        print("\nYou come to a fork in the road and are again tasked with making a decision. The two paths laid before you pass by different settlements. The path to your left passes by a village where you can see children and people roaming about, the other passes by what appears to be an empty saloon.")
        route = input("\nWhat path do you choose? (Left, Right)").capitalize()
        if route == "Left":
            print("\nWrong decision, the village is the home of a group of ravenous cannibals! They are quite cordial among themselves but to outsiders they are quite vicious. Try Again.")
        elif route == "Right":
            print("\nYou continue on")
            break
        else:
            print("\nA spirit descends to harvest your soul for being unable to follow directions. Try again.")

    #Path right continuation
    while path == "Right":
        print("\nYou come to a fork in the road and are again tasked with making a decision. To your left lies a wide desert, and to your right are rolling hills ")
        route = input("\nWhat path do you choose? (Left, Right)").capitalize()
        if route == "Right":
            print("\nYou decided to go over the rolling hills, however you didn't realize the hills were quite literally rolling and because of your blunder the crushed you under their massive size. Try again")
        elif route == "Left":
            print("\nYou decide to try your hand at passing through the desert.")
            break
        else:
            print("\nA spirit descends to harvest your soul for being unable to follow directions. Try again.")

    while True:
        if route == "Left":
            print("\nAfter wandering through the desert you find an Oasis with people and food. Your travels have exhausted you and you decide to make this your home. You live comfortably for years until you die of old age. You may not have escaped but this ending isn't too bad.")
            break
        elif route == "Right":
            print("\nYou continue past the saloon, and eventually you run into a massive grey wall that seems to stretch into the sky. You find what appears to be a handle and you pull on it. A door opens in the wall, and you walk through....\nCongratulations you have successfully cleared the maze!")
            break
        
    print("Program terminated")
 
if __name__ == "__main__":
    text()
