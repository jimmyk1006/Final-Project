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

#Boss Fights Shared Variables
player_hitpoints = 100
punch_hitpoints = 100
bash_hitpoints = 100

#Boss Fight 1 Variables
gruul_hitpoints = 500
stomp_hitpoints = 10
maul_hitpoints = 20
grullies_hitpoints = 200
stage1p_hitpoints = gruul_hitpoints - punch_hitpoints
stage1b_hitpoints = gruul_hitpoints - bash_hitpoints

#Boss Fight 2 Variables
mindflare_hitpoints = 500
mindcontrol_hitpoints = 10
shadowmend_hitpoints = 20
knob_hitpoints = 200
stage1pp_hitpoints = mindflare_hitpoints - punch_hitpoints
stage1bb_hitpoints = mindflare_hitpoints - bash_hitpoints

#Boss Fight 3 Variables
gilgrog_hitpoints = 500
slimespit_hitpoints = 10
taillash_hitpoints = 20
gilminions_hitpoints = 200
stage1ppp_hitpoints = mindflare_hitpoints - punch_hitpoints
stage1bbb_hitpoints = mindflare_hitpoints - bash_hitpoints


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
              time.sleep(2)
              print (name, "now has", player_hitpoints - stomp_hitpoints, "hitpoints")
       else:
              print(name, "bashes gruul in the head for", bash_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1b_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a stomp move and stomps on", name, "for", stomp_hitpoints, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - stomp_hitpoints, "hitpoints")
#Stage 2
       print("Pick from the following for your second attack:")
       print("Punch, Punch")
       time.sleep(2)
       print("Bash, Bash")
       time.sleep(2)
       print("Punch, Bash")
       time.sleep(2)
       second_attack = input()
       if second_attack == "Punch, Punch":
              print(name, "punches gruul in the face twice for", punch_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1p_hitpoints - punch_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a double stomp move and stomps on", name, "for", stomp_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - stomp_hitpoints * 3, "hitpoints")
       elif second_attack == "Bash, Bash":
              print(name, "bashes gruul in the head twice for", bash_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1b_hitpoints - bash_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a double stomp move and stomps on", name, "for", stomp_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - stomp_hitpoints * 3, "hitpoints")
       else:
              print(name, "punches gruul in the face and bashes him in the head for", bash_hitpoints + punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Gruul now has", stage1b_hitpoints - bash_hitpoints - punch_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Gruul fires back with a double stomp move and stomps on", name, "for", stomp_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - stomp_hitpoints * 3, "hitpoints")

#Stage 3

       print("Congratz you have weakend Gruul to 20% of his health! This brings you into stage 3....final stage of the boss fight")
       time.sleep(2)
       print('In this phase of the fight you will be allowed to use your Special Ability...')
       time.sleep(2)
       print("Gruul is staggering all of the place, lets finish him!")
       time.sleep(2)
       print("Gruul is currently at 200 hitpoints")
       print("Do you want to finish him with your Special Ability?")
       stage3 = input("Type Y or N:")
       for Y in stage3:
              if specialabil == "Ice Burst":
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")
              elif specialabil == "Fire Ball":
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")
              elif specialabil == "Moon Fire":
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")
              elif specialabil == "Star Fall":
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")
              elif specialabil == "Bladestorm":
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")
              else:
                     print(name, "hits Gruul with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #1!")




#Boss Fight 2 West Chamber Option
def westchamber():
       #West Chamber
       print (name, "flys into the West Chamber....")
       time.sleep(2)
       print (name, "gets attacked by knob fliers!!!")
       time.sleep(2)
       print ("Knob fliers have", knob_hitpoints, "hitpoints")
       time.sleep(2)
       print ("Do you want to use", name,"'s special ability to defeat the Knob fliers")
       time.sleep(2)
       usespecabil = input("Type Yes to cast your special ability upon the Knob fliers:")
       if usespecabil == "Yes":
              print(name, "hits all the Knob fliers with", specialabil, "for 200 hitpoints")
              time.sleep(2)
              print("Congratz", name, "has defeated Knob fliers now on to the main boss...Mind Flare")
              time.sleep(2)
       else:
              print("Game over, follow the directions please!!!!")

#Boss Fight Mind Flare
def bossfight2():
       print("Mindflare is at", mindflare_hitpoints, "hitpoints")
       print("Pick from the following for your first attack:")
       time.sleep(2)
       print("Punch or Bash")
       time.sleep(2)
       first_attack = input()
#Stage 1
       if first_attack == "Punch":
              print(name, "punches Mind Flare in the face for", punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Mind Flare now has", stage1pp_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Mind Flare fires back with a mind control spell and scrambles", name, "mind for", mindcontrol_hitpoints, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - mindcontrol_hitpoints, "hitpoints")
       else:
              print(name, "bashes Mind Flare in the head for", bash_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Mind Flare now has", stage1bb_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Mind fires back with a stomp move and stomps on", name, "for", mindcontrol_hitpoints, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - mindcontrol_hitpoints, "hitpoints")
#Stage 2
       print("Pick from the following for your second attack:")
       print("Punch, Punch")
       time.sleep(2)
       print("Bash, Bash")
       time.sleep(2)
       print("Punch, Bash")
       time.sleep(2)
       second_attack = input()
       if second_attack == "Punch, Punch":
              print(name, "punches Mind Flare  in the face twice for", punch_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("Mind Flare now has", stage1pp_hitpoints - punch_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("Mind Flare fires back with a double move and puts Mind Control on", name, "for", mindcontrol_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - mindcontrol_hitpoints * 3, "hitpoints")
       elif second_attack == "Bash, Bash":
              print(name, "bashes Mind Flare in the head twice for", bash_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("Mind Flare now has", stage1bb_hitpoints - bash_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("Mind Flare fires back with a double move and puts Mind Control on", name, "for", mindcontrol_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - mindcontrol_hitpoints * 3, "hitpoints")
       else:
              print(name, "punches Mind Flare in the face and bashes him in the head for", bash_hitpoints + punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("Mind Flare now has", stage1bb_hitpoints - bash_hitpoints - punch_hitpoints, "hitpoints")
              time.sleep(2)
              print ("Mind Flare fires back with a double move and puts Mind Control on", name, "for", mindcontrol_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - mindcontrol_hitpoints * 3, "hitpoints")

#Stage 3

       print("Congratz you have weakend Mind Flare to 20% of his health! This brings you into stage 3....final stage of the boss fight")
       time.sleep(2)
       print('In this phase of the fight you will be allowed to use your Special Ability...')
       time.sleep(2)
       print("Mind flare is staggering all of the place, lets finish him!")
       time.sleep(2)
       print("Mine Flare is currently at 200 hitpoints")
       print("Do you want to finish him with your Special Ability?")
       stage3 = input("Type Y or N:")
       for Y in stage3:
              if specialabil == "Ice Burst":
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")
              elif specialabil == "Fire Ball":
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")
              elif specialabil == "Moon Fire":
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")
              elif specialabil == "Star Fall":
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")
              elif specialabil == "Bladestorm":
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")
              else:
                     print(name, "hits Mind Flare with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #2!")



#Boss Fight 3 Left Entrance Option
def leftentrance():
       #Left Entrance
       print (name, "rides his trusty stead into the left entrance....the gate flys open and")
       time.sleep(2)
       print (name, "gets attacked by gilgorg minions!!!")
       time.sleep(2)
       print ("Gilgorg Minionss have", gilminions_hitpoints, "hitpoints")
       time.sleep(2)
       print ("Do you want to use", name,"'s special ability to defeat Gilgrog Minions")
       time.sleep(2)
       usespecabil = input("Type Yes to cast your special ability upon the Gilgrog Minions:")
       if usespecabil == "Yes":
              print(name, "hits all of Gilgrog minions with", specialabil, "for 200 hitpoints")
              time.sleep(2)
              print("Congratz", name, "has defeated Gilgrog minons now on to the main boss...Gilgrog")
              time.sleep(2)
       else:
              print("Game over, follow the directions please!!!!")


#Boss Fight Gilgrog
def bossfight3():
       print("Gilgrog is at", gilgrog_hitpoints, "hitpoints")
       print("Pick from the following for your first attack:")
       time.sleep(2)
       print("Punch or Bash")
       time.sleep(2)
       first_attack = input()
#Stage 1
       if first_attack == "Punch":
              print(name, "punches gilgrog in the face for", punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("gilgrog now has", stage1ppp_hitpoints, "hitpoints")
              time.sleep(2)
              print ("gilgrog fires back with a smilespit spell on", name, "and hits for", slimespit_hitpoints, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - slimespit_hitpoints, "hitpoints")
       else:
              print(name, "bashes gilgrog in the head for", bash_hitpoints, "hitpoints.")
              time.sleep(2)
              print("gilgrog now has", stage1bbb_hitpoints, "hitpoints")
              time.sleep(2)
              print ("gilgrog fires back with a slimespit spell on", name, "and hits for", slimespit_hitpoints, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - slimespit_hitpoints, "hitpoints")
#Stage 2
       print("Pick from the following for your second attack:")
       print("Punch, Punch")
       time.sleep(2)
       print("Bash, Bash")
       time.sleep(2)
       print("Punch, Bash")
       time.sleep(2)
       second_attack = input()
       if second_attack == "Punch, Punch":
              print(name, "punches gilgrog in the face twice for", punch_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("gilgrog  now has", stage1ppp_hitpoints - punch_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("gilgrog fires back with a double move of slimespit and hits", name, "for", slimespit_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - slimespit_hitpoints * 3, "hitpoints")
       elif second_attack == "Bash, Bash":
              print(name, "bashes gilgrog in the head twice for", bash_hitpoints * 2, "hitpoints.")
              time.sleep(2)
              print("gilgrog now has", stage1bbb_hitpoints - bash_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print ("gilgrog fires back with a double move of slimespit and hits", name, "for", slimespit_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - slimespit_hitpoints * 3, "hitpoints")
       else:
              print(name, "punches gilgrog in the face and bashes him in the head for", bash_hitpoints + punch_hitpoints, "hitpoints.")
              time.sleep(2)
              print("gilgrog now has", stage1bbb_hitpoints - bash_hitpoints - punch_hitpoints, "hitpoints")
              time.sleep(2)
              print ("gilgrog fires back with a double move of slimespit and hits", name, "for", slimespit_hitpoints * 2, "hitpoints")
              time.sleep(2)
              print (name, "now has", player_hitpoints - slimespit_hitpoints * 3, "hitpoints")

#Stage 3

       print("Congratz you have weakend gilgrog to 20% of his health! This brings you into stage 3....final stage of the boss fight")
       time.sleep(2)
       print('In this phase of the fight you will be allowed to use your Special Ability...')
       time.sleep(2)
       print("gilgrog is staggering all of the place, lets finish him!")
       time.sleep(2)
       print("gilgrog is currently at 200 hitpoints")
       print("Do you want to finish him with your Special Ability?")
       stage3 = input("Type Y or N:")
       for Y in stage3:
              if specialabil == "Ice Burst":
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")
              elif specialabil == "Fire Ball":
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")
              elif specialabil == "Moon Fire":
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")
              elif specialabil == "Star Fall":
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")
              elif specialabil == "Bladestorm":
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")
              else:
                     print(name, "hits gilgrog with", specialabil, "and finishes him!")
                     time.sleep(4)
                     print("Congratz", name, "you have defeated Boss Fight #3!")


