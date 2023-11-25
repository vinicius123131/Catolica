def printar_caracteres_linha(qtde, caractere):
    i = 0
    while i < qtde:
        print(caractere, end="")
        i +=1
    print()

def printar_linhas(qtde_linha, qtde_caractere, caractere):
    i = 0
    while i < qtde_linha:
        printar_caracteres_linha(qtde_caractere, caractere)
        i+=1

def main():
    qtde, caractere = input("QTDE, Caractere: ").split()
    qtde = int(qtde)
    printar_caracteres_linha(qtde, caractere)
    qtde_linhas= int(input("Qual a quantidade de linhas: "))
    printar_linhas(qtde_linhas, qtde, caractere)

main()