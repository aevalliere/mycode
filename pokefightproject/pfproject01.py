#!/usr/bin/python3

#Setting up the 
import requests

poke = 'http://pokeapi.co/api/v2/pokemon/'

def  showInstructions():
  #print a main menu and the commands
  print('''
Pokefighter
===========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print(rooms[currentRoom]['desc'])
  #print the current inventory
  print('Inventory: ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Pallet Town' : {
                'desc' : 'A quaint village. There lies a route to Viridian City to the north.', 
                'north' : 'Viridian City',
                },
            'Viridian City': {
                'desc' : 'A small town, the gym leader here never seems to be around. To the west lies Indigo Plateau, and to the north lies Pewter City.',
                'west' : 'Indigo Plateau',
                'north' : 'Pewter City',
                'item'  : 'earth badge',
                },
            'Pewter City' : {
                'desc' : 'A town seemingly carved from stone. Everything here exemplifies toughness. To the east lies the massive Mt. Moon.',
                'east' : 'Mt. Moon',
                },
            'Mt. Moon' : {
                'desc' : 'A massive mountain stands before you. If you head towards the west you will reach Pewter City. If you go east you will reach Cerulean City',
                'west' : 'Pewter City',
                'east' : 'Cerulean City',
                'item'  : 'triforce of power',
                },
            'Cerulean City' : {
                'desc' : 'A town where the locals are obsessed with water type pokemon. To the North lies a house. To the south is Saffron City',
                'north' : 'House',
                'south' : 'Saffron City',
                },
            'Saffron City' : {
                'desc' : 'The Shining Big City. To the north is Cerulean City, to the west is Celadon City. Lavender Town is found to the east, and to the south is Vermillion City',
                'north' : 'Cerulean City',
                'west' : 'Celadon City',
                'east' : 'Lavender Town',
                'south' : 'Vermillion City',
                },
            'Vermillion City' : {
                'desc' : 'The Port of Exquisite Sunsets. To the north lies Saffron City, and to the east lies the coast.',
                'north' : 'Saffron City',
                'east' : 'Coast',
                },
            'Lavender Town' : {
                'desc' : 'The Noble Town. To the north lies a house, and to the south is Saffron City.',
                'north' : 'House',
                'south' : 'Saffron City',
                'item' : "triforce of courage",
                },
            'Coast' : {
                'desc' : 'A coastline stretching as far as the eye can see. To the north is Saffron City, to the south Fuscia City can be found, and to the est Vermillion City awaits.',
                'north' : 'Saffron City',
                'south' : 'Fuscia City',
                'east' : 'Vermillion City',
                'item' : 'ghostly mitt',
                },
            'Celadon City' : {
                'desc' : 'The City of Rainbow Dreams. To the west lies Saffron City.',
                'west' : 'Saffron City',
                },
            'Cinnibar Island' : {
                'desc' : 'The Ravaged Town of the Past. To the North you can travel to Pallet Town, and to the east you can surf on open waters.',
                'north' : 'Pallet Town',
                'east' : 'Surfing',
                },
            'Surfing' : {
                'desc' : 'You are in the middle of the ocean, no people are around. All you can see is endless blue water. You know to the west lies Cinnibar Island. You also know to the north lies Fuscia City',
                'west' : 'Cinnibar Island',
                'north' : 'Fuscia City',
                'item'  : 'triforce of wisdom',
                },
            'Indigo Plateau' : {
                'desc' : 'The Ultimate Goal of Trainers!. To the north lies your greatest challenge! To the east lies Pewter City.',
                'east' : 'Pewter City',
                'north' : 'Elite Four - Lorelai',
                },
            'Elite Four - Lorelai' : {
                'desc' : 'In front of you is a lady with red hair. To the north lies the next challenge.',
                'north' : 'Elite Four - Bruno',
                },
            'Elite Four - Bruno' : {
                'desc' : 'In front of you is a muscular man. To the north lies the next challenge.',
                'north' : 'Elite Four - Agatha',
                },
            'Elite Four - Agatha' : {
                'desc' : 'In front of you is a old woman. To the north lies the next challenge.',
                'north' : 'Elite Four - Lance',
                },
            'Elite Four - Lance' : {
                'desc' : 'In front of you is a man wearing a cape. To the north lies the next challenge.',
                'north' : 'Champion',
                },
            'Champion' : {
                'desc' : 'In front of you is a man who you have seen on TV, he is very young and is wearing a red hat. To the north lies the Hall of Fame.',
                'north' : 'Hall of Fame',
                'item'  : 'photograph',
                },
            'Hall of Fame' : {
                'desc' : '',
                },
            'Fuscia City' : {
                'desc' : 'The Happening and Passing City, to the north is the coast, and to the south is a large body of water with a conveniently located Lapras ferry station.',
                'north' : 'Coast',
                'south' : 'Surfing',
                },
         
         }
            
#start the player in the Hall
currentRoom = 'Pallet Town'

showInstructions()

#Give Dscription of the rpg
print("\nYou want to be the very best that no one ever was, and you want to do it by yourself.\nYou are planning on going on an adventure in which you will fight pokemon with your own two hands.\nYou are not some 12 year old that has to save the world because apparently all the adults are incompetent.\nYou just want to show the pokemon who the boss is around these parts.\nDo you have what it takes to be the human pokemon master?")

#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
      
    ## Define how a player can win
    if currentRoom == 'Hall of Fame' and 'Photograph' in inventory:
        print('You have proven that you are the very best, that noone ever was! Now your daily life will consist of continually punching pokemon to maintain your title. THE END')
        break
