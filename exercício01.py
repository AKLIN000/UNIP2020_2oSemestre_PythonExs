'''
01 – Desenvolva uma classe que apresente todos os números primos existentes entre N1 e N2, em que N1
e N2 são números naturais fornecidos. Um número é primo quando é divisível somente por ele e pela unidade
(1).
'''

def primos (n1,n2):
        divisores = 0
        cont = 1
        for cont in range (cont,n1+1):
            rest = n1%cont
            if rest == 0:
                divisores += 1
        if divisores == 2:
            print(n1)

n1 = int (input('escreva o número de início da contagem'))
n2 = int (input('insira o número final da contagem'))

print ('Os números primos contidos entre {} e {} são :'.format(n1,n2))

for n1 in  range (n1,n2+1):
    primos(n1,n2)