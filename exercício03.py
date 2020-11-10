'''
03 – Escreva uma classe que leia um vetor de 30 posições de números inteiros e imprimir, logo após, gerar
2 vetores a partir dele, um contendo os elementos de posições ímpares do vetor e o outro os elementos
pares. Imprimi-los no final.
'''

lista = []
x = 0
for i in range(31):
    lista.append(x)
    x+=1
print(lista)

lista_par = []
lista_impar = []
for i in range (31):
    if i%2==0:
        lista_par.append(lista[i])
    else :
        lista_impar.append(lista[i])

print('Lista par : ',lista_par)    
print('lista ímpar: ',lista_impar)