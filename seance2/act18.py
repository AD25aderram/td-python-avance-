machines = {
    "m1": "192.168.0.1",
    "m2": "192.168.0.2",
    "m3": "192.168.0.3",
    "m4": "192.168.0.4",
    "m5": "192.168.0.5",
}

print("l'adresse IP de m2 est", machines["m2"])

comp = 0
for i in machines:
    comp+=1
print(comp)

machines["m6"]="198.160.0.6"

del machines["m4"]

if "m5" in machines:
    print("il y a")
else:
    print("il n y a pas")



cle = input("donner votre machines : ")
if cle in machines:
    print("l'adresse IP de ", cle, " est", machines[cle])
else:
    print("la machine ", cle, "n'est pas repertoriee")


