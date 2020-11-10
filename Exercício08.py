'''
08-Crie um programa que leia um número entre 2 e 20 e gere uma tela com a seguinte configuração:
Digite um número: 7
Saída do programa:
1234567
x123456
xx12345
xxx1234
xxxx123
xxxxx12
xxxxxx1
'''
lista=[]
x = int(input('Digite um número entre 2 e 20: '))

if x > 2 and x < 21:
    for i in range (x):
        lista.append(i+1)
print(lista)

cont = 0

for i in lista:
    lista[cont] = 'x'
    print(lista)
    cont+=1