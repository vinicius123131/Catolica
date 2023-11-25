def segundo(segundos):
    return segundos%60

def minuto(segundos):
    segundos=segundos-segundo(segundos)
    return segundos//60

def hora(segundos):
    minutos = minuto(segundos)
    return minutos//60

def dia(segundos):
    horas = hora(segundos)
    return horas//24

def mes(segundos):
    dias = dia(segundos)
    return dias//30

def ano(segundos):
    meses = mes(segundos)
    return meses//12

def main():
    while True:
        segundos_input = int(input("Digite os segundos: "))
        if segundos_input <= 0:
            break

        minutos = minuto(segundos_input)
        horas = hora(segundos_input)
        dias = dia(segundos_input)
        meses = mes(segundos_input)
        anos = ano(segundos_input)
        print(f"anos: {anos}, meses: {meses},")
        print(f"dias: {dias}, horas: {horas}")
        print(f"minutos: {minutos}, segundos:{segundos_input}",)

main()
