"""
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a
idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
"""
import datetime

dataAtual = datetime.date.today()

print('Digite o nome da pesssoa que você quer calcular idade em dias')
nomePessoa = input('Nome: ')

print('Digite o dia do nascimento dessa pessoa')
diaNascimentoPessoa = int(input('Dia: '))

print('Digite o mês de nascimento dessa pessoa')
mesNascimentoPessoa = int(input('Mês: '))

print('Digite o ano de nascimento dessa pessoa')
anoNascimentoPesssoa = int(input('Ano: '))

dataNascimento = datetime.date(anoNascimentoPesssoa, mesNascimentoPessoa, diaNascimentoPessoa)

print("a data de nascimento de ", nomePessoa, " convertida em dias é igual a isso:")
print(dataAtual - dataNascimento)
