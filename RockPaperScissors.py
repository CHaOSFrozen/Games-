# Imports Random Module
import random

# Ask user for input 
user_input = input("Enter a choice from rock, paper and scissors: ")
actions = ["rock", "paper", "scissors"]
# Randomises the action by the AI
AI_action = random.choice(possible_actions)
# Prints the User Input and AI Input
print(f"\nYou chose {user_input}, AI choses {AI_action}.\n")


# 3 Possible Answers for User Input 

if user_input == AI_action:
    print(f"Both players selected {user_input}. It's a tie!")
elif user_input == "rock":
    if AI_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "paper":
    if AI_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "scissors":
    if AI_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
