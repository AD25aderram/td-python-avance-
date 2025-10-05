L3=[]
for i in range(5):
    L3.append(int(input("enter a number: ")))

for i in range(5):
    print(L3[i])


somme = 0
for i in L3:
    somme += i
print("la somme est:", somme)

produit = 1
for i in range(2,5):
    produit *= L3[i]
print("le produit est:", produit)

print("le maximum est:", max(L3))
print("le minimum est:", min(L3))


comp = 0
for i in L3:
    if i%3 == 0:
        comp += 1
print("le nombre des multiples de 3 est:", comp)


for i in range(5):
    print(L3[5-i-1])

    