def receber_valor(valor):
    global soma_total
    soma_total += valor

def printar_total():
    global soma_total
    print(f"a soma é {soma_total}")

def main():
    global soma_total
    soma_total = 0
    while True:
        numero = int(input("Digite um número: "))
        if numero <= 0:
            break
        receber_valor(numero)
        printar_total()

main()