#Intro to my program of mini Boss fight 3
print ("This is the thrid Mini Boss Fight Program, Please read the following:")
print ("You will use your character that you created from the character creation program to defeat a boss.")
import time
time.sleep(2)
print ("Welcome to Gilgrogs's Hollow, Thrid Mini Boss Fight")
print ("You will be fighting Gilgrog the flesh reaper, as his name implies, he loves to rip all the flesh"
       " off of his enemies and enjoys its as his meals.")
time.sleep(2)
print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")

#Here I import my variable from the Toon Creator
from CharacterInfo import name, race_choice, class_choice, armor_choice, armor_color, specialabil
from bossfightfunctions import leftentrance, bossfight3

#hitpoints
player_hitpoints = 100
print(name, "has", player_hitpoints, "hitpoints")
time.sleep(2)


#Start of the dungeon
print (name, "rides his trusty stead into Gilgrog's Hollow.", name, "sees two gated entrances, one to the left and one to the right, only one gated entrance will allow you into the hollow!")
time.sleep(2)
print("Choose your decsion wisely!!!!")
time.sleep(2)
print ("What gated entrance do you want to ride your trusty stead into?")
entrance_choice = input("Choose Left or Right:")

print (name, "has chosen", entrance_choice, "gated entrance...good luck")
time.sleep(2)

#Right Entrance
if entrance_choice == "Right":
       print(name, "rides his trusty stead into the right entrance and trys to open but its locked!")
       time.sleep(2)
       print(name, "trys to use his special ability of", specialabil, "to open the gate but when", specialabil, "hits the gate...it explodes")
       time.sleep(2)
       print("Gilgrog riged the gate with explosives and you exploded in the attempt of breaking the gate down...you die!")
       time.sleep(2)
       print("GAME OVER!")
else:
       leftentrance()


#Gilgrogs minions defeated now to boss!
print ("Are you ready to fight Gilgrog the flesh reaper?")
readycheck = input("Answer Yes or No:")

if race_choice == 'Orc':
       print("Gilgrog laughs at", name, "because he is an Orc. Gilgrog has a natural immunity to orcs...")
       time.sleep(2)
       print("Gilgrog spits green slime all over you...you dissolve and die")
       time.sleep(2)
       print("Gilgrog kills you game over!")

elif readycheck == 'Yes':
       bossfight3()
else:
       print("To bad Gilgrog doesn't care, he spits green slime all over and it dissovles your brain.... you die!")
       time.sleep(2)
       print("GAME OVER!")
