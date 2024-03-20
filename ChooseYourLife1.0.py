# Programmer: Marcus Campos-Jones
# Date: 3.15.2024
# Program: Choose Your Life

# Print initial mission information
# Function to handle health changes
import time

# Global variable to track player's health
health = 25

# Function to handle health changes
import time  # Importing the time module for adding delays

# Global variable to track player's health
health = 25

# Function to handle health changes
def change_health(amount):
    global health
    health += amount
    if amount < 0:
        print(f"You have lost health! Decreasing health by {abs(amount)}, resulting in your health decreasing to {health}.")
    else:
        print(f"Your health increased by {amount}, resulting in your health level increasing to {health}.")

# Function to handle decision prompts
def make_decision(prompt):
    while True:
        decision = input(prompt).upper()
        if decision == 'Y' or decision == 'N':
            return decision
        else:
            print("Invalid input. Please enter Y or N.")

# Apple Tree scenario
def apple_tree():
    global health
    print("\nYou see an apple tree! You are starving. Do you eat the apple?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-2)  # Decreasing health if apple is eaten
    else:
        print("Great choice! You decide not to eat the bad apple.")

# Fork scenario
def fork_in_trail():
    global health
    print("\nYou come to a fork in the trail. You must decide if you go left or right.")
    choice = make_decision("Type Y for left or N for right: ")
    if choice == 'Y':
        change_health(-5)  # Decreasing health if left path is chosen
    else:
        change_health(2)  # Increasing health if right path is chosen

# Cave scenario
def cave():
    global health
    print("\nYou've reached a cave. Now, the choice is yours: enter or not.")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-2)  # Decreasing health if entered
    else:
        change_health(5)  # Increasing health if not entered

# River scenario
def river():
    global health
    print("\nYou have reached a river. Now, you must decide whether to enter or not.")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(5)  # Increasing health if entered
    else:
        change_health(-2)  # Decreasing health if not entered

# House scenario
def house():
    global health
    print("\nYou have reached a house. Now, you must decide whether to enter or not.")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-2)  # Decreasing health if entered
    else:
        change_health(5)  # Increasing health if not entered

# Campfire scenario
def campfire():
    global health
    print("\nYou have reached a campfire. You must decide if you sit next to it or not.")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(2)  # Increasing health if sitting by the campfire
        print("You decide to sleep by the campfire for the night.")
    else:
        change_health(-5)  # Decreasing health if not sitting by the campfire

# Awake scenario
def awake():
    global health
    print("\nYou awaken next to the campfire. Do you put more wood on the fire?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-2)  # Decreasing health if putting more wood
    else:
        change_health(5)  # Increasing health if not putting more wood

# Forest scenario
def forest():
    global health
    print("\nYou have walked away from the campfire. Do you go left or right?")
    choice = make_decision("Type Y for left or N for right: ")
    if choice == 'Y':
        change_health(-2)  # Decreasing health if going left
    else:
        change_health(-2)  # Decreasing health if going right

# Sword scenario
def sword():
    global health
    print("\nYou stand before a sword embedded in a stone wall. Will you claim it?")
    choice = make_decision("Type Y to claim the sword or N to walk away: ")
    if choice == 'Y':
        change_health(5)  # Increasing health if claiming the sword
        print("Your health increases by 5 points.")
    else:
        print("You decide to leave the sword untouched.")

# Main game loop
if __name__ == "__main__":
    print("Our mission is to get out of the woods!")
    print("Make a wrong turn or choice and you could be in a fight for your life")

    scenarios = [apple_tree, fork_in_trail, cave, river, house, campfire, awake, forest, sword]

    for scenario in scenarios:
        if health > 0:
            scenario()
            time.sleep(2)  # Add a delay of 2 seconds between each scenario
        else:
            print("You have died. You never escaped the forest!")
            break

    # Ending
    print("\nYou awaken abruptly, heart pounding.")
    print("The remnants of a chilling nightmare linger in your mind.")
    print("The eerie whispers of the forest envelop you.")
    print("Invisible watchers, their presence palpable, beckon from the shadows.")
    print("Behind you, only an abyss of darkness; then, a bone-chilling voice: 'Gotcha.'")
    if health > 0:
        if health > 15:
            print("\nBut as you gather your strength and resolve, you realize it was all a test.")
            print("You've overcome the challenges of the forest, emerging victorious and alive.")
            print("You made it out of the woods!")
            print("Congratulations! You've won the game.")
        else:
            print("\nOverwhelmed by the horrors of the forest, you succumb to darkness.")
            print("Your heart races faster until it can no longer bear the terror.")
            print("In the end, the forest claims another victim.")
            print("Game over. You have perished in the depths of the woods.")
            print("Subject 72, status: deceased. Location: Forever lost. Time: Unknown.")
    else:
        print("\nGame over. Subject 72, status: awake. Location: Bravo Site-34. Time: 13:50.")

