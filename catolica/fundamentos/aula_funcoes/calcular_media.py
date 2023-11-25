def receber_numeros():
    a = input("Digite um número: ")
    if a == "c":
        return None
    return int(a)

def calcular_media(a,b):
    global media 
    media +=a
    return media/b

def main():
    i = 1
    global media
    media = 0
    while i > 0:
        n = receber_numeros()
        if n == None:
            break
        print(f"Média igual {calcular_media(n,i)}")
        i+=1

main()