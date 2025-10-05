t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
comp = 0
for i in range(len(t1)):
    comp += 1
    t2.insert(i+comp,t1[i])
print(t2)