# Python Text RPG
# Author: Lan Luu
# Create: 04/07/2025

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player setup ###
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'starting_zone'
myPlayer = Player()


### Title Screen ###
def title_sceen_selections():
    option = input("> ")
    
    if option.lower() == ("play"):
        start_game() # Placeholder until written
    elif option.lower() == ("help"):
        help_menu() 
    elif option.lower() == ("quit"):
        sys.exit()
    
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter an valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # Placeholder until written
        elif option.lower() == ("help"):
            help_menu() 
        elif option.lower() == ("quit"):
            sys.exit()

def title_sceen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#################################")
    print("# WELCOME TO THE TEXT-BASE RPG! #")
    print("#################################")
    print("            - Play -             ")
    print("            - Help -             ")
    print("            - Quit -             ")
    print("  Copyright 2025 lanluu@pdx.edu  ")
    title_sceen_selections()
    
def help_menu():
    print("#################################")
    print("# WELCOME TO THE TEXT-BASE RPG! #")
    print("#################################")
    print("- Use Up, Down, Left, Righ to move")
    print("- Type your command to do them")
    print("- Use 'Look' To inspect something")
    print("- Good luck and have fun!")
    title_sceen_selections()

### GAME FUNCTIONALITY ###
def start_game():
    pass

### MAP ###

'''
MAP LAYER
    Player started at b2
  1   2   3   4
-----------------
|   |   |   |   |   a
----------------- 
|   | x |   |   |   b
-----------------
|   |   |   |   |   c
-----------------
|   |   |   |   |   d 
-----------------
'''

# CONSTANT
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

'''
# Later upgrade
class Zone:
    def __init__(self):
        self.zone_name = ''
        self.description = 'description'
        self.examination = 'examine'
        self.solved = False
        self.up = ''
        self.down = ''
        self.left = ''
        self.right = ''
'''

# solved grid
solved_places = { 'a1': False, 'a2': False, 'a3':False, 'a4': False
                , 'b1': False, 'b2': False, 'b3':False, 'b4': False
                , 'c1': False, 'c2': False, 'c3':False, 'c4': False
                , 'd1': False, 'd2': False, 'd3':False, 'd4': False
                 }

# zone map dictionary (better make a zone class instead of using 16 dict)
zone_map = {
    'a1': {
        'ZONENAME': 'Town Entrance',
        'DESCRIPTION': 'A large archway marks the entrance to the town, with guards stationed at either side.',
        'EXAMINATION': 'The town gates creak open as travelers pass through. The scent of baked bread and fresh flowers fills the air.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2'
    },
    'a2': {
        'ZONENAME': 'Town Square',
        'DESCRIPTION': 'A bustling square in the heart of the town, where vendors sell their wares.',
        'EXAMINATION': 'The square is full of activity, with street performers, merchants, and townsfolk going about their business.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3'
    },

    'a3': {
        'ZONENAME': 'Town Market',
        'DESCRIPTION': 'A busy marketplace where merchants and traders from far and wide come to sell their goods.',
        'EXAMINATION': 'The air is filled with the sounds of bartering and the smell of fresh produce and exotic spices.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4'
    },

    'a4': {
        'ZONENAME': 'Town Tavern',
        'DESCRIPTION': 'A warm, inviting tavern that serves as a gathering place for locals and travelers alike.',
        'EXAMINATION': 'The tavern is lively with the sounds of laughter and music. The scent of roasting meat fills the air.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': ''
    },

    'b1': {
        'ZONENAME': 'Village Entrance',
        'DESCRIPTION': 'A small, peaceful village at the edge of the forest.',
        'EXAMINATION': 'A wooden sign marks the entrance to the village. You hear the faint sound of a blacksmith hammering away.',
        'SOLVED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'LEFT': '',
        'RIGHT': 'b2'
    },

    'b2': {
        'ZONENAME': 'Character Home',
        'DESCRIPTION': 'Your humble abode, a small house tucked away in the village.',
        'EXAMINATION': 'The familiar warmth of your home surrounds you. A place for rest and reflection after long journeys.',
        'SOLVED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3'
    },

    'b3': {
        'ZONENAME': 'Blacksmith Shop',
        'DESCRIPTION': 'A forge where weapons and armor are made.',
        'EXAMINATION': 'The blacksmith hammers away at a sword. The heat from the forge is almost unbearable.',
        'SOLVED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4'
    },

    'b4': {
        'ZONENAME': 'Outskirts',
        'DESCRIPTION': 'The outskirts of the village. Fields stretch for miles.',
        'EXAMINATION': 'The fields are peaceful and quiet, with crops swaying gently in the breeze.',
        'SOLVED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': ''
    },

    'c1': {
        'ZONENAME': 'Forest Clearing',
        'DESCRIPTION': 'A small clearing deep in the forest, with a small pond in the center.',
        'EXAMINATION': 'Wildflowers grow around the pond. You spot a few animals drinking from the water.',
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': 'd1',
        'LEFT': '',
        'RIGHT': 'c2'
    },

    'c2': {
        'ZONENAME': 'Deep Forest',
        'DESCRIPTION': 'The forest becomes darker and more ominous the further you travel.',
        'EXAMINATION': 'The trees are ancient and twisted. Strange sounds echo in the distance.',
        'SOLVED': False,
        'UP': 'b2',
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3'
    },

    'c3': {
        'ZONENAME': 'Cave Depths',
        'DESCRIPTION': 'The deeper sections of the cave, where the light from the entrance no longer reaches.',
        'EXAMINATION': 'The air is musty and cold. You can see glowing crystals embedded in the walls.',
        'SOLVED': False,
        'UP': 'b3',
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4'
    },

    'c4': {
        'ZONENAME': 'Mountain Base',
        'DESCRIPTION': 'The base of a tall mountain, its peak hidden by clouds.',
        'EXAMINATION': 'The air is thinner here, and the mountain looms high above. The path leading up is steep and treacherous.',
        'SOLVED': False,
        'UP': 'b4',
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': ''
    },

    'd1': {
        'ZONENAME': 'Mountain Trail',
        'DESCRIPTION': 'A rocky trail winding up the side of the mountain.',
        'EXAMINATION': 'Loose rocks make the path dangerous. The wind is strong, and the air is cold.',
        'SOLVED': False,
        'UP': 'c1',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'd2'
    },

    'd2': {
        'ZONENAME': 'Mountain Pass',
        'DESCRIPTION': 'A narrow pass between two towering peaks.',
        'EXAMINATION': 'The path here is narrow, with steep cliffs on either side. The wind howls loudly.',
        'SOLVED': False,
        'UP': 'c2',
        'DOWN': '',
        'LEFT': 'd1',
        'RIGHT': 'd3'
    },

    'd3': {
        'ZONENAME': 'Frozen Cave',
        'DESCRIPTION': 'A cave deep in the mountain, covered in ice and snow.',
        'EXAMINATION': 'The walls are covered in frost. The cold bites at your skin, and you see frozen stalactites hanging from the ceiling.',
        'SOLVED': False,
        'UP': 'c3',
        'DOWN': '',
        'LEFT': 'd2',
        'RIGHT': 'd4'
    },

    'd4': {
        'ZONENAME': 'Mountain Summit',
        'DESCRIPTION': 'The peak of the mountain, with a breathtaking view of the surrounding land.',
        'EXAMINATION': 'The wind is fierce at this height, but the view is unparalleled. You feel like you’re on top of the world.',
        'SOLVED': False,
        'UP': 'c4',
        'DOWN': '',
        'LEFT': 'd3',
        'RIGHT': ''
    }
}

title_sceen()