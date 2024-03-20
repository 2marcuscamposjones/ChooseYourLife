# Programmer: Marcus Campos-Jones
# Date: 3.15.2024
# Program: Choose Your Life

# Print initial mission information
print("Our mission is to get out of the woods!")
print("Make a wrong turn or choice and you could be in a fight for your life")

# Initialize player's health and health modifiers
health = 25
dcrsHlthMjr = 5  # Major health decrease
dcrsHlthMnr = 2  # Minor health decrease
incrsHkthMJr = 5  # Major health increase
incrsHkthMnr = 2  # Minor health increase

# Apple Tree
if health > 0:
    print("\nYou have just walked into the woods and you have a health level of", health)
    print("You see an apple tree! You are starving. Do you eat the apple?")
    apple = input("Type Y for yes or N for no: ").upper()
    if apple == "Y":
        health -= dcrsHlthMnr
        print("You ate the apple, but it was bad. You have lost health!")
        print("Your health decreased by", dcrsHlthMnr, "resulting in your health decreasing to", health)
    else:
        print("Great choice! You decide not to eat the bad apple.")
        print("Your health remains at", health)
else:
    print("You have died. You never escaped the forest!")

# Fork
if health > 0:
    print("\nYou come to a fork in the trail. You must decide if you go left or right.")
    print("A crucial decision lies ahead. Make sure you make the right choice!")
    fork = input("Type Y for left or N for right: ").upper()
    if fork == "Y":
        health -= dcrsHlthMjr
        print("You chose the wrong path and ran into a rattlesnake. It bites you.")
        print("You have lost health! Decreasing health by", dcrsHlthMjr, "resulting in your")
        print("health decreasing to", health, ".")
    else:
        health += incrsHkthMnr
        print("You chose the right path and found a nice pumpkin, increasing your")
        print("health by", incrsHkthMnr, "resulting in your health level increasing to", health)
else:
    print("You have died. You never escaped the forest!")

# Cave
if health > 0:
    print("\nYou've reached a cave. Now, the choice is yours: enter or not.")
    print("A crucial decision lies ahead. Choose wisely!")
    cave = input("Type Y for yes or N for no: ").upper()
    if cave == "Y":
        health -= dcrsHlthMnr
        print("You've chosen the wrong path; you've fallen into a hole.")
        print("You've lost health! Decreasing health by", dcrsHlthMnr, "resulting in")
        print("your health decreasing to", health, ".")
    else:
        health += incrsHkthMJr
        print("You've chosen the right path; you've found a medkit, increasing your")
        print("health by", incrsHkthMJr, "resulting in your health level increasing to", health)
else:
    print("You have died. You never escaped the forest!")

# River
if health > 0:
    print("\nYou have reached a river. Now, you must decide whether to enter or not.")
    print("A significant decision lies ahead. Make sure you make the right choice!")
    river = input("Type Y for yes or N for no: ").upper()
    if river == "Y":
        health += incrsHkthMJr
        print("You chose the right path; the water heals you.")
        print("Health increased by", incrsHkthMJr, "resulting in your health level increasing to", health)
    else:
        health -= dcrsHlthMnr
        print("You chose not to get in the water and trip, hurting yourself.")
        print("You have lost health! Decreasing health by", dcrsHlthMnr, "resulting in your")
        print("health decreasing to", health, ".")
else:
    print("You have died. You never escaped the forest!")

# House
if health > 0:
    print("\nYou have reached a house. Now, you must decide whether to enter or not.")
    print("A significant decision lies ahead. Make sure you make the right choice!")
    house = input("Type Y for yes or N for no: ").upper()
    if house == "Y":
        health -= dcrsHlthMnr
        print("You chose the wrong path and are attacked.")
        print("You have lost health! Decreasing health by", dcrsHlthMnr, "resulting in your")
        print("health decreasing to", health, ".")
    else:
        health += incrsHkthMJr
        print("You chose the right path; the old lady gives you cookies, increasing your")
        print("health by", incrsHkthMJr, "resulting in your health level increasing to", health)
else:
    print("You have died. You never escaped the forest!")

