# Intro to my program of Character Creation
print("This is a Character Creation Program, Please read the following:")

print("Character Creation Involves making a Character of your Choose")

print("Character Creation program will allow you to pick options and will make a character based on your inputs")

print("Please Read all Questions and Instructions Carefully, Hope you enjoy")
import time
import random
time.sleep(1)

# Program asks to pick your name
print("First thing is to choose your Character's name!")
time.sleep(2)
name_choice = input("Do you want to come up with your own name for your character or use the random name picker?"
                    " Please type my own or random?")
if name_choice == 'my own':
    print("What is your character's name?: ")
    name = input('')
    print("You have named your character:")
    print(name)
elif name_choice == 'random':
    names = [
        "Warford", "Oxton", "Sinan", "Mason", "Sigwald", "Deangelo", "Bertram", "Malvin", "Elijah", "Cearbhall",
        "Alexander", "Vico",
        "Prerue", "Galiena", "Blanca", "Gatty", "Cherise", "Anuschka", "Eartha", "Joseph", "Natalii", "Becky", "Maryam",
        "Sebastian",
        "Gabriel", "Carter", "Jayden", "Wilfreida", "Krimlo", "Licko"]
    idx = random.randint(0, len(names) - 1)
    name = (names[idx])
    print("You have named your character:")
    print(name)
else:
    print('Try Again')

# Program asks to pick your class
time.sleep(4)
print("Next is to pick your character's class")
print("The Following are Character Classes:")
print("Warrior")
print("Druid")
print("Mage")
time.sleep(7)
print("What class do you want", name, "to be?")
class_choice = input()
if class_choice == 'Mage':
    print("You have chosen", name, "to be a MAGE")
elif class_choice == 'Druid':
    print("You have chosen", name, "to be a DRUID")
elif class_choice == 'Warrior':
    print("You have chosen", name, "to be a Warrior")
else:
    print("Please Choose, Mage, Druid, or Warrior")

# Program asks to pick your race
time.sleep(5)
print("Next is to pick your character's race")
print("The Following are Character Races:")
print("Night Elf")
print("Orc")
print("Worgen")
time.sleep(7)
print("What Race do you want", name, "to be?")
race_choice = input()
if race_choice == 'Night Elf':
    print("You have chosen", name, "to be an", race_choice, class_choice)
elif race_choice == 'Orc':
    print("You have chosen", name, "to be an", race_choice, class_choice)
elif race_choice == 'Worgen':
    print("You have chosen", name, "to be an", race_choice, class_choice)
else:
    print("Please Choose, Night Elf, Orc, or Worgen")

# Program ask you to pick your armor type
time.sleep(4)
print("Next is to pick your character's armor")
print("The Following are Armor Types available:")
print("Cloth")
print("Leather")
print("Plate")
time.sleep(7)
print("What Armor type do you want", name, race_choice, class_choice, "to be?")
armor_choice = input()
print("You have chosen your", race_choice, class_choice, name, "to wear", armor_choice, "Armor!")

# Program ask you to pick your armor color
time.sleep(4)
print("Next is to pick your character's armor color")
print("The Following are Armor Colors available:")
print("Red")
print("Blue")
print("Orange")
print("Pink")
print("Purple")
print("Black")
time.sleep(7)
print("What color type do you want your armor to be?")
armor_color = input()
print("You have chosen your", race_choice, class_choice, name, "to wear", armor_color, armor_choice, "Armor!")

# Program assings your weapon for you but allows you to choose an special ability for that class
time.sleep(4)
print("Next is to pick your character's weapon special ability")
if class_choice == 'Mage':
    print("By default Mage Class is assigned a Wand as a weapon")
    time.sleep(4)
    print("The following are special abilities for the Wand Weapon:")
    time.sleep(4)
    print("Ice burst, Which cast a huge ice burst against the enemy for 100 hit points"
          " and freezes the enemy in place for 15 seconds")
    time.sleep(4)
    print("Fire Ball, Which cast an gigantic fire ball against the enemy for 100 hit points "
          " and burns the enemy for 10 seconds for 10 Hitpoints each second")
    time.sleep(4)
    specialabil = input("Please choose Ice Burst or Fire Ball: ")
    print("You have assigned your", race_choice, class_choice, name, "the", specialabil, "special ability")
elif class_choice == 'Druid':
    print("By default Druid Class is assigned a Staff as a weapon")
    time.sleep(4)
    print("The following are special abilities for the Staff Weapon:")
    time.sleep(4)
    print("Moon Fire, Which cast a huge Moon Blast against the enemy for 100 hit points"
          " and burns the enemy for 10 seconds for 10 hit points each second")
    time.sleep(4)
    print("Star Fall, Which cast an rift of Stars onto your team, healing them for 100 hit points")
    time.sleep(4)
    specialabil = input("Please choose Moon Fire or Star Fall: ")
    print("You have assigned your", race_choice, class_choice, name, "the", specialabil, "special ability")
elif class_choice == 'Warrior':
    print("By default Warrior Class is assigned a Sword as a weapon")
    time.sleep(4)
    print("The following are special abilities for the Sword Weapon:")
    time.sleep(4)
    print("Bladestorm, Which brings your Warrior into a frenzy hitting all enemies for 125 hitpoints")
    time.sleep(4)
    print(
        "Rend, Slices your enemy for 125 hitpoints and causes the enemy to bleed for 10 hit points every second for 10 seconds")
    time.sleep(4)
    specialabil = input("Please choose Bladestorm or Rend: ")
    print("You have assigned your", race_choice, class_choice, name, "the", specialabil, "special ability")
else:
    print("Please Try Again")

# Ending
time.sleep(2)
print("Congratz you have completed your character creation!!!!")
time.sleep(2)
print("You have created the following character:")
print(name, "the", race_choice, class_choice, "wearing", armor_color, armor_choice, "armor",
      "with the special ability of", specialabil)
time.sleep(2)

#saves character info into a
f = open('CharacterInfo.py', 'w+')
f.write("name = '%s'" % name)
f.write("\n" "race_choice = '%s'" % race_choice)
f.write("\n" "class_choice = '%s'" % class_choice)
f.write("\n" "armor_color = '%s'" % armor_color)
f.write("\n" "armor_choice = '%s'" % armor_choice)
f.write("\n" "specialabil = '%s'" % specialabil)
f.close()
