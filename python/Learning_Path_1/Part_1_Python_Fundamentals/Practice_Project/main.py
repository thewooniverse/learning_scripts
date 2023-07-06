# pylint: disable=line-too-long
## import strings
import sys
from items_monsters import *

"""
Specifications
- At least 3 different rooms to be explored
- Concept of inventory and items and conditional outcome based on whether player has the item or not
- If you do not have an item when encountering a monster
- This version will have a specific "solve" to kill all monsters and follows a on-rails storyline.
- Treasure Score at the end of the game
- Leaderboard text / sorting (leaderboard module from other files), creates temporary player profile files 

To Dos:
Next
- organize files for configs / room settings with File IO
- complete the storyline
- complete the leaderboard logic with File IO

Future features
- Add wait times
- Add probabilities / fighting mechanics vs monsters

- Gameplay history for each player and session / path log and error logs optionally
- refactoring with OOP?


Object oriented programming would definitely be a better way to do this, especially with monsters, items etc...
but lets try to do a solve now without it for now before we learn it.
Do it again but with OOP afterwards, and randomly generated dungeon structures in node structures.
"""


player = {'username': '', 'points': 0, 'inventory': [], "rooms_visited":[]}


##### Define core loops #####

# create temp files / player profiles
# copy config file


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
    # handle each type of reason, dialogue + points
    print("\n\n-----Game Over-----\n\n")

    if reason == "loss":
        # print lost dialogue
        print(loss_dl)

    elif reason == "win":
        # print win dialogue
        print(win_dl)
        player['points'] += 5
    
    elif reason == "quit":
        # print quit dialogue
        print(quit_dl)
        player['points'] += 1
    
    # summarize points and add it to the leaderboard
    inventory_points = inventory_point_calculation()
    player['points'] += inventory_points

    print(f'Your final points tally to {player["points"]}\n')

    # print the new leaderboard and your position
    print(f"Player Name: {player['username']} \nPlayer Score: {player['points']}\n")

    # remove the temp files and clean up before play_again() exits the script

    # call play again
    play_again()

    # ask user if they want to play again?



# Define Play again?
def play_again():
    # yes - reset temporary files
    print(replay_dl)
    user_input = input(">> ")

    while len(user_input) != 1:
        print("\nThis is not a valid input.")
        play_again()

    accepted_response = ['y', 'n', 'Y', 'N']

    if user_input in accepted_response:
        if user_input == "y" or user_input == "Y":
            print("\n\n\n\n\n\n\n\n\n")
            start_game()
        else:
            print("\nThanks for playing!")
            sys.exit()
    else:
        print('This is not a valid input')
        play_again()

    



##### Leaderboard logics #####
# define point calculation
def inventory_point_calculation():

    print("-----Point Calculation-----")
    
    total_points = 0
    # goes through the player's list of items
    for item in player['inventory']:
        # print point calculations
        print(f"{item['name']} is worth {item['points']} points!")
        # sum up the points
        total_points += item['points']
    print(f"From your adventure, your loot and items are worth {total_points}. Well done adventurer!")
    return(total_points)

# define add to the leaderboard and display




##### Core gameplay functions #####
# Define enterring room
def enter_room(room):
    print(room['dialogue'])
    ## if not previously entered, proceed with encounter and then loot, then next step options
    if room['visited'] == False:
        # encounter to check monsters
        if room['monster']:
            encounter(room['monster'])
        # collect remaining items
        if room['item'] != []:
            for item in room['item']:
                player['inventory'].append(item)
                print(item['dialogue'])

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
        for loot in monster['loot']:
            player['inventory'].append(loot)
        looted = monster['loot'][0]
        print(looted['dialogue'])
        
    ## no - lose dialogue and game over
    else:
        print(monster['dialogue_loss'])
        game_over("loss")

# Define choose room function
def choose_from(room):
    # display options
    print("\nYou decide where you want to go to next...\n")
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

# inventory check function
def inventory_check():
    print('------Inventory------')
    for item in player['inventory']:
        print("-- "+item['name'])
    print('---------------------')

##### START GAME #####

start_game()