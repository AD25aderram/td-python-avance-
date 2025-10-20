with open('Table_de_multiplication.txt','w+') as file:
    for i in range(1,11):
        file.write(f"la table de multiplication de 0{i}\n")
        for j in range(1,11):
            file.write(f"0{i} x 0{j} = {i*j}\n")
        file.write("\n")