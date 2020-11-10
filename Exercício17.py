'''
17-Desenvolver um programa que calcule a média aritmética simples das notas de um aluno com opção
de escolha para entrada de 2 notas, 3 notas ou 4 notas. Exiba no final o nome do aluno e sua média com a
informação: “Aprovado” se média maior ou igual a 7, “Reprovado” se média menor que 4 e “Exame” nos
demais casos. (utilizar laço de repetição com opção de saída do sistema).'''

while True:
    a = 1
    notas = []
    soma=0
    media=0
    quantidade = int(input('Com Quantas Notas Desejas Fazer a Média Do Aluno ?  '))
    for i in range (quantidade):
        notas.append(int(input(f'{a}a nota: ')))
        a+=1
    for i in notas:
        soma+=i
    media = soma/quantidade
    if media>=7:#SE APROVADO
        print(f'Aluno "Aprovado" com Média: {media}')
    elif media<7 and media>=4:#EXAME
        print(f'Aluno de "Exame" com Média: {media}') 
    elif media<4:#REPROVADO
        print(f'Aluno "Reprovado" com Média: {media}')
    pergunta = input('Deseja Calcular a Média de outro aluno??   ')
    if pergunta=='n' or pergunta=='não' or pergunta=='nao':
        break