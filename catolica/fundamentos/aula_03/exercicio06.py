"""
6. Faça um programa que lê um número inteiro de 3 digito, e o programa deve apresentar a
quantidade de centenas, separado a de dezenas e por fim as unidades. Por exemplo, para o
número 341, a saída deve ser 3 centenas, 4 dezenas e 1 unidades.
"""

entrada = input('Digite três números para separação: ')
print('O número ', entrada, 'tem')
print(entrada[0], 'centenas')
print(entrada[1], 'dezenas')
print(entrada[2], 'unidade')
