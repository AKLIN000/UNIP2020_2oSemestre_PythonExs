'''
15-– Elabore um programa que receba dois números (tipo float) digitados pelo usuário e pergunte qual
operação ele deseja realizar. Operações possíveis: soma, subtração, multiplicação, divisão, maior e menor
número. Exiba no final os números digitados e o resultado da operação escolhida.'''

def operaracoes (numero1, numero2, op): #DEF PARA AS OPERAÇÕES
    devolve = 0
    print(f'O números digitados foram {numero1} e {numero2}')
    if op == 1:
        devolve=numero1+numero2
        print(f'A Soma dos números é {devolve}')
    elif op == 2:
        devolve = numero1-numero2
        print(f'A Subtração dos números é {devolve}')
    elif op == 3:
        devolve = numero1*numero2
        print(f'A Multiplicação dos números é {devolve}')
    elif op == 4:
        if numero2!=0:
            devolve = numero1/numero2
            print(f'A Divisão dos núemros é {devolve}')
        else:
            print('Divisão com 0 não existente.')
    elif op == 5:
        if numero1 > numero2:
            print (f'O maior entre os Dois é {numero1} e o menor é {numero2} ')
        else:
            print (f'O maior entre os Dois é {numero2} e o menor é {numero1} ')

while True:
    numero1 = float(input('Insira o número para a operação:'))
    numero2 = float(input('Insira o 2o número para a operação:'))
    op = int(input('''Qual operção desejas fazer ??

    digite [1 para soma]
    digite [2 para subtração]
    digite [3 para multiplicação]
    digite [4 para divisão]
    ou digite [5 se desejas saber qual é o maior e o menor número]
    
    '''))
    
    operaracoes(numero1,numero2,op)

    pergunta = input('\nVocê quer repetir com outros números??  ')

    if pergunta == 'n' or pergunta == 'não' or pergunta=='nao':
        break