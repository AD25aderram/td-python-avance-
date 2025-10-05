adress_ip = ["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]

#qst 1
print(adress_ip[0])

#qst 2
print(adress_ip[4])

#qst 3
print(adress_ip[2])

#qst 4
adress_ip.append("172.31.0.1")

#qst 5
adress_ip.remove("200.100.50.1")

#qst 6
print(len(adress_ip))

#qst 7
if "192.168.0.1" in adress_ip:
    print("il exist")
else:
    print("il n'exist pas")

#qst 8
print("la classe de ", adress_ip[1], " est : class A")

#qst 9
adress_ip.sort()

#qst 10
for adrs in adress_ip:
    if adrs != "192.168.0.1":
        print("c'est faux que tous les adress ip appartiennet a la classe C")
        break
else:
    print("c'est vrai que tous les adress ip appartiennet a la classe C")

#qst 11
comp = 0
for adrs in adress_ip:
    if adrs == "200.100.50.1":
        comp += 1
print("il exist ",comp ," adress public")   