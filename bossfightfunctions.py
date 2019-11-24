import time
from CharacterInfo import name, race_choice, class_choice, armor_choice, armor_color, specialabil
#Global Variables
#Here I set variables for when you will use your weapons special ability
Ice_burst = 200
Fire_Ball = 200
Moon_Fire = 200
Star_Fall = 200
Bladestorm = 200
Rend = 200

#Boss Fight 1 Variables
gruul_hitpoints = 1000
grullies_hitpoints = 200

def lefttunnel():
       #Left Tunnel
       print ("Down the left tunnel goes", name)
       time.sleep(2)
       print (name, "gets attacked by grullies!!!")
       time.sleep(2)
       print ("Grullies have", grullies_hitpoints, "hitpoints")
       time.sleep(2)
       print ("Do you want to use", name,"'s special ability to defeat the grullies")
       time.sleep(2)
       usespecabil = input("Type Yes to cast your special ability upon the grullies:")
       if usespecabil == "Yes":
              print(name, "hits all the grullies with", specialabil, "for 200 hitpoints")
              time.sleep(2)
              print("Congratz", name, "has defeated grullies now on to the main boss...Gruul")
              time.sleep(2)
       else:
              print("Game over, follow the directions please!!!!")

