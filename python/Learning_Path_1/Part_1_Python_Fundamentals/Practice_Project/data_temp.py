
# items
ancient_coin = {"name":'ancient coin', 'points': 1, "dialogue": "You find an ancient coin, this could be worth something!"}
garlic = {"name":'garlic', 'points': 0, "dialogue": "You find some garlic in the kitchen, its strong!"}
shotgun = {"name":'shotgun','points': 0, "dialogue": "You find a shotgun, you feel a little more American, and a little safer"}
holy_water = {"name":'holy water','points': 0, "dialogue": "You collect some Holy Water into a vial, this could come in handy against demonic beings"}
st_paul_ash = {"name":'St. Paul\'s Ashes', 'points': 3, "dialogue": "You find an eery artefact, a small urn that carries the ashes of the legendary Saint Paul, the protector Saint the castle's church was built in the grace of."}

# loot (would be, subclass of items)
lucky_charm = {"name":'lucky charm', 'points': 2, "dialogue": "The cat gives you a lucky charm! Black cats aren't bad luck!"}
vampire_robe = {"name":'vampire robe','points': 2, "dialogue": "The vampire is slain, but its fire drip is not, you "}
rotten_brain = {"name":'rotten brain', 'points': 3, "dialogue": "The Zombie drops a half eaten, rotten brain. You take it for the sake science, yuck."}
lich_crown = {"name":'Lich Crown', 'points': 10, "dialogue": "The lich screams and disintegrates into dust, leaving its crown behind."}


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

# Rooms
garden_entrance = {"visited": True, "options": ["grand hallway", "cemetary"], "item": [], 
"dialogue": "You have entered the Garden Entrance of the castle. You feel a slight sense of doubt about all this...",
"monster": None,
}

cemetary = {"visited": False, "options": ['St.Paul\'s memorial', 'garden entrance'], "item": [ancient_coin],
"dialogue": "You have entered the Cemetary, something feels off.",
"monster": zombie,
}

st_pauls = {"visited": False, "options": ['cemetary'],  "item": [st_paul_ash],
"monster": None,
"dialogue": "You have entered St Paul's memorial, "}

grand_hallway = {"visited": False, "options": ['Kitchen', 'garden entrance', 'church'], "item": [],
"monster": None,
 "dialogue": "You have entered the  Grand Hallway"}

church = {"visited": False, "options": ['Kitchen', 'garden entrance', 'church'],
"monster": vampire,
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
loss_dl = 'You have been defeated. Well done player. Try again...'
win_dl = "You have slain the Lich and freed the Castle of its conjuring, you are now the new lord of the castle and live happily ever after. Triumph! \n+5 points!"
quit_dl = "You have decided to leave the castle and chose to live instead of exploring further.\nTo be alive, is indeed worth something. \n+1 points!"
replay_dl = "The game is now over, would you like to play again? Type Y/N (case insensitive)"
