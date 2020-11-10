'''
18 – Desenvolver um programa que entre com as notas (NP1 e NP2), quantidade de falta e carga horaria da
disciplina e informe se o aluno “Passou Direto”, “Exame”, “Substitutiva” ou “Reprovado”. Caso o aluno entre
com “NC” o aluno deve realizar a PSUB. Caso o aluno fique com nota insatisfatória, deve realizar um exame
e após o lançamento, o programa deve reanalisar a situação, acrescentando “Aprovado após exame” ou
“Reprovado após exame”. A regra deve ser a mesma do Manual do Aluno (vide páginas 14 e 25) disponível
no link: https://unip.br/presencial/servicos/aluno/download/calendario_manual_cursos_tradicionais1.pdf
'''
def carga_horaria (faltas): # método para saber se o aluno foi reprovado por excesso de faltas
    while True:
        aulas = float(input('Quatidade de aulas na semana da matéria referida : '))
        if aulas == 1:
            if faltas > 5:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 1.5:
            if faltas > 7:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 2:
            if faltas > 10:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 2.5:
            if faltas > 12:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 3:
            if faltas > 15:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 3.5:
            if faltas > 17:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 4:
            if faltas > 20:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 4.5:
            if faltas > 22:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 5:
            if faltas > 25:
                aprovado = False
            else:
                aprovado = True
            break
        elif aulas == 6:
            if faltas > 30:
                aprovado = False
            else:
                aprovado = True
            break
        else : 
            print('Total De aulas semanais inexistente')
    return aprovado

    if sub == 's' and np1 == 0:
        np2 = float(input('Nota da np2 : '))
        print = (f'Aluno com {np2} na primeira prova. necessita fazer a prova sub para substituir a NP1')
        substitutiva = True
        return substitutiva
    elif sub == 's' and np2 == 0:
        np1 = float(input('Nota da np1 : '))
        print = (f'Aluno com {np1} na segunda prova. necessita fazer a prova sub para substituir a NP2')
        substitutiva = True
        return substitutiva

def exames (nota):# MÉTODO PARA EXAME
    nota_doExame = float(input('Nota do Exame: '))
    media = (nota_doExame+nota)/2
    if media >=10:
        print(f'ALUNO |APROVADO| APÓS EXAME COM NOTA ATINGINDO A NOTA NECESSÁRIA (10) : media {nota}  |  exame : {nota_doExame} | TOTAL : {media}')
    else :
        print(f'ALUNO |REPROVADO| APÓS EXAME COM NOTA ATINGINDO A NOTA NECESSÁRIA (10) : media {nota}  |  exame : {nota_doExame} | TOTAL : {media}')

def subs (nota,pergunta):# MÉTODO PARA AS SUBS
    nota_sub = float(input('NOTA da SUB do Aluno : '))
    if pergunta == 1:
        media = (nota_sub+nota)/2
        if media >= 7:
            print(f'ALUNO APROVADO AO FAZER A PROVA SUBSTUTIVA COM MÉDIA : {media} ')
        else:
            print(f'ALUNO EM EXAME APÓS FAZER A PROVA SUBSTITUTIVA COM MÉDIA : {media}')
            exames(media)
    elif pergunta == 2:
        media = (nota_sub+nota)/2
        if media >= 7:
            print(f'ALUNO APROVADO AO FAZER A PROVA SUBSTUTIVA COM MÉDIA : {media}')
        else:
            print(f'ALUNO EM EXAME APÓS FAZER A PROVA SUBSTITUTIVA COM MÉDIA : {media}')
            exames(media)

# ONDE A BANDA TOCA

disciplina = input('Qual disciplina será contabilizada ?  ')
faltas = int(input('Quantidade de faltas no semestre : ')) # qutd de faltas
aprovado_porfaltas = carga_horaria(faltas)#CHAMA UM DEF PARA VERIFICAR SE O ALUNO EXCEDEU O LIMITE DE FALTAS 

if aprovado_porfaltas == True:#SE O ALUNO TIVER DENTRO DO ATURADO PARA FALTAS
    print('\nEntre com as notas')
    nc = input('CASO O ALUNO TENHA PERDIDO ALGUMA PROVA (NP1 ou NP2) DIGITE SIM  ') # pergunta para saber se o aluno está de sub
    if nc == 'sim' or nc == 'Sim' or nc == 's':#CASO O ALUNO ESTEJA DE SUB-----------------------------------
        pergunta = int(input("Qual das np's o aluno não fez ?? (digite 1  ou 2)"))
        if   pergunta == 1:
            np2 = float(input('Nota da np2 : '))
            print(f'Aluno com {np2} na primeira prova. necessita fazer a prova sub para substituir a NP1')
            subs(np2,pergunta)
        elif pergunta == 2:
            np1 = float(input('Nota da np1 : '))
            print (f'Aluno com {np1} na primeira prova. necessita fazer a prova sub para substituir a NP1')
            subs(np1,pergunta)
    else:#CASO O ALUNO NÃO ESTEJA DE SUB---------------------------------------------------------------------
        np1 = float(input('Nota da np1 : '))
        np2 = float(input('Nota da np2 : '))
        nota=(np1+np2)/2
        if nota >= 7:
            print(f'ALUNO APROVADO NA DISCIPLINA {disciplina} COM MÉDIA {nota} ')#ALUNO COM A PRESENÇA E AS NOTAS CERTINHAS
        else:
            print(f'ALUNO DE EXAME. MÉDIA {nota}')
            exames(nota)#CHAMA DEF PARA A NOTA DO EXAME

else:#CASO O ALUNO FOR REPROVADO POR FALTAS
    print('ALUNO REPROVADO POR EXCESSO DE FALTA')