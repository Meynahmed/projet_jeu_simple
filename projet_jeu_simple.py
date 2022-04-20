a=0
while  a <1 or a >10:
       a = float(input("saisissez un nombre compris entre 1 et 10:"))
       if a <1:
          print("Plus Grand")
       elif a >10:
           print ("Plus Petit ")

print ("vous etes dans le bon intervale")
if a%2==0:
   print("Vous avez gagné 10 Euros")
   if a<=3:
      print("Vous avez perdu 5 euros")