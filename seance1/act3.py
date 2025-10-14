#qst 1
a=int(input("Entrez la variable a: "))
b=int(input("Entrez la variable b: "))
print("La somme : ", a+b)
print("La multipliaction : ", a*b)

#qst 2
var1=input("Entrez la 1ere valeur: ")
var2=input("Entrez la 2eme valeur: ")

var3 = var1
var1 = var2
var2 = var3


print("La nouvelle valeur de var1: ", var1)
print("La nouvelle valeur de var2: ", var2)

#qst 3
nombre1 = float(input("Entrez le 1er nombre réel : "))
nombre2 = float(input("Entrez le 2ème nombre réel : "))
nombre3 = float(input("Entrez le 3ème nombre réel : "))

max_valeur = nombre1

if nombre2 > max_valeur:
    max_valeur = nombre2

if nombre3 > max_valeur:
    max_valeur = nombre3

print(f"Le maximum est la valeur : {max_valeur}")


#qst 4
unite = input("Choisissez l'unité de votre distance ('km' ou 'mile') : ").lower()
distance = float(input("Entrez la distance : "))

if unite == 'km':
    distance_convertie = distance * 0.6213
elif unite == 'mile':
    distance_convertie = distance / 0.6213
else:
    exit("Erreur : veuillez entrer 'km' ou 'mile'.")

print("La distance convertie est :", distance_convertie)