# Campfire
if health > 0:
    print("\nYou have reached a campfire. You must decide if you sit next to it or not.")
    print("Big decision, make sure you make the right choice!")
    campfire = input("Type Y for yes or N for no: ").upper()
    if campfire == "Y":
        health += incrsHkthMnr
        print("You chose the right option; you are warm.")
        print("You have gained health by", incrsHkthMnr, "resulting in your health level increasing to", health)
        print("You decide to sleep by the campfire for the night.")
    else:
        health -= dcrsHlthMjr
        print("You chose the wrong option; you freeze.")
        print("You have lost health! Decreasing health by", dcrsHlthMjr, "resulting in your")
        print("health decreasing to", health, ".")
else:
    print("You have died. You never escaped the forest!")

# Awake
if health > 0:
    print("\nYou awaken next to the campfire. Do you put more wood on the fire?")
    print("Big decision, make sure you make the right choice!")
    awake = input("Type Y for yes or N for no: ").upper()
    if awake == "Y":
        health -= dcrsHlthMnr
        print("You chose the wrong option; you can't lift the wood.")
        print("You have lost health! Decreasing health by", dcrsHlthMnr, "resulting in your health level decreasing to", health)
    else:
        health += incrsHkthMJr
        print("You chose the right option; you choose to watch the fire die out.")
        print("You have gained health by", incrsHkthMJr, "resulting in your health level increasing to", health)
else:
    print("You have died. You never escaped the forest!")

# Forest
if health > 0:
    print("\nYou have walked away from the campfire. Do you go left or right?")
    print("Big decision, make sure you make the right choice!")
    forest = input("Type Y for left or N for right: ").upper()
    if forest == "Y":
        health -= dcrsHlthMnr
        print("You chose the wrong path; you fall down the hill.")
        print("You have lost health! Decreasing health by", dcrsHlthMnr, "resulting in your")
        print("health decreasing to", health, ".")
    else:
        health -= dcrsHlthMnr
        print("You chose wrong; you fall down after seeing something shiny on the ground.")
        print("You have lost health! Decreasing health by", dcrsHlthMnr, "resulting in your")
        print("health decreasing to", health, ".")
else:
    print("You have died. You never escaped the forest!")

# Sword
if health > 0:
    print("\nYou stand before a sword embedded in a stone wall. Will you claim it?")
    print("A weighty decision lies before you. Choose wisely!")
    sword = input("Type Y to claim the sword or N to walk away: ").upper()
    if sword == "Y":
        health += incrsHkthMJr
        print("Struggling against resistance, you grasp the sword, feeling a surge of determination.")
        print("You made the right choice.")
        print("Your health increases by", incrsHkthMJr, "points, bringing your total to", health)
    else:
        print("You decide to leave the sword untouched, wary of its unknown power.")
else:
    print("You have perished, trapped forever in the forest's grasp!")

# Dream
if health > 0:
    print("\nYou awaken abruptly, heart pounding.")
    print("The remnants of a chilling nightmare linger in your mind.")
    print("The eerie whispers of the forest envelop you.")
    print("Invisible watchers, their presence palpable, beckon from the shadows.")
    print("Behind you, only an abyss of darkness; then, a bone-chilling voice: 'Gotcha.'")

    # Good ending
    if health > 15:
        print("\nBut as you gather your strength and resolve, you realize it was all a test.")
        print("You've overcome the challenges of the forest, emerging victorious and alive.")
        print("You made it out of the woods!")
        print("Congratulations! You've won the game.")
    # Bad ending
    else:
        print("\nOverwhelmed by the horrors of the forest, you succumb to darkness.")
        print("Your heart races faster until it can no longer bear the terror.")
        print("In the end, the forest claims another victim.")
        print("Game over. You have perished in the depths of the woods.")
        print("Subject 72, status: deceased. Location: Forever lost. Time: Unknown.")
else:
    print("\nYou awaken abruptly, heart pounding.")
    print("The remnants of a chilling nightmare linger in your mind.")
    print("The eerie whispers of the forest envelop you.")
    print("Invisible watchers, their presence palpable, beckon from the shadows.")
    print("Behind you, only an abyss of darkness; then, a bone-chilling voice: 'Gotcha.'")
    print("\nGame over. Subject 72, status: awake. Location: Bravo Site-34. Time: 13:50.")
