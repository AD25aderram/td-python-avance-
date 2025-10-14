def F1(n):
    for i in range(n):
        print("bonjour")

def F2(n):
    if n%10 == 0:
        return True 
    else:
        return False
    
def F4(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact      

def F3(mot):
    comp = 0
    for letter in mot:
        if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'u' or letter == 'i' or letter == 'y':
            comp+=1
    return comp

def F5(n):
    for i in range(10):
        print(f"{n}*{i}={n*i}")

def F6(mot):
    comp = 0
    for letter in mot:
        comp+=1
    return comp

def F7(n):
    solution1 = 1
    solution2 = 1
    for i in range(n):
        solution3 = solution2 + solution1
        print(f"{solution1}+{solution2}={solution3}")
        solution1 = solution2
        solution2 = solution3 






