import time
import random


# Function to handle health changes
def change_health(amount):
    global health
    health += amount
    if amount < 0:
        print(
            f"You have lost health! Decreasing health by {abs(amount)}, resulting in your health decreasing to {health}.")
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


# Inventory
inventory = []


# Add item to inventory
def add_to_inventory(item):
    inventory.append(item)


# Use item from inventory
def use_item(item):
    global health
    if item == 'FIRST_AID_KIT':
        change_health(10)
        print("You used the first aid kit and regained some health.")


# Scenario 1: Finding a Weapon
def find_weapon():
    global health
    print("\nYou stumble upon an old military outpost and find a weapon. Do you take it?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        add_to_inventory('WEAPON')
    else:
        print("You chose not to take the weapon.")


# Scenario 2: Finding a First Aid Kit
def find_first_aid_kit():
    global health
    print("\nYou stumbled upon an abandoned shelter and found a first aid kit. Do you use it?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        add_to_inventory('FIRST_AID_KIT')
    else:
        print("You chose not to use the first aid kit.")


# Scenario 3: Toxic Radiation Zone
def radiation_zone():
    global health
    print("\nYou encounter a toxic radiation zone. Do you have protective gear?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-15)
    else:
        change_health(-20)


# Scenario 4: Scavenging for Supplies
def scavenging():
    global health
    print("\nYou decide to scavenge for supplies in an old warehouse. Do you search carefully?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(5)
    else:
        change_health(-5)


# Scenario 5: Firefight
def firefight():
    global health
    print("\nYou stumble upon a group of hostile survivors. A firefight ensues. Do you fight back?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-30)
    else:
        print("You chose not to engage in the firefight.")


# Scenario 6: Radioactive Animals
def radioactive_animals():
    global health
    print("\nYou encounter a pack of radioactive animals. Do you confront them?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-25)
    else:
        change_health(5)


# Scenario 7: Resting
def resting():
    global health
    print("\nYou find a safe spot to rest and relax. Do you take a break?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(15)
        print("You take a well-deserved rest and feel rejuvenated.")

        # Dream sequence
        print("\nAs you drift into sleep, memories of your recent struggles haunt your dreams.")
        print(
            "Visions of toxic radiation zones, fierce firefights, and encounters with radioactive animals flash before your eyes.")
        print("You wake up in a cold sweat, the nightmares of the wasteland still fresh in your mind.")
    else:
        print("You decide to keep moving forward.")


# Scenario 8: Abandoned Bunker
def abandoned_bunker():
    global health
    print("\nYou come across an abandoned bunker. Do you explore it?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        loot = random.choice(["ammunition", "food", "water"])
        print(f"You found a stash of {loot}. Your health remains unchanged.")
        add_to_inventory(loot.upper().replace(" ", "_"))  # Add loot to inventory
        print(
            "\nAs you search through the bunker, you are ambushed by stalkers, mutated soldiers that failed their mission to leave the zone.")
        change_health(-40)
    else:
        print("You choose not to explore the abandoned bunker.")


# Scenario 9: Acid Rain
def acid_rain():
    global health
    print("\nAcid rain begins to fall from the sky. Do you seek shelter?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        change_health(-10)
    else:
        print("You brave the acid rain and continue on your journey.")


# Scenario 10: Deserted Town
def deserted_town():
    global health
    print("\nYou stumble upon a deserted town. Do you scavenge for supplies?")
    choice = make_decision("Type Y for yes or N for no: ")
    if choice == 'Y':
        loot = random.choice(["medical supplies", "clothing", "tools"])
        print(f"You found some {loot}. Your health remains unchanged.")
        add_to_inventory(loot.upper().replace(" ", "_"))  # Add loot to inventory
    else:

