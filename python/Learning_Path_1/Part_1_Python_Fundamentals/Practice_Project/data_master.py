
# items
ancient_coin = {"name":'ancient coin', 'points': 1, "dialogue": "You find an ancient coin, this could be worth something!"}
garlic = {"name":'garlic', 'points': 1, "dialogue": "You find some garlic in the kitchen, its strong!"}
shotgun = {"name":'shotgun','points': 1, "dialogue": "You find a shotgun, you feel a little more American, and a little safer"}
holy_water = {"name":'holy water','points': 1, "dialogue": "You collect some Holy Water into a vial, this could come in handy against demonic beings"}
st_paul_ash = {"name":'St. Paul\'s Ashes', 'points': 5, "dialogue": "You find an eery artefact, a small urn that carries the ashes of the legendary Saint Paul, the protector Saint the castle's church was built in the grace of."}




# loot (would be, subclass of items)
# lucky_charm = {"name":'lucky charm', 'points': 3, "dialogue": "The cat gives you a lucky charm! Black cats aren't bad luck!"}
rotten_brain = {"name":'rotten brain', 'points': 3, "dialogue": "The Zombie drops a half eaten, rotten brain. You take it for the sake science, yuck."}
vampire_robe = {"name":'vampire robe','points': 3, "dialogue": "The vampire is slain, but its fire drip is not, you pick up its velvet robe."}
torture_whip = {"name":'Torture Whip', 'points': 3, "dialogue": "As the succubus disintegrates back into hell, its leaves behind its torturous and lustful whip. \nI wonder what she would have done to me with these...."}
lich_crown = {"name":'Lich Crown', 'points': 10, "dialogue": "The lich screams and disintegrates into dust, leaving its crown behind. You dare not wear it...."}



# Monsters
zombie = {"is_hostile": True, "loot": [rotten_brain], "weakness": shotgun,
"dialogue": "You notice a zombie, digging away at what seems to be the remains of a wild deer",
"dialogue_win": "As the zombie begins walking towards you, you instinctly shoot your shotgun as its head as commonly done in movies.",
"dialogue_loss": "You try to fend off the zombie, however, you are simply unable to overpower it. If only you had a ranged weapon..."
}
succubus = {"is_hostile": True, "loot": [torture_whip], "weakness": holy_water,
"dialogue": "You notice a Succubus, as it notices you back it murmurs demonic words of promiscuity.",
"dialogue_win": "As you begin to lose control over your own consciousness, you remember the holy water in your backpack, you throw it onto the Succubus. \nShe begins screaming and disintegrating... Good riddance.",
"dialogue_loss": "She approaches and overpowers you. You have lost consciousness and control, you are now a servant of her promiscuous femdom."
}

vampire = {"is_hostile": True, "loot": [vampire_robe], "weakness": garlic,
"dialogue": "You notice a Vampire, sucking away at the neck of a seemingly freshly killed goat",
"dialogue_win": "You throw your Garlic at the vampire, and while it repulsively pukes you take the chance of his weakness to strike the back of its head and killing it.",
"dialogue_loss": "You try to fight the vampire, however its strengths overpower you. As it sinks its teeth into your throat and your consciousness fades, you regret that you did not have anything to weaken its powers."
}

lich = {"is_hostile": True, "loot": [lich_crown], "weakness": st_paul_ash,
"dialogue": "Lich. This must be the final boss. Whether you are or are not ready for this, you must fight.",
"dialogue_win": "You try everything in your arsenal, however nothing seems to work. The lich is simply too powerful. As it begins to cast its spell unto you, the ashes of Saint Paul bursts into flames and the Protector Saint Paul manifests himself. Banishing the creature once and for all to the depths of hell.",
"dialogue_loss": "You try everything in your arsenal, however nothing seems to work. The being is simply outside of the bounds of mortal strength. It casts its spell unto you, making you into an obidient deathly knight."
}





# Rooms
garden_entrance = { "options": ["grand hallway", "cemetary", 'fountain'], "item": [],
"dialogue": "You have entered the Garden Entrance of the castle. You feel a slight sense of doubt about all this...",
"monster": None,
}

fountain = { "options": ['garden entrance'], "item": [holy_water],
"dialogue": "You have entered the fountain, there is a flowing well of holy water. The only thing that feels undamned in this place.",
"monster": None,
}

cemetary = { "options": ['garden entrance', 'St.Paul\'s memorial'], "item": [ancient_coin],
"dialogue": "You have entered the Cemetary, something feels off.",
"monster": zombie,
}

st_pauls = {"options": ['cemetary'],  "item": [st_paul_ash],
"monster": None,
"dialogue": "You have entered St Paul's memorial, where lies the remains of Saint Paul."}

grand_hallway = {"options": ['garden entrance', 'kitchen', 'church'], "item": [],
"monster": None,
"dialogue": "You have entered the  Grand Hallway, where to go from here...?"}

kitchen = {"options": ['grand hallway', 'armory'], "item": [garlic],
"monster": None,
"dialogue": "You have entered the Kitchen... It smells foul."}
armory = {"options": ['kitchen'], "item": [shotgun],
"monster": None,
"dialogue": "You have entered the Kitchen... It smells foul."}

church = {"options": ['grand hallway', 'crypt'], "item": [],
"monster": succubus,
"dialogue": "You have have entered the Church, this place no longer feels holy..."}

crypt = {"options": ['church', 'library'], "item": [],
"monster": vampire,
"dialogue": "You have entered the crypt... It smells like fresh blood, shouldn't this place be for dead bodies only?"}

library = {"options": ['crypt', 'Archibishop\'s room'], "item": [ancient_coin],
"monster": None,
"dialogue": "You climb up the stairs to reach what seems to be a library at the atop the Tower..."}

archbishops_room = {"options": ['library'], "item": [],
"monster": lich,
"dialogue": "You enter the Archbishop's room... this must be the end of it."}



names_of_rooms = {'St.Paul\'s memorial': st_pauls, "garden entrance": garden_entrance, "cemetary": cemetary,
"grand hallway": grand_hallway, "church": church, "fountain": fountain, 'kitchen': kitchen, "armory": armory,
'Archibishop\'s room': archbishops_room, 'crypt':crypt, 'library':library}









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
