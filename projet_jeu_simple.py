a=0
while  a <1 or a >10:
       a = float(input("saisissez un nombre compris entre 1 et 10:"))
       if a <1:
          print("Plus Grand")
       elif a >10:
           print ("Plus Petit ")

print ("vous etes dans le bon intervale")
if a%2==0:
   if a < 5:
      print("Vous avez gagné un euro.")
   elif a > 5:
      print("Vous avez perdu 3 euros.")
else:
    if a <= 5:
       print("vous avez gagné 2 euro")
    elif a == 5:
        print("vous avez rien gagné")
    else:
        print("vous avez perdu 4 euro")
#faire une boucle qui pour des nombres en dehors de l'intervalle mais compris entre 10 et 20, on rempli une liste vide avec ces nombres
list = []
while a > 10 and a < 20:
    nb = int(input(" entrer un nombre :"))
    list.append(nb)
    print( list)


