"""
Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
Calcular e escrever o valor do novo salário.
"""
print('Digite o nome do funcinário que você quer saber o reajuste salarial')
nomeFuncionario = input('Nome: ')

salarioFuncinario = float(input('Salário: '))

reajusteEmPorcentagem = float(input('Digite a porcentagem do reajuste: '))

def calcularValorDoAumento(valor, porcentagemValor):
    return (valor * porcentagemValor) / 100

print("O salário do funcionário: ", nomeFuncionario)
print("Atualizado com o reajuste fica: ", salarioFuncinario+calcularValorDoAumento(salarioFuncinario, reajusteEmPorcentagem))