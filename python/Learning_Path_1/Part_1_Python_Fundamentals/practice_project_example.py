print(', '.join([r for r in ["grand hallway", "cemetary", "exit"]]))
print(len(["grand hallway", "cemetary", "exit"]))
for n in range(len(["grand hallway", "cemetary", "exit"])):
    print(n)


def start_game():
    print("You are in a dark room in an old castle. In front of you are two doors. Choose one (1 or 2):")

    player_choice = input("> ")
    if player_choice == "1":
        game_over("You enter a room full of treasures. You're rich!")
    elif player_choice == "2":
        game_over("You enter a room full of traps. Game Over!")
    else:
        game_over("You didn't follow the game rules. Game Over!")

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()

def play_again():
    print("\nDo you want to play again? (yes or no)")

    # convert the player's input to lower_case
    player_choice = input("> ").lower()

    if "yes" in player_choice:
        start_game()
    else:
        print("Bye!")

start_game()

