def ler_float():
    return float(input("Digite um número float "))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a-b

n1 = ler_float()
n2 = ler_float()
n3 = ler_float()

print(subtracao(soma(n1, n2), n3))