'''
04-Escreva um procedimento que receba um número arábico inteiro e imprima o corresponde número em
romano. Por exemplo, para 5 a saída desejada é “V”. A função deve ser capaz de gerar o número romano
para os 50 primeiros inteiros. Uma mensagem de erro deve ser mostrada caso um número fora dessa faixa
seja recebido. Crie também um algoritmo que leia um valor inteiro e chame o procedimento criado acima
para a impressão do número romano.
'''
def roman_uni (unid):
    numero_roman = ()
    if unid == '1':
        numero_roman = ('I')
        return numero_roman
    elif unid == '2':
        numero_roman = ('II')
        return numero_roman
    elif unid == '3':
        numero_roman = ('III')
        return numero_roman
    elif unid == '4':
        numero_roman = ('IV')
        return numero_roman  
    elif unid == '5':
        numero_roman = ('V')
        return numero_roman
    elif unid == '6':
        numero_roman = ('VI')
        return numero_roman
    elif unid == '7':
        numero_roman = ('VII')
        return numero_roman
    elif unid == '8':
        numero_roman = ('VIII')
        return numero_roman
    elif unid == '9':
        numero_roman = ('IX')
        return numero_roman
    elif unid == '0':
        numero_roman = ('')
        return numero_roman
    

def romanos(num):
    numero_romano = []
    unidades = len(num)
    if unidades > 1:
        dezena = num [:1]
        unid = num [1:]
        if dezena == '1':
            numero_romano.append('X')
            numero_romano.append(roman_uni (unid))
        elif dezena == '2':
            numero_romano.append('XX')
            numero_romano.append(roman_uni (unid))
        elif dezena == '3':
            numero_romano.append('XXX')
            numero_romano.append(roman_uni (unid))
        elif dezena == '4':
            numero_romano.append('XL')
            numero_romano.append(roman_uni (unid))
        elif dezena == '5':
            numero_romano.append('L')
            numero_romano.append(roman_uni(unid))
    else:
        numero_romano.append(roman_uni (unid))

    if unidades > 1 :
        print("".join(numero_romano))
    else:
        print(numero_romano)

    

num = int((input('Número a ser convertido para romano: ')))
if num > 50:
    print('ERRO (Somente números abaixo de 50 aceito neste programa)')
else:
    num1=str(num)
    romanos(num1)