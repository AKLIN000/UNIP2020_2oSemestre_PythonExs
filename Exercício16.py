'''
16-Elabore um programa que faça a conversão de moedas. O programa deve receber uma quantidade em
determinada moeda e a taxa de conversão e apresentar a quantidade convertida na moeda selecionada.
Conversões possíveis: dólar para real, euro para real, real para dólar e real para euro. (utilizar laço de
repetição com opção de saída do sistema).

real em dolar = 0,18
dolar real = 5,16
euro para real = 6,67
real para euro = 0,15
'''
def conversor(qual,valor):
    convertido = 0
    if qual == 1:
        convertido = valor*0.18
    if qual == 2:
        convertido = valor*5.16
    if qual == 3:
        convertido = valor*6.67
    if qual == 4:
        convertido = valor*0.15
    return convertido

while True:
    qual = int(input('''
     ______________________
    | Real para Dólar [1]  |
    | Dólar para real [2]  |
    | Euro Para Real  [3]  |
    | Real para Euro  [4]  |
     s----------------------
    Qual conversão Vocé deseja fazer ?''')) #DECISÃO DE QUAL A CONVERSÃO COM UMA PEQUENA TABELA
    valor = float(input('Valor a ser convertido: '))
    print(f'O Valor convertido é {conversor(qual, valor)} ')
    pergunta=str.lower(input('Deseja Fazer outra conversão ? '))
    if pergunta == 'não' or pergunta =='n'or pergunta=='nao':
        break
