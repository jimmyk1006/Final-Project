import random
def randomnamepicker():

   names = [
   "Warford" ,"Oxton" ,"Sinan" ,"Mason" ,"Sigwald" ,"Deangelo" ,"Bertram" ,"Malvin" ,"Elijah" ,"Cearbhall" ,"Alexander" ,"Vico" ,
   "Prerue" ,"Galiena" ,"Blanca" ,"Gatty" ,"Cherise" ,"Anuschka" ,"Eartha" ,"Joseph" ,"Natalii" ,"Becky" ,"Maryam" ,"Sebastian" ,"Gabriel" ,"Carter" ,"Jayden" ,"Wilfreida" ,"Krimlo" ,"Licko"
   ]
   print(f"All names: {names}\n")

   idx = random.randint(0, len(names) - 1)
   name = (f"Name: {names[idx]}")
   print ("You have named your character:")
   print (name)

randomnamepicker()

