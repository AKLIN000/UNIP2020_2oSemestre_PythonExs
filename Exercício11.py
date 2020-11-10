'''
11–Construa um programa que, para um grupo de 50 valores inteiros, determine:
a) A soma dos números positivos;
b) A quantidade de valores negativos;
'''

lista = []
soma = 0
lista_negativos = []

for i in range (50):
    lista.append(int(input('Valor a ser adicionados à lista: ')))

for i in lista:
    if i > 0:
        soma+=i
    elif i < 0:
        lista_negativos.append(i)

print(f'A lista é {lista} a soma dos positivos da lista é \n{soma} e a quatidade de valores negativos dessa lista é {len(lista_negativos)} ')