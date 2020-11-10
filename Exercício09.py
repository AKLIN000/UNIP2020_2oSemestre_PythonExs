'''
09-– Faça uma função que recebe um valor inteiro e verifica se o valor é positivo, negativo ou zero. A função
deve retornar 1 para valores positivos, ‐1 para negativos e 0 para o valor 0.'''

def valor (x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0

x = int(input('Insira um Número para verificar se é negativo ou positivo: '))



if valor(x) == 0:
    print('valor neutro (0)')
elif valor(x) == 1:
    print('valor negativo')
elif valor(x) == -1:
    print('valor positivo')