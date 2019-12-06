#Intro to my program of mini Boss fight 1
print ("This is the first Mini Boss Fight Program, Please read the following:")
print ("You will use your character that you created from the character creation program to defeat a boss.")
import time
time.sleep(2)
print ("Welcome to Gruul's Lair, First Mini Boss Fight")
print ("You will be fighting Gruul the Dragonslayer, as his name implies, he is a reowned"
       " dragon-slayer, killing all dragons in sight.")
time.sleep(2)
print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")

#Here I import my variable from the Toon Creator
from CharacterInfo import name, race_choice, class_choice, armor_choice, armor_color, specialabil
from bossfightfunctions import lefttunnel, bossfight1

#hitpoints
player_hitpoints = 100
print(name, "has", player_hitpoints, "hitpoints")
time.sleep(2)


#Start of the dungeon
print (name, "walks into Gruul's Lair.", name, "sees two tunnels, one to the left and right, only one tunnel will allow you into the lair!")
time.sleep(2)
print("Choose your decsion wisely!!!!")
time.sleep(2)
print ("What tunnel do you want to walk down?")
tunnel_choice = input("Choose Left or Right:")

print (name, "has chosen", tunnel_choice, "tunnel...good luck")
time.sleep(2)

#Right Tunnel
if tunnel_choice == "Right":
       print(name, "runs into the right tunnel and falls into a pit of spikes and dies!!")
       print("GAME OVER!")
else:
       lefttunnel()


#Gruulies defeated now to boss!
print ("Are you ready to fight Gruul the Dragonslayer?")
readycheck = input("Answer Yes or No:")

if armor_color == 'Pink':
       print("Gruul laughs at", name,armor_color, "armor", "and smacks all the", armor_color, "armor off of", name)
       time.sleep(2)
       print("Gruul kills you game over!")

elif readycheck == 'Yes':
       bossfight1()
else:
       print("To bad Gruul doesn't care, he smashes you in the face and you die!")
       time.sleep(2)
       print("GAME OVER!")
