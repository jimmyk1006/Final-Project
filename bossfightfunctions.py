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
stomp_hitpoints = 10
maul_hitpoints = 20
grullies_hitpoints = 200
player_hitpoints = 100
punch_hitpoints = 100
bash_hitpoints = 200
stage1p_hitpoints = gruul_hitpoints - punch_hitpoints
stage1b_hitpoints = gruul_hitpoints - bash_hitpoints

#Boss Fight 1 Left Tunnel Option
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

#Boss Fight Gruul
def bossfight1():
       print("Gruul is at", gruul_hitpoints, "hitpoints")
       print("Pick from the following for your first attack:")
       time.sleep(2)
       print("Punch or Bash")
       time.sleep(2)
       first_attack = input()
#Stage 1
       if first_attack == "Punch":
              print(name, "punches gruul in the face for", punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1p_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a stomp move and stomps on", name, "for", stomp_hitpoints, "hitpoints")
       else:
              print(name, "bashes gruul in the head for", bash_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1b_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a stomp move and stomps on", name, "for", stomp_hitpoints, "hitpoints")
#Stage 2

