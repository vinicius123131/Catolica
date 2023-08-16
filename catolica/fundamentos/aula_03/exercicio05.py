"""
5. Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
efetuadas. Escrever um algoritmo que leia o valor total de suas vendas e o salário fixo. Calcule e
escreva o salário final do vendedor.
"""
totalVendas = float(input('Digite o total das vendas do vendedor: '))
salarioFixo = float(input('Digite o valor do salário fixo: '))
comissaoVendedor = 5

def calcularValorPorcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

print('O salário do vendedor é ', salarioFixo + calcularValorPorcentagem(totalVendas, comissaoVendedor))


