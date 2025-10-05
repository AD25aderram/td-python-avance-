for i in range(10):
    if i < 5:
        print(" "*i+"* "*(5-i))
    else:
        print(" "*(10-i-1)+"* "*(i-4) + " "*(i-5))
