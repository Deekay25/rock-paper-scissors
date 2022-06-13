import random

player = input("Please enter player name: ")
while True:

    user_action = input('Enter a choice (rock,paper,scissors): ')
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n{player}({user_action}) : CPU({computer_action}).\n")

    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action == "rock":
        if computer_action == "paper":
            print(f"Rock smashes scissors! {player} win!")
            quit()
        else:
            print(f"Paper covers rock! {player} lose.")
            quit()
    elif user_action == "paper":
        if computer_action == "rock":
            print(f"Paper covers rock! {player} win!")
            quit()
        else:
            print(f"Scissors cuts paper! {player} lose.")
            quit()
    elif user_action == "scissors":
        if computer_action == "paper":
            print(f"Scissors cuts paper! {player} win!")
            quit()
        else:
            print(f"Rock smashes scissors! {player} lose.")
            quit()
    elif user_action != possible_actions:
        print(f"{user_action} not accepted.\nPlay again. Choose from the given words only.")
        continue
