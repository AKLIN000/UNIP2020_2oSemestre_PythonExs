'''
Elabore um algoritmo que leia dois vetores de dez posições e faça a multiplicação dos elementos da
seguinte forma: o primeiro do vetor 1 com o último do vetor 2, o segundo do vetor 1 com o penúltimo do
vetor 2 e assim por diante, colocando o resultado num terceiro vetor, que deve ser mostrado como saída.
'''

lista1 = []
lista2 = []
for i in range (10):
    lista1.append(int(input('Número para add na lista 1: ')))
for i in range (10):
    lista2.append(int(input('Número para add na lista 2: ')))
print(f'A 1a lista é : {lista1}')
print(f'\nA 2a lista é : {lista2}')
lista2.reverse()
x=0
lista3=[]
for i in range (1,11):
    lista3.append(lista1[x]*lista2[x])
    x+=1
print(f'\nA 1a lista multiplicada com o inverso da 2a lista é : {lista3}')