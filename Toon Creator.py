print ("This is a Character Creation Program, Please read the following:")

print ("Character Creation Involves making a Character of your Choose")

print ("Character Creation program will allow pick options and make a toon based on your inputs")

print ("Please Read all Questions and Instructions Carefully, Hope you enjoy")
import time
time.sleep(1)
name = input("What is your character's name?: ")
print ("You have named your character:")
print (name)
time.sleep(4)
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
