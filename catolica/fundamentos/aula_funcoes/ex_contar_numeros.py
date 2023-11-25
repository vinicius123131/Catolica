def contar_algarismos(numero):
    qtde_algarismos = 0
    while numero > 0:
        numero = numero // 10
        qtde_algarismos +=1
    return qtde_algarismos
def main():
    numero = int(input())
    print(contar_algarismos(numero))

main()