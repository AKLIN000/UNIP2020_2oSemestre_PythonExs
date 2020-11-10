'''
02-Escrever um algoritmo que produza na tela um triângulo de Pascal de grau “n” usando uma matriz.
Abaixo temos um triângulo de Pascal de grau 6 (isto é, com seis linhas):

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

Os elementos extremos em cada linha são iguais a 1. Os outros são obtidos somando-se os dois valores que
aparecem imediatamente acima e à esquerda na linha anterior. Exemplo: O quarto elemento da linha
corresponde a soma do quarto e do terceiro elemento na linha anterior, isto é, 4 = 1 + 3.
'''
def pascal(n1): #MÉTODO PARA O PASCAL
    triangulo = [[]for i in range (n1)]
    for i in range (n1):
        for j in range (i+1):
            if (i>j):
                if (j==0):
                    triangulo[i].append(1)
                else:
                    triangulo[i].append(triangulo[i-1][j]+triangulo[i-1][j-1])
            elif (j==i):
                triangulo[i].append(1)
    print (list(triangulo))

n1 = int(input('Número de linhas do triângulo de pascal: '))

pascal(n1)