"""
Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao
total de eleitores.
"""
totalDeVotos = int(input('Digite o total de votos: '))
votosBrancos = int(input('Quantidade de votos BRANCOS: '))
votosNulos = int(input('Quantidade de votos NULOS: '))
votosValidos = int(input('Quantidade de votos VÁLIDOS: '))


def calcularPorcetagemFormula(total, numeroParaSaberPorcetagem):
    return (numeroParaSaberPorcetagem / total) * 100


print('Votos Brancos: ', calcularPorcetagemFormula(totalDeVotos, votosBrancos))
print('Votos Nulos: ', calcularPorcetagemFormula(totalDeVotos, votosNulos))
print('Votos Válidos: ', calcularPorcetagemFormula(totalDeVotos, votosValidos))
