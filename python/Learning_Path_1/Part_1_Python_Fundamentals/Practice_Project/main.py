

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
- Define simple loop of entering room, discovering treasure and ending game / restarting game core loop
- Define monster interaction 1 with item 1
- Complete the storyline with the above loops
- Complete the leaderboards logic

Object oriented programming would definitely be a better way to do this, especially with monsters, items etc...
but lets try to do a solve now without it for now before we learn it.

Do it again but with OOP afterwards, and randomly generated dungeon structures in node structures.
"""

# Define storyline along with dictionaries
"""
Storyline:

Each room you enter, depending on whether there is a monster or an item - it gives different prompts / inputs
Monsters - Vampire, Zombie, Succubus, Lich
Items - Garlic, Crossbow, Holy Water, Various Monster Loots
"""
# items
ancient_coin = {'points': 1, "dialogue": "You find an ancient coin, this could be worth something!"}
garlic = {'points': 0, "dialogue": "You find some garlic in the kitchen, its strong!"}
shotgun = {'points': 0, "dialogue": "You find a shotgun, you feel a little more American, and a little safer"}
holy_water = {'points': 0, "dialogue": "You collect some Holy Water into a vial, this could come in handy against demonic beings"}
st_paul_ash = {'points': 3, "dialogue": "You find an eery artefact, a small urn that carries the ashes of the legendary Saint Paul, the protector Saint the castle's church was built in the grace of."}

# loot (would be, subclass of items)
lucky_charm = {'points': 2, "dialogue": "The cat gives you a lucky charm! Black cats aren't bad luck!"}
vampire_robe = {'points': 2, "dialogue": "The vampire evaporates, remaining his dripped out robe"}
rotten_brain = {'points': 3, "dialogue": "The Zombie drops a half eaten, rotten brain. You take it for science, yuck."}
lich_crown = {'points': 10, "dialogue": "The lich screams and disintegrates into dust, leaving its crown behind."}

# Monsters
vampire = {"is_hostile": True, "loot": [vampire_robe], "weakness": "garlic"}
zombie = {"is_hostile": True, "loot": [rotten_brain], "weakness": "shotgun"}

monsters = [vampire]

# items

garden_entrance = {"options": ["garden hallway", "cemetary", "exit"], "dialogue": "You have entered the Garden Room"}
cemetary = {"options": ['St.Paul\'s memorial', 'garden entrance', 'exit'], "dialogue": "You have entered the Garden Room"}






# other variables / containers
opening_dl = """
You are tasked to explore a cursed castle.
The castle is rumored to be under the curse and control of a lich that has summoned various monsters.
Explore the castle, discover and collect items and artefacts and slay monsters to free the castle of the lich and its underlings.

Each room you enter may or may not have monsters, and or items that may or may not be useful in fighting certain monsters.
Monsters often carry loot that count towards your final score.
After each encounter with each room, you may choose to go to other rooms.
You may always choose to exit the dungeon alive.

So, what is your name adventurer?
    """
player = {'username': '', 'points': 0}

# Define Start Game
def start_game():
    print(f'{opening_dl}')
    player_username = input(">> ")
    player['username'] = player_username
    enter_room(garden_entrance)

# Define Game Over
def game_over(reason):


# Define enterring room


# Define Encounter
# Define item checks

# Define Loot


# Define options






