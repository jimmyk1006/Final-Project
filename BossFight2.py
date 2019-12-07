#Intro to my program of mini Boss fight 2
print ("This is the second Mini Boss Fight Program, Please read the following:")
print ("You will use your character that you created from the character creation program to defeat a boss.")
import time
time.sleep(2)
print ("Welcome to Mind Flare's Chambers, Second Mini Boss Fight")
print ("You will be fighting Mind Flare the Vision Seeker, as his name implies, he uses mind powers to try"
       " and take over the world, killing all he sees.")
time.sleep(2)
print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")

#Here I import my variable from the Toon Creator
from CharacterInfo import name, race_choice, class_choice, armor_choice, armor_color, specialabil
from bossfightfunctions import westchamber, bossfight2

#hitpoints
player_hitpoints = 100
print(name, "has", player_hitpoints, "hitpoints")
time.sleep(2)


#Start of the dungeon
print (name, "flys into Mind Flares's Chambers.", name, "sees two chambers, one to going to the west and one going to the east, only one chamber will allow you into the chambers!")
time.sleep(2)
print("Choose your decsion wisely!!!!")
time.sleep(2)
print ("What chamber do you want to fly into?")
chamber_choice = input("Choose West or East:")

print (name, "has chosen", chamber_choice, "chamber...good luck")
time.sleep(2)

#East Chamber
if chamber_choice == "East":
       print(name, "flys into the east chamber and falls into a pit of exploding stars and dies!!")
       print("GAME OVER!")
else:
       westchamber()


#Knob Fliers defeated now to boss!
print ("Are you ready to fight Mind Flare the Vision Seeker?")
readycheck = input("Answer Yes or No:")

if armor_choice == 'Cloth':
       print("Mind Flare laughs at", name,armor_choice, "armor", "and smacks all the", armor_choice, "armor off of", name)
       time.sleep(2)
       print("Mind Flare kills you game over!")

elif readycheck == 'Yes':
       bossfight2()
else:
       print("To bad Mind Flare doesn't care, he takes control of your mind and flys you into mouth.... you die!")
       time.sleep(2)
       print("GAME OVER!")
