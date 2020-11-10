'''
06-Fazer um algoritmo que calcule e escreva a soma dos 50 primeiros termos das seguintes séries:

...
4
991
3
994
2
997
1
1000
'''
x = 1000
y = 1
lista = []
soma = 0

for i in range(1,51):
    lista.append(x/i)
    x -= 3

x = 1000
y = 1

for i in lista:
    soma+=i
    print(f'{x}/{y} = {i}\nsoma de {soma-i:.4f} + {i:.4f} é {soma:.4f} (arredondados)')

    x-=3
    y+=1
    print()