#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
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
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'desc' : 'A long hallway. The walls are barren and there are no signs of life beyond large scratches marking the floor. To the South you see a kitchen, and to the East what appears to be a dining room.',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                },
            'Kitchen' : {
                  'desc' : 'A dark kitchen is before your eyes. It has been utterly destroyed by the creature that had made the kitchen its nest. The only exit is to the north, where the hall you started from awaits.',
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'desc' : 'You see a long dining table, with chairs strewn about. To the West you see the hall you started in, to the south you see a beautiful garden, and to the north you see a door leading to what you assume is a pantry.',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                },
            'Garden' : {
                  'desc' : 'A sunny and delightful location, with fresh flowers blooming everywhere. A stark contrast from inside the house. A locked gate covered in magical vines impedes your way out of this insanity. To the North you can see the dining room where you came from.',
                  'north' : 'Dining Room',
                },
            'Pantry' : {
                  'desc' : 'A cramped pantry. Food used to be stored here but it has long since been emptied. To the South is the Dining Room, to the East you notice a tunnel that you believe you can squeeze through.',
                  'south' : 'Dining Room',
                  'east' : 'Tunnel',
                  'item' : 'cookie',
                },
            'Tunnel' : {
                'desc' : 'Your belief in being able to squeeze through is questionable. You can only squirm forwards towards the North  and can no longer turn back.',
                'north' : 'Another World',
                'item' : "Sword",
                },
            'Another World' : {
                'desc' : "A beautiful land full magic and wonders",
                },
            
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

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
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    
    elif 'sword' in inventory and 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You hack at the monster with the sword you found. You have slain the monster. The house is yours.')
        break

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break  


    elif currentRoom == 'Another World':
        print('You emerge in a new world. The entrance you came in disappears. Welcome to your new life.')
        break
    
