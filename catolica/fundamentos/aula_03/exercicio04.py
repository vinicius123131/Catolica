"""
4. O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Suponha que o percentual do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica
de um carro, calcular e escrever o custo final ao consumidor.
"""
porcentagemJurosDistribuidor = 28
porcentagemJurosImpostos = 45

print('Bem vindo! vamos te ajudar a calcular o valor final para venda ao consumidor')

custoFabricaProducaoCarro = float(input('Custo de fábrica de um carro: '))

def calcularValorPorcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

custoConsumidorFinal = custoFabricaProducaoCarro + calcularValorPorcentagem(custoFabricaProducaoCarro, porcentagemJurosImpostos) + calcularValorPorcentagem(custoFabricaProducaoCarro, porcentagemJurosDistribuidor)

print('Valor final do carro é: ', custoConsumidorFinal)
