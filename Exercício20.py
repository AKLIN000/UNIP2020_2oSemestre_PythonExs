'''
20– Desenvolva um programa que receba 10 valores de temperatura ambiente de uma cidade. O programa
deve armazenar tais valores em uma lista denominada temp, conforme os valores vão sendo recebidos. Após
isso, o programa deve retornar a média de temperatura, temperatura máxima, temperatura mínima e por
fim criar uma segunda lista (chamada dados) e por os valores em ordem crescente.
'''

temp = []
x = 1
soma = 0
media = 0
for i in range(10):
    temp.append(float(input(f'{x}a Temperatura :')))
    x+=1
for i in temp:
    soma+=i
media = soma/10
temp.sort()
print(f'a Média de Temperatura da cidade é {media} a temperatura mínima é {min(temp)} e a máxima {max(temp)} ')
print(f'e Por fim a Lista em Ordem Crescente : {temp}')
