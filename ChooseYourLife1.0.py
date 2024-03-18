# Programmer: Marcus Campos-Jones
# Date: 3.15.2024
# Program: Choose your Life

# Print initial mission information
print("Our mission is to get out of the woods!.")
print("Make a wrong turn or choice and you could be in a fight for your life")

# Initialize player's health and health modifiers
health = 25
dcrsHlthMjr = 5  # Major health decrease
dcrsHlthMnr = 2  # Minor health decrease
incrsHkthMJr = 5  # Major health increase
incrsHkthMnr = 2  # Minor health increase
# Apple Tree
# Programmer: Marcus Campos-Jones

if health > 0:
    print("\nYou have just walked into the wood and you have a health level of.")
    print(health,"and see an apple tree! You are starving. do you eat the apple?")
    apple = input("Type a Y for yes or N for no ").upper()
    if apple == "Y":
      health = health - dcrsHlthMnr
      print("You ate the apple a bad apple you have lost health!")
      print("Your health by ",dcrsHlthMnr,"resulting in my heath levels")
      print("decreasing to",health)
    else:
      print("Great choise,you decide to not eat the bad apple.")
      print("Your health remains at",health)
else:
    print("You have died, you never escaped the forest!")
# fork
# programmer: Marcus Campos-Jones
if health > 0:
    print("\nYou come to a fork in the trail, you must decide if you go left or right.")
    print("Big decicion, make sure you make the right choise!")
    fork = input("Type a Y for left or N for right ").upper()
    if fork == "Y":
      health = health - dcrsHlthMjr
      print("You chose the wrong path, you ran into a rattlesnake. It bites you")
      print("You have lost health! decreasing heath by",dcrsHlthMjr,"resulting in your")
      print("deacresing to", str(health) + ".")
    else:
      health = health + incrsHkthMnr
      print("You chose the right path, you found a nice pumpkin incresing your")
      print("health by",incrsHkthMnr,"resulting in your heath levels icreasing ")
      print("to",health)
else:
  print("You have died, you never escaped the forest!")
# Cave
# Programmer: Marcus Campos-Jones
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
  print("You have died, you never escaped the forest!")
# river
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
# house
# Programmer: Marcus Campos-Jones
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
# campfire
if health > 0:
  print("\nYou have reached a campfire, you must decide if you sit next to it or not.")
  print("Big decicion, make sure you make the right choise!")
  campfire = input("Type a Y for yes or N for no ").upper()
  if campfire == "Y":
    health = health + incrsHkthMnr
    print("You chose the right option, you are warm.")
    print("You have gained health by",incrsHkthMnr,"resulting in your heath levels ")
    print("increasing to",health)
    print("You decide to sleep in the campfire for the night.")
  else:
    health = health - dcrsHlthMjr
    print("You chose the wrong option you freeze.")
    print("You have lost health! decreasing heath by",dcrsHlthMjr,"resulting in your")
    print("decreasing to", str(health) + ".")
else:
  print("You have died, you never escaped the forest!")
# awake
if health > 0:
  print(" \nyou awake next to the campfire,do you put more wood on the fire?")
  print("Big decicion, make sure you make the right choise!")
  awake = input("Type a Y for yes or N for no ").upper()
  if awake == "Y":
    health = health - dcrsHlthMnr
    print("You chose the wrong option,you cant lift the wood.")
    print("You have gained health by",dcrsHlthMnr,"resulting in your heath levels ")
    print("increasing to",health)
  else:
    health = health + incrsHkthMJr
    print("You chose the right option, you choose to watch the fire die out.")
    print("You have gained health by",incrsHkthMJr,"resulting in your heath levels ")
    print("increasing to",health)
else:
  print("You have died, you never escaped the forest!")
# forest
if health > 0:
  print("\nYou have walked away from the campfire. do you go left or right?")
  print("Big decicion, make sure you make the right choise!")
  forest = input("Type a Y for left or N for right ").upper()
  if forest == "Y":
    health = health - dcrsHlthMnr
    print("You chose the wrong path, you fall down the hill.")
    print("You have lost health! decreeasing heath by",dcrsHlthMnr,"resulting in your")
    print("deacresing to", str(health) + ".")
  else:
    heath = health - dcrsHlthMnr
    print("You chose wrong, you fall down after seeing something shiny on the ground.")
    print("You have lost health! decreeasing heath by",dcrsHlthMnr,"resulting in your")
    print("deacresing to", str(health) + ".")
else:
  print("You have died, you never escaped the forest!")
# sword
if health > 0:
  print("\nIn front of you see a sword in a stone wall, do you pick it up?")
  ("Big decicion, make sure you make the right choise!")
  sword = input("Type a Y for left or N for right ").upper()
  if sword == "Y":
    health = health + incrsHkthMJr
    print("The sword is hard to pull out but it fills you up with determation")
    print("You chose the right option")
    print("You have gained health by",incrsHkthMJr,"resulting in your heath levels ")
    print("increasing to",health)
  else:
    print("you choose not to pull out the sword.")
else:
  print("You have died, you never escaped the forest!")
# dream
if health > 0:
    print("\nYou wake up in bed, heart pounding.")
    print("A haunting nightmare lingers in your mind.")
    print("Echoes of the forest whisper to you.")
    print("Invisible watchers, unseen but felt, beckon.")
    print("Behind, only darkness; then, a chilling voice: 'Gotcha.'")
    print("\nGame over. Subject 72, awake. Location: Bravo Site-34. Time: 13:50.")
