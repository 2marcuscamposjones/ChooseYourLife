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
    print("\nYou have reached a cave, you must decide if you go in or not.")
    print("Big decicion, make sure you make the right choise!")
    cave = input("Type a Y for yes or N for no ").upper()
    if cave == "Y":
      health = health - dcrsHlthMnr
      print("You chose the wrong path, you fell into a hole.")
      print("You have lost health! decreeasing heath by",dcrsHlthMnr,"resulting in your")
      print("deacresing to", str(health) + ".")
    else:
      health = health + incrsHkthMJr
      print("You chose the right path, you found a medkit incresing your")
      print("health by",incrsHkthMJr,"resulting in your heath levels icreasing ")
      print("to",health)
else:
  print("You have died, you never escaped the forest!")
# river
# Programmer: Marcus Campos-Jones
if health > 0:
  print("\nYou have reached a river, you must decide if you go in or not.")
  print("Big decicion, make sure you make the right choise!")
  river = input("Type a Y for yes or N for no ").upper()
  if river == "Y":
    health = health + incrsHkthMJr
    print("You chose the rigjt path,the water heals your.")
    print("health by",incrsHkthMJr,"resulting in your heath levels icreasing ")
    print("to",health)
  else:
    health = health - dcrsHlthMnr
    print("You chose not get in the water, trip and hurt yourself.")
    print("You have lost health! decreeasing heath by",dcrsHlthMnr,"resulting in your")
    print("deacresing to", str(health) + ".")
else:
  print("You have died, you never escaped the forest!")
# house
# Programmer: Marcus Campos-Jones
if health > 0:
  print("\nYou have reached a house, you must decide if you go in or not.")
  print("Big decicion, make sure you make the right choise!")
  house = input("Type a Y for yes or N for no ").upper()
  if house == "Y":
    health = health - dcrsHlthMnr
    print("You chose the wrong path, you are attacked.")
    print("You have lost health! decreeasing heath by",dcrsHlthMnr,"resulting in your")
    print("deacresing to", str(health) + ".")
  else:
    health = health + incrsHkthMJr
    print("You chose the right path, the old lady gives you cookies increasing your")
    print("health by",incrsHkthMJr,"resulting in your heath levels icreasing ")
    print("to",health)
else:
  print("You have died, you never escaped the forest!")
# campfire
# Programmer: Marcus Campos-Jones
if health > 0:
  print("\nYou have reached a campfire, you must decide if you sit next to it or not.")
  print("Big decicion, make sure you make the right choise!")
  campfire = input("Type a Y for yes or N for no ").upper()
  if campfire == "Y":
    health = health +  incrsHkthMnr
    print("You chose the right option, you are warm.")
    print("You have gained health by",incrsHkthMnr,"resulting in your heath levels ")
    print("increasing to",health)
    print("You decide to sleep in the campfire for the night.")
  else:
    health = health - dcrsHlthMjr
    print("You chose the wrong option you freeze.")
    print("You have lost health! decreeasing heath by",dcrsHlthMjr,"resulting in your")
    print("deacresing to", str(health) + ".")
else:
  print("You have died, you never escaped the forest!")
# awake
# Programmer: Marcus Campos-Jones
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
# Programmer: Marcus Campos-Jones
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
# programmer: Marcus Campos-Jones
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
# Programmer: Marcus Campos-Jones
if health > 0:
  print("\nYou awake up in your bed.")
  print("What a terrible nightmare you think.")
  print("As you get out of bed you can hear the forrest calling you.")
  print("We are the invisable watchers we can see you, you should check behind you.")
  print("There is nothing but darkness behind you than you hear a voice say gotcha.\n")
  print("\nGame over,test subject 72,status awake,location Bravo site-34,time 13:50.")
