'''
05-Preencher por leitura uma matriz M (5,5). Em seguida, calcular e imprimir a matriz toda e a média dos
elementos das áreas assinaladas abaixo:'''
matriza = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range (5):
    for j in range (5):
        x = int(input(f'inserira um número para a linha {i} coluna {j} : '))
        matriza[i][j]=(x)
        x+=1
print(f'A matriz é a seguinte: \n')

for i in range (5):
    for j in range (5):
        print(f'[{matriza[i][j]:^8}]', end='')
    print()

soma = 0

for i in range (5):
    for j in range (5):
        if i-j == 1 and j != 0:
            soma+=matriza[i][j]
            matriza[i][j]
            print(f'[{matriza[i][j]:^8}]', end='')
        elif i-j == 2 and j !=0:
            soma+=matriza[i][j]
            print(f'[{matriza[i][j]:^8}]', end='')
        elif i-j == 3 and j !=0:
            soma+=matriza[i][j]
            print(f'[{matriza[i][j]:^8}]', end='')
    print()

print('\n')
print(f'A soma dos termos requeridos é : {soma}')

    