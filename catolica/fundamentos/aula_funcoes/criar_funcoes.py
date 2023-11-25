def isPar(n):
    if (n%2 == 0):
        return True
    return False

def isParPrint(n):
    if isPar(n):
        return print(f"{n} is par")
    return print(f"{n} is impar")

def isImpar(n):
    return not isPar(n)

def menorQueZero(n):
    if n < 0:
        return True
    return False

def isValid():
    while True:
        n = int(input("Input a number "))
        n1 = int(input("Input a number "))
        if menorQueZero(n) or menorQueZero(n1):
            print("Input is invalid")
            print()
        else:
            isParPrint(n)
            isParPrint(n1)
            print()

isValid()


