#!/usr/bin/python3.6


'''a = 10
b = 5
print(a + b)
'''


'''text = "je suis du texte"

print (text*3)'''


'''text = text + "en plus"

print text
'''


'''

# 
txt = "Hello World!!!!!"

print len(txt)

print txt[1]

print [0:5]
'''

# Les espacements
'''print ("Bonjour je m'appelle %s " %("Emin"))'''


'''text = "je suis du \"texte\""

print (text)'''


# Liste

'''maListe = []
print type(maListe)
maListe = [1,2,3]

print maListe

# Ajout dans la List

maListe.append = "toto"

maListe.append[0] = "toto"
'''
# Supprimer l'index
'''maListe = ["1er","Deuxieme","Troisieme"]

del maListe[1]
print (maListe)'''

# Supprimer avec la valeur

'''maListe.remove("troisieme")

print maList'''


'''maListe = ["1er","Deuxieme","Troisieme"]

print maList.count("1er")




print maList.index("1er")'''

'''maListe = ["1er","Deuxieme","Troisieme"]

secondelist = maListe

maListe[0]="toto"

print (secondelist)'''




'''maListe = ["1er","Deuxieme","Troisieme"]

secondelist = maListe[:]

maListe[0]="toto"

print (secondelist)'''



'''maListe = ["1er","Deuxieme","Troisieme"]

print ("1er" in maListe)

print ("toto" in maListe)
'''

'''maListe = range(15)


liste = list(range(10))

liste.extend(maListe)
print (liste)'''



# Verif

'''maListe = ["1er","Deuxieme","Troisieme"]'''

'''MonTuple = ()
print (type(MonTuple))
MonTuple = ("toto")
print (type(MonTuple))
MonTuple[0]="error"
'''

# Dictionnaire
'''
MonDico = {}

MonDico["name"]="Emin"

MonDico["height"]="1m90"

print (MonDico["name"])
'''



# Fonction
'''
def ma_function():
	print "Salut les gens"

ma_function()
'''

'''
def somme(a,b):
	return a + b

som = somme (1,10)
print (som)
'''
'''
def splat_function(*param):
	print param

splat_function(1,2,"Salut")
'''



'''
a = "salut"

c = 5

def test():
	b = "test"
	print (c)

test()

print (a)
print (b) 
'''

# Rcuperer une entree dans le terminal
'''valeur = input("Enter your valeur")
print (type(valeur))'''

# Retourne une valeur d'une liste aleatoirement
'''random.choice([1,2,3,4,5])'''



# IF
'''
a = 10
if a > 5:
	print ("ok")
'''

# While
'''i = 0
while i < 10:
	print (i)
	i = i + 1
'''

'''
def exo04():
	enter = input("entrer un mot \n")
	print (len(enter))

exo04()
'''
'''
import random  #module permettant de generer des nombres pseudos aleatoires

mystere=random(0, 20)   # fonction permettant de generer des nombres aleatoires entier entre 0 et 20 en tout cas dans mon programme
print ('Voici un jeu dont vous devez deviner un nombre entre 0 et 20')   #l'instruction print sert a afficher du texte
print ('Entrer un nombre : ')
nombre=input()           # Pour stocker dans la variable nombre ce que a rentré l'utilisateur
while nombre != mystere:          # tant que nombre est different de la variable mystere
    print ('Entrez un nombre : ') 
    nombre=input()
else:                            #Quand le nombre est celui que le programme a generé
    print ('Bravo vous avez trouvé le bon numero ')

'''
print ("133")
from random import *
nbmystere = randint(1,10)
print (nbmystere)
nbenter = int(input("Saisir le nombre entre 1 et 10 : "))

def exo12():
	

	while (1) :
	
		if nbenter > nbmystere:
			print ("trop grand")
			exo12()
		if nbenter < nbmystere:
			print ("trop petit")
			exo12()
		if nbenter == nbmystere:
			print ("ok")
			break



exo12()
