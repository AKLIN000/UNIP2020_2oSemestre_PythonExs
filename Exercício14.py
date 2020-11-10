'''
14-Desenvolva um programa que receba nome e salário de um funcionário e calcule o valor do salário
líquido desse funcionário, utilizando função, descontando os impostos INSS e Imposto de Renda (IR)
conforme tabela oficial vigente. (utilizar laço de repetição com opção de saída do sistema).

inss:
7,5% até um salário mínimo (R$ 1.045)                              
9% para quem ganha entre R$ 1.045,01 R$ e 2.089,60                  
12% para quem ganha entre R$ 2.089,61 e R$ 3.134,40
14% para quem ganha entre R$ 3.134,41 e R$ 6.101,06.


imposto de renda:
Base de cálculo                                     Alíquota                Parcela a deduzir
	
Até R$ 22.847,76  -----------------------------      -                               -             
De R$ 22.847,77 até R$ 33.919,80 --------------      7,5%                       R$ 1.713,58
De R$ 33.919,81 até R$ 45.012,60 --------------      15%                        R$ 4.257,57
De R$ 45.012,61 até R$55.976,16 ---------------      22,5%                      R$ 7.633,51
Acima de R$ 55.976,16 ------------------------       27,5%                      R$ 10.432,32
'''
def inss (salario):#DEF DO INSS
    salario_desconto_inss:0
    if salario<=1045:
        salario_desconto_inss = salario*0.075
    elif salario >= 1045.01 and salario<=2089.60:
        salario_desconto_inss = ((salario-1045.01)*0.09)+78.38
    elif salario >= 2089.61 and salario<=3134.40:
        salario_desconto_inss = ((salario-2089.61)*0.12)+78.38+94.01
    elif salario >= 3134.41 and salario<=6101.06:
        salario_desconto_inss = ((salario-3134.41)*0.14)+78.38+94.01+125.38
    elif salario > 6101.06:
        salario_desconto_inss = ((salario-6101.06)*0.14)+78.38+94.01+125.38+415.33
    #print(f'o desconto do inss é {salario_desconto_inss} ')
    return salario_desconto_inss
def ir (salario):#DEF DO IR
    rendimento = salario*12
    deducao_simp = rendimento * 0.2
    if deducao_simp > 16754.34:
        deducao_simp = (16754.34)
    base_de_cal = rendimento-deducao_simp
    #aliquotas e parcelas a deduduzir------------------
    if base_de_cal > 55976.16:
        aliquota = 0.275
        parcelas_deduzir = 10432.32
    elif base_de_cal >= 45012.61 and base_de_cal <= 55976.16:
        aliquota = 0.225
        parcelas_deduzir = 7633.51
    elif base_de_cal >= 33919.81 and base_de_cal <= 45012.60:
        aliquota = 0.15
        parcelas_deduzir = 4257.57
    elif base_de_cal >= 22847.77 and base_de_cal <= 333919.80:
        aliquota = 0.075
        parcelas_deduzir = 1713.58
    elif base_de_cal <= 22847.76:
        aliquota=1
        parcelas_deduzir = 0
    #IMPOSTO INCIO----------------------------------
    imposto_inicial = base_de_cal * aliquota
    #IMPOSTO FINAL-----------------------------------
    imposto_final = imposto_inicial-parcelas_deduzir
    return imposto_final


while True:
    pessoa = input('nome do se humano: ')#NOME
    salario = float(input('Salário do indivíduo: '))#SALÁRIO
    print(f'o Salário com desconte do inss é :{salario - inss(salario):.2f} ')#CHAMADA DO DEF PARA INSS
    print(f'o Imposto de Renda a ser pago com base no sálario insirido é aproximadamente: {ir(salario):.2f}')
    pergunta =str.lower(input('Deseja Calcular algum outro Salário ?   '))
    if pergunta == 'n' or pergunta == 'não' or pergunta == 'nao':
        break
