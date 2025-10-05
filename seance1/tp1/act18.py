for i in range(12):
    if i < 6:
        for j in range(i):
            print("*", end=" ")
    else:
        for j in range(10, i, -1):
            print("*", end=" ")
    print("")