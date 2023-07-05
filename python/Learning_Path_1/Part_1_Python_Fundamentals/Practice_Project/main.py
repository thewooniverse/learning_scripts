# pylint: disable=line-too-long
## import strings
import sys

"""
Specifications
- At least 3 different rooms to be explored
- Concept of inventory and items and conditional outcome based on whether player has the item or not
- If you do not have an item when encountering a monster
- This version will have a specific "solve" to kill all monsters and follows a on-rails storyline.
- Treasure Score at the end of the game
- Leaderboard text / sorting (leaderboard module from other files), creates temporary player profile files 
-- and creates leaderboard

To Dos:
- Complete the storyline with the above loops
- Complete the leaderboards logic
- Add a feature for checking player inventory when prompted for action
- Add wait times

- Play again feature w/o restarting script:
-- temp files and configuration files for session and automatic deletion of those session files.

Object oriented programming would definitely be a better way to do this, especially with monsters, items etc...
but lets try to do a solve now without it for now before we learn it.

Do it again but with OOP afterwards, and randomly generated dungeon structures in node structures.
"""
# define objects (to be migrated)

# items
ancient_coin = {'points': 1, "dialogue": "You find an ancient coin, this could be worth something!"}
garlic = {'points': 0, "dialogue": "You find some garlic in the kitchen, its strong!"}
shotgun = {'points': 0, "dialogue": "You find a shotgun, you feel a little more American, and a little safer"}
holy_water = {'points': 0, "dialogue": "You collect some Holy Water into a vial, this could come in handy against demonic beings"}
st_paul_ash = {'points': 3, "dialogue": "You find an eery artefact, a small urn that carries the ashes of the legendary Saint Paul, the protector Saint the castle's church was built in the grace of."}

# loot (would be, subclass of items)
lucky_charm = {'points': 2, "dialogue": "The cat gives you a lucky charm! Black cats aren't bad luck!"}
vampire_robe = {'points': 2, "dialogue": "The vampire is slain, but its fire drip is not, you "}
rotten_brain = {'points': 3, "dialogue": "The Zombie drops a half eaten, rotten brain. You take it for the sake science, yuck."}
lich_crown = {'points': 10, "dialogue": "The lich screams and disintegrates into dust, leaving its crown behind."}

# Monsters
vampire = {"is_hostile": True, "loot": [vampire_robe], "weakness": garlic,
"dialogue": "You notice a Vampire, sucking away at the neck of a seemingly freshly killed goat",
"dialogue_win": "You throw your Garlic at the vampire, and while it repulsively pukes you take the chance of his weakness to strike the back of its head and kill it.",
"dialogue_loss": "You try to fight the vampire, however its strengths overpower you. As it sinks its teeth into your throat and your consciousness fades, you regret that you did not have anything to weaken its powers."
}
zombie = {"is_hostile": True, "loot": [rotten_brain], "weakness": shotgun,
"dialogue": "You notice a zombie, digging away at what seems to be the remains of a wild deer",
"dialogue_win": "As the zombie begins walking towards you, you instinctly shoot your shotgun as its head as commonly done in movies.",
"dialogue_loss": "You try to fend off the zombie, however, you are simply unable to overpower it. If only you had a ranged weapon..."
}


monsters = [vampire]

# items

garden_entrance = {"visited": True, "options": ["grand hallway", "cemetary"], "item": [], 
"dialogue": "You have entered the Garden Entrance of the castle. You feel a slight sense of doubt about all this...",
"monster": None,
}
cemetary = {"visited": False, "options": ['St.Paul\'s memorial', 'garden entrance'], "item": [ancient_coin],
"dialogue": "You have entered the Cemetary, something feels off.",
"monster": zombie,
}

st_pauls = {"visited": False, "options": ['cemetary'],  "item": [],
"dialogue": "You have entered St Paul's memorial, "}

