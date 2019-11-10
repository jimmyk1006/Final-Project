#Intro to my program of mini Boss fight 1
print ("This is the first Mini Boss Fight Program, Please read the following:")
print ("You will use your character that you created from the character creation program to defeat a boss")
import time
time.sleep(2)
print ("Welcome to Gruul's Lair, First Mini Boss Fight")
print ("You will be fighting Gruul the Dragonslayer, as his name implies, he is a reowned"
       " dragon-slayer, killing all dragons in sight.")
time.sleep(2)
print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")

#Here I import my variable from the Toon Creator
from CharacterInfo import name, race_choice, class_choice, armor_choice, armor_color, specialabil

#hitpoints
gruul_hitpoints = 1000
player_hitpoints = 100
print(name, "has", player_hitpoints, "hitpoints")
time.sleep(2)
print("Choose your decsions wisely!!!!")
time.sleep(2)

#Start of the dungeon
print (name, "walks into Gruul's Lair.", name, "sees two tunnels, one to the left and right, only one tunnel will allow you into the lair!")
time.sleep(2)
print ("What tunnel do you want walk down?")
tunnel_choice = input("Choose Left or Right:")
print (name, "has chosen", tunnel_choice, "tunnel...good luck")
#Here I set variables for when you will use your weapons special ability
#Ice burst
#Fire Ball
#Moon Fire
#Star Fall
#Bladestorm
#Rend

#print ("Are you ready to fight Gruul the Dragonslayer")
#readycheck = input("Answer Yes or No")
#if readycheck == 'Yes':
