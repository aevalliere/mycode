#!/usr/bin/python3

def  showInstructions():
  #print a main menu and the commands
  print('''
Pokefighter
===========
Commands:
  go [direction]
  get [item]
  use [item]
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

#an inventory, which will initially contain the item fist, and the item infinite potion
inventory = ["fist", "potion"]

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Pallet Town' : {
                'desc' : 'A quaint village. There lies a route to Viridian City to the north. To the south of town is a small beach', 
                'north' : 'Viridian City',
                'south' : 'Cinnibar Island',
                },
            'Viridian City': {
                'desc' : 'A small town, the gym leader here never seems to be around. To the west lies Indigo Plateau, to the south is Pallet Town and to the north lies Pewter City.',
                'west' : 'Indigo Plateau',
                'north' : 'Pewter City',
                "south" : 'Pallet Town',
                'item'  : 'earth badge',
                'monster' : '0',
                },
            'Pewter City' : {
                'desc' : 'A town seemingly carved from stone. Everything here exemplifies toughness. To the east lies the massive Mt. Moon and to the south is Viridian City.',
                'east' : 'Mt. Moon',
                'south' : ' Viridian City',
                'monster' : '1',
                'item'  : 'boulder badge',
                },
            'Mt. Moon' : {
                'desc' : 'A massive mountain stands before you. If you head towards the west you will reach Pewter City. If you go east you will reach Cerulean City',
                'west' : 'Pewter City',
                'east' : 'Cerulean City',
                'item'  : 'triforce of power',
                'monster' : '2',
                },
            'Cerulean City' : {
                'desc' : 'A town where the locals are obsessed with water type pokemon. To the north lies a house. To the south is Saffron City, and to the west is Mt. Moon',
                'north' : 'House',
                'south' : 'Saffron City',
                'west' : 'Mt. Moon',
                'monster' : '3',
                'item'  : 'cascade badge',
                },
            'Saffron City' : {
                'desc' : 'The Shining Big City. To the north is Cerulean City, to the west is Celadon City. Lavender Town is found to the east, and to the south is Vermillion City',
                'north' : 'Cerulean City',
                'west' : 'Celadon City',
                'east' : 'Lavender Town',
                'south' : 'Vermillion City',
                'monster' : '4',
                'item'  : 'marsh badge',
                },
            'Vermillion City' : {
                'desc' : 'The Port of Exquisite Sunsets. To the north lies Saffron City, and to the east lies the coast.',
                'north' : 'Saffron City',
                'east' : 'Coast',
                'monster' : '5',
                'item'  : 'thunder badge',
                },
            'Lavender Town' : {
                'desc' : 'The Noble Town. A long coastline lies to the south, and to the west is Saffron City.',
                'south' : 'Coast',
                'west' : 'Saffron City',
                'item' : 'triforce of courage',
                'monster' : '7',
                },
            'Coast' : {
                'desc' : 'A coastline stretching as far as the eye can see. To the north is Saffron City, to the south Fuscia City can be found, and to the west Vermillion City awaits.',
                'north' : 'Lavender Town',
                'south' : 'Fuscia City',
                'west' : 'Vermillion City',
                },
            'Celadon City' : {
                'desc' : 'The City of Rainbow Dreams. To the east lies Saffron City.',
                'east' : 'Saffron City',
                'monster' : '8',
                'item'  : 'rainbow badge',
                },
            'Cinnibar Island' : {
                'desc' : 'The Ravaged Town of the Past. To the North you can travel to Pallet Town, and to the east you can surf on open waters.',
                'north' : 'Pallet Town',
                'east' : 'Surfing',
                'monster' : '9',
                'item'  : 'volcano badge',
                },
            'Surfing' : {
                'desc' : 'You are in the middle of the ocean, no people are around. All you can see is endless blue water. You know to the west lies Cinnibar Island. You also know to the north lies Fuscia City',
                'west' : 'Cinnibar Island',
                'north' : 'Fuscia City',
                'item'  : 'triforce of wisdom',
                },
            'Indigo Plateau' : {
                'desc' : 'The Ultimate Goal of Trainers!. To the north lies your greatest challenge, but beware once you start you won\'t be able to stop! To the east lies Pewter City.',
                'east' : 'Pewter City',
                'north' : 'Elite Four - Lorelai',
                },
            'Elite Four - Lorelai' : {
                'desc' : 'In front of you is a lady with red hair. To the north lies the next challenge.',
                'north' : 'Elite Four - Bruno',
                'monster' : '10',
                },
            'Elite Four - Bruno' : {
                'desc' : 'In front of you is a muscular man. To the north lies the next challenge.',
                'north' : 'Elite Four - Agatha',
                'monster' : '11',
                },
            'Elite Four - Agatha' : {
                'desc' : 'In front of you is a old woman. To the north lies the next challenge.',
                'north' : 'Elite Four - Lance',
                'monster' : '12',
                },
            'Elite Four - Lance' : {
                'desc' : 'In front of you is a man wearing a cape. To the north lies the next challenge.',
                'north' : 'Champion',
                'monster' : '13',
                },
            'Champion' : {
                'desc' : 'In front of you is a man who you have seen on TV, he is very young and is wearing a red hat. To the north lies the Hall of Fame.',
                'north' : 'Hall of Fame',
                'monster' : '14',
                },
            'Hall of Fame' : {
                'desc' : 'A Hall for Champions, to the south is the Champion\'s room.',
                'south' : 'Champion',
                },
            'Fuscia City' : {
                'desc' : 'The Happening and Passing City, to the north is the coast, and to the south is a large body of water with a conveniently located Lapras ferry station.',
                'north' : 'Coast',
                'south' : 'Surfing',
                'monster' : '6',
                'item'  : 'soul badge',
                },
            'House' : {
                'desc' : 'A man named Bill\'s house. You keep hearing him mutter about how collecting all three pieces of the triforce will bring unlimited power.',
                'south' : 'Cerulean City',
                },
         
         }
            
#start the player in the Hall
currentRoom = 'Pallet Town'

showInstructions()

#Give Description of the rpg
print("\nYou want to be the very best that no one ever was, and you want to do it by yourself.\nYou are planning on going on an adventure in which you will fight pokemon with your own two hands.\nYou are not some 12 year old that has to save the world because apparently all the adults are incompetent.\nYou just want to show the pokemon who the boss is around these parts.\nDo you have what it takes to be the human pokemon master?")

def clear():
    # check and make call for specific operating system
    _ = call('clear' if osname =='posix' else 'cls')

bestiary = [{'name' : 'Caterpie', 'health' : 45, 'damage' : '30'},
            {'name' : 'Geodude', 'health' : 40, 'damage' : '80'},
            {'name' : 'Clefairy', 'health' : 70, 'damage' : '45'},
            {'name' : 'Starmie', 'health' : 60, 'damage' : '45'},
            {'name' : 'Alakazam', 'health' : 55, 'damage' : '50'},
            {'name' : 'Raichu', 'health' : 60, 'damage' : '90'},
            {'name' : 'Venomoth', 'health' : 70, 'damage' : '65'},
            {'name' : 'Haunter', 'health' : 45, 'damage' : '50'},
            {'name' : 'Victreebel', 'health' : 80, 'damage' : '105'},
            {'name' : 'Arcanine', 'health' : 90, 'damage' : '110'},
            {'name' : 'Lapras', 'health' : 130, 'damage' : '85'},
            {'name' : 'Machamp', 'health' : 90, 'damage' : '130'},
            {'name' : 'Gengar', 'health' : 60, 'damage' : '65'},
            {'name' : 'Dragonite', 'health' : 91, 'damage' : '134'},
            {'name' : 'Red\'s Pikachu', 'health' : 172, 'damage' : '119'},
            ]

playerstrength = 30
player_health = 300
#inventory = []
def combat():
    try:
        global player_health, inventory, bestiary
        round = 1
        bestiaryentry = rooms[currentRoom]['monster']
        monster_ID = int(bestiaryentry)
        monster_health = bestiary[monster_ID]['health']
        if 'monster' in rooms[currentRoom]:
            print(f"A {bestiary[monster_ID]['name']} has appeared")
        else:
            pass
        while True:
            print("Player Health: [" + str(player_health) + "]")
            print("Pokemon\'s Health: [" + str(monster_health) + "]")

            print("Type: USE [item]") 
            move = input().lower().split(" ", 1) 
            monster_damage = (bestiary[monster_ID]['damage'])
            print("\n=========================")


            if move[0] == 'use': #
                if "fist" in inventory and move[1] == 'fist': # checks if weapon is in your inventory
                    print(f"You hit a {bestiary[monster_ID]['name']} for {playerstrength} damage!")
                    try:
                         monster_health -= int(playerstrength)
                    except:
                        pass
                    if monster_health <= 0:
                        print(f"The {bestiary[monster_ID]['name']} has been knocked out.\n")
                        del rooms[currentRoom]['monster']
                        break

                    print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                    print ("=========================\n")

                    player_health -= int(monster_damage)
                if 'potion' in inventory and move[1] == 'potion':
                    print("You drink from the potion. Your health has been restored!")
                    print("Your potion magically refills itself! Handy!")
                    if player_health <=200:
                        player_health += 100
                    else:
                        player_health += 30
                    print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                    print ("=========================\n")

                    player_health -= int(monster_damage)
                if move[1] not in inventory:
                    print(f"There is no {move[1]} in your inventory!")
            else:
                print('That is not a valid command')
    except:
        pass
#loop forever
while True:

    showStatus()
    combat()
    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them       
    move = move.lower().split(" ", 1)
    
    #if they type 'go' first
    if move[0] == 'go':
        #Must fight pokemon
        if 'monster' in rooms[currentRoom]:
            print (f"A {bestiary[monster_ID]['name']} is in the way")
        else:
           # if 'boulder badge' and 'cascade badge' and 'thunder badge' and 'rainbow badge' and 'soul badge' and 'marsh badge' and 'volcano badge' and 'earth badge' not in inventory and rooms[currentRoom] == 'Viridian City' and move[1] == 'west':
            #    print('You are only allowed past this point once you have collected all eight gym badges.')
            #   currentRoom = 'Viridian City'
            if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
                #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if 'monster' in rooms[currentRoom]:
            print (f"A {bestiary[monster_ID]['name']} is in the way")
        else:
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
    
    if move[0].lower() == 'use':
        if move[1].lower() == 'potion' and 'potion' in inventory:
            print("You drink from the potion. Your health has been restored!")
            print("Your potion magically refills itself! Handy!")
            player_health = 300
        else:
            print("You can\'t use that.")
    
    #Quest reward
    if 'triforce of courage' in inventory and 'triforce of wisdom' in inventory and 'triforce of power' in inventory:
        playerstrength = 1000
        print("You have been granted the strength to one hit ko everything. Use your power wisely.")
    

    ## Define how a player can win
    if currentRoom == 'Hall of Fame':
        print('You have proven that you are the very best, that noone ever was! Now your daily life will consist of continually punching pokemon to maintain your title. THE END')
        break