grand_hallway = {"visited": False, "options": ['Kitchen', 'garden entrance', 'church'], "item": [],
"monster": None,
 "dialogue": "You have entered the  Grand Hallway"}

church = {"visited": False, "options": ['Kitchen', 'garden entrance', 'church'],
"dialogue": "You have entered the Garden Room"}

names_of_rooms = {'St.Paul\'s memorial': st_pauls, "garden entrance": garden_entrance, "cemetary": cemetary,
"grand hallway": grand_hallway, "church": church}


# other variables / containers
opening_dl = """You are tasked to explore a cursed castle.
The castle is rumored to be under the curse and control of a lich that has summoned various monsters.
Explore the castle, discover and collect items and artefacts and slay monsters to free the castle of the lich and its underlings.

Each room you enter may or may not have monsters, and or items that may or may not be useful in fighting certain monsters.
Monsters often carry loot that count towards your final score.
After each encounter with each room, you may choose to go to other rooms.
You may always choose to exit the dungeon alive.

So, what is your name adventurer?"""

player = {'username': '', 'points': 0, 'inventory': [shotgun], "rooms_visited":[]}

# Define Start Game
def start_game():
    # opening dialogue / interaction to set up user
    print(opening_dl)
    player_username = input(">> ")
    player['username'] = player_username
    print(f"\nWelcome to the beginning of your adventure, {player['username']}!")
    
    # begin the game
    enter_room(garden_entrance)

# Define Game Over
def game_over(reason):
    sys.exit()

    # ask user if they want to play again?

# Define Game Over
def play_again():
    pass

# Define enterring room
def enter_room(room):
    print(room['dialogue'])
    ## if not previously entered, proceed with encounter and then loot, then next step options
    if room['visited'] == False:
        # encounter to check monsters
        if room['monster']:
            encounter(room['monster'])
        # collect remaining items
        player['inventory'].append(room['item'])

        # change room state to visited and display next step options
        room['visited'] = True # needs to later be changed to player configs or temp files
        choose_from(room)

    # check if the room has been entered
    ## if yes, proceed to action options for next steps
    elif room['visited']:
        choose_from(room)


# Define Encounter monster
def encounter(monster):
    print(monster['dialogue'])
    # check item
    ## yes - win dialogue and loot the enemy
    if monster['weakness'] in player['inventory']:
        print(monster['dialogue_win'])
        player['inventory'].append(monster['loot'])
        looted = monster['loot'][0]
        print(looted['dialogue'])
        
    ## no - lose dialogue and game over
    else:
        print(monster['dialogue_loss'])
        game_over("loss")


# Define choose room
def choose_from(room):
    # display options
    print("You decide where you want to go to next...\n")
    # give user input prompts for the options
    path_options = []
    for n in range(len(room['options'])):
        print(f"{n+1}. {room['options'][n]}, type {n+1}")
        path_options.append(f"{n+1}. {room['options'][n]}, type {n+1}")
    print("I. To check inventory, type i.\nX. To give up, type x.")
    path_options.append("I. To check inventory, type i.\nX. To give up, type x.")

    # collect user input with error handling
    accepted_inputs = ['i', 'x'] + [n+1 for n in range(len(room['options']))]
    user_input = input(">> ")
    # handle different data types with try / excepts
    while len(user_input) != 1:
        print(f"\nThis is not a valid input, please select from the options again:")
        print('\n'.join(path_options))
        user_input = input(">> ")
    
    # check if its a valid number
    if user_input.isdigit():
        if int(user_input) in accepted_inputs:
            enter_room(names_of_rooms[room['options'][int(user_input)-1]])
        else:
            choose_from(room)
    
    elif user_input.isalpha():
        if user_input.lower() == "i":
            inventory_check()
            choose_from(room)
        elif user_input.lower() == "x":
            game_over("quit")
        else:
            choose_from(room)
    else:
        choose_from(room)



def inventory_check():
    pass



start_game()