'''
13- Desenvolva um programa que receba nome, idade e salário digitados pelo usuário e apresente no final
quantas dessas idades estão entre 15 e 17 anos, quantas são maiores de 21 anos, quantos salários estão
entre R$1.500,00 e R$2.000,00, quantos estão acima de R$3.500,00 e qual é o maior e o menor salário
digitado. (utilizar laço de repetição com opção de saída do sistema).
'''

nomes = []
idades = []
salarios = []
while True:
    print('\nDiga-nos o nome, a idade e o salário do indivíduo\n')
    nomes.append(input('Nome: '))
    idades.append(int(input('Idade: ')))
    salarios.append(float(input('Salário: ')))
    pergunta = str.lower(input('Deseja adicionar outra pessoa ??: '))
    if pergunta == 'nao' or pergunta=='n' or pergunta=='não':
        break



idades_15e17 = []
idade_21 = []
salarios_1500e2000 = []
salarios_3500 = []


for i in idades:
    if i > 14 and i < 18:
        idades_15e17.append(i)
    elif i>21:
        idade_21.append(i)

for i in salarios:
    if i>=1500 and i<=2000:
        salarios_1500e2000.append(i)
    elif i>=3500:
        salarios_3500.append(i)
maior_salario = 0
menor_salario = 0
x = 1

for i in salarios:
    if i > maior_salario:
        maior_salario = i
    if x ==1:
        menor_salario=i
    elif i < menor_salario:
        menor_salario=i
    x=0

print(f'''nomes: {nomes}
idade: {idades}
salarios: {salarios}
idades entre 15 e 17: {len(idades_15e17)}
idades maiores que 21: {len(idade_21)}
salários entre 1.500,00 e 2.000,00 : {len(salarios_1500e2000)}
salários acima de 3.500,00 : {len(salarios_3500)}
maior salário : {maior_salario}
menor salário : {menor_salario} ''')
