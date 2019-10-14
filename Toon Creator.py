#Intro to my program of Character Creation
print ("This is a Character Creation Program, Please read the following:")

print ("Character Creation Involves making a Character of your Choose")

print ("Character Creation program will allow pick options and make a toon based on your inputs")

print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")
import time
time.sleep(1)
#Program asks to pick your name
name = input("What is your character's name?: ")
print ("You have named your character:")
print (name)
time.sleep(4)
#Program asks to pick your class
print ("Next is to pick your character's class")
print ("The Following are Character Classes:")
print ("Warrior")
print ("Druid")
print ("Mage")
time.sleep(7)
print ("What class do you want", name, "to be?")
class_choice = input()
if class_choice == 'Mage':
    print ("You have chosen", name, "to be a MAGE")
elif class_choice == 'Druid':
    print ("You have chosen", name, "to be a DRUID")
elif class_choice == 'Warrior':
    print ("You have chosen", name, "to be a Warrior")
else:
    print ("Please Choose, Mage, Druid, or Warrior")
time.sleep(5)
#Program asks to pick your race
print ("Next is to pick your character's race")
print ("The Following are Character Races:")
print ("Night Elf")
print ("Orc")
print ("Worgen")
time.sleep(7)
print ("What Race do you want", name, "to be?")
race_choice = input()
if race_choice == 'Night Elf':
    print ("You have chosen", name, "to be an", race_choice, class_choice)
elif race_choice == 'Orc':
    print ("You have chosen", name, "to be an", race_choice, class_choice)
elif race_choice == 'Worgen':
    print ("You have chosen", name, "to be an", race_choice, class_choice)
else:
    print ("Please Choose, Night Elf, Orc, or Worgen")
#Program ask you to pick your armor type
time.sleep(4)
print ("Next is to pick your character's armor")
print ("The Following are Armor Types available:")
print ("Cloth")
print ("Leather")
print ("Plate")
time.sleep(7)
print ("What Armor type do you want", name, race_choice, class_choice, "to be?")
armor_choice = input()
print ("You have chosen your", race_choice, class_choice, name, "to wear", armor_choice, "Armor!")
#Program ask you to pick your armor color
time.sleep(4)
print ("Next is to pick your character's armor color")
print ("The Following are Armor Colors available:")
print ("Red")
print ("Blue")
print ("Orange")
print ("Pink")
print ("Purple")
print ("Black")
time.sleep(7)
print ("What color type do you want your armor to be?")
armor_color= input()
print ("You have chosen your", race_choice, class_choice, name, "to wear", armor_color, armor_choice, "Armor!")
#Program assings your weapon for you but allows you to choose an special ability for that class
time.sleep(4)
print ("Next is to pick your character's weapon special ability")
if class_choice == 'Mage':
    print ("By default Mage Class is assigned a Wand as a weapon")
    time.sleep(4)
    print ("The following are special abilities for the Wand Weapon:")
    time.sleep(4)
    print ("Ice burst, Which cast a huge ice burst against the enemy for 100 hitpoints"
           "and freezes the enemy in place for 15 seconds")
    time.sleep(4)
    print ("Fire Ball, Which cast an gigantic fire ball against the enemy for 100 hitpoints "
           "and burns the enemy for 10 seconds for 10 Hitpoints each second")
    time.sleep(4)
    mageabil = input("Please choose Ice burst or Fire ball: ")
    print ("You have assigned your", race_choice, class_choice, name, mageabil, "special ability")
elif class_choice == 'Druid':
    print ("By default Druid Class is assigned a Staff as a weapon")
    time.sleep(4)
    print ("The following are special abilities for the Staff Weapon:")
    time.sleep(4)
    print ("Moon Fire, Which cast a huge Moon Blast against the enemy for 100 hitpoints"
           "and burns the enemy for 10 seconds for 10 Hitpoints each second")
    time.sleep(4)
    print ("Star Fall, Which cast an rift of Stars onto your team, healing them for 100 hitpoints")
    time.sleep(4)
    druidabil = input("Please choose Moon Fire or Star Fall: ")
    print ("You have assigned your", race_choice, class_choice, name, druidabil, "special ability")
elif class_choice == 'Warrior':
    print ("By default Warrior Class is assigned a Sword as a weapon")
    time.sleep(4)
    print ("The following are special abilities for the Sword Weapon:")
    time.sleep(4)
    print ("Bladestorm, Which brings your Warrior into a frenzy hitting all enemies for 125 hitpoints")
    time.sleep(4)
    print ("Rend, Slices your enemy for 125 hitpoints and causes the enemy to bleed for 10 hit points every second for 10 seconds")
    time.sleep(4)
    warriorabil = input("Please choose Bladestorm or Rend: ")
    print ("You have assigned your", race_choice, class_choice, name, warriorabil, "special ability")
else:
    print ("Please Try Again")


