'''
Desenvolva um programa que receba 25 números (tipo float) digitados pelo usuário e apresente no final
a quantidade de números positivos, negativos, zeros, pares e ímpares digitados.
'''
import random
lista = []
for i in range (25):
    lista.append(float(input('Valor a ser add na Lista: ')))
print(f'Sua lista é:\n{lista}')

lista_negativos = []
lista_positivos = []
zeros = []
pares = []
impares = []

for i in lista:
    if i > 0:
        lista_positivos.append(i)
    elif i < 0:
        lista_negativos.append(i)
    elif i == 0:
        zeros.append(i)
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print(f'''\nQuantidade de Números positivos é: {len(lista_positivos)}
Quantidade de Números negativos é: {len(lista_negativos)}
Quantidade de números zeros é: {len(zeros)}
Quantidade de números pares é: {len(pares)}
E a quantidade de Ímpares é : {len(impares)}''')
