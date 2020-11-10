'''
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia
todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final
diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o
campeão). O campeão é o que tem a menor média de tempos.
'''

#LEMBRAR DE TROCAR OS VALORES DEPOIS
corredores = {} #ESSE DIC GUARDARÁ OS NOMES E 'TODOS' OS TEMPOS (pedido no enunciado)
corredores_e_melhores_tempos = {} # ESSE DIC GUARDARA OS NOMES E OS 'MELHORES' TEMPOS 
corredores_tempos_media = [] # AS MEDIAS PARA VER QUAL A MELHOR PARA DEPOIS FAZER A ORDENAÇÃO
tempo_convertido = [] # TEMPOS CONVERTIDOS PARA STR PARA USAR COMO CHAVE
corredores_nomes = [] # NOMES ADD AQUI PARA DEPOIS FAZER LIGAÇÃO COM OS TEMPOS // (TUDO PQ NÃO CONSEGUI ACHAR UMA FORMA DE ENCONTRAR O INDEX DE DETERMINADO VALOR :/ )
corredor = 1

for cont in range (6): # IN RANGE DO TAMANHO DA QTD DE CORREDORES
    
    nome = input(f'Nome do {corredor}o(a) corredor(a) ')
    tempos = [] # LISTA QUE ADD TODAS AS VOLTAS DO CORREDOR (SERÁ ADD NO DIC 'corredores')
    volta = 1
    somas = 0
    for i in range (10): # IN RANGE (DENTRO DO OUTRO) DO TAMANHO DA QTD DE VOLTAS
        tempo=(float(input(f'tempo da {volta}a volta (em segundos) :')))
        tempos.append(tempo)
        volta+=1
        somas+=tempo
    
    corredores[nome]=tempos # ADD O NOME E OS TEMPOS
    corredores_tempos_media.append(somas/10) # MÉDIA
    corredores_nomes.append(nome)
    corredor+=1
    

for i in corredores_tempos_media : #FOR PARA CONVERTER OS NUMBERS
        tempo_convertido.append(str(i))

x = 0 #vaviável para os indexs dos nomes

for i in tempo_convertido: #FOR PARA O OUTRO DIC. ONDE AS CHAVES SÃO OS TEMPOS
    corredores_e_melhores_tempos [i] = corredores_nomes[x]
    x+=1

corredores_tempos_media.sort()
print(corredores_tempos_media, 'PARA VER SE ESTÁ ORDENADO')

tempo_convertido_ord = [] # ARGHHHHHHHHH

for i in corredores_tempos_media : #FOR PARA CONVERTER OS NUMBERS DE NOVOoOoOOoOOoooOooO aff!!
        tempo_convertido_ord.append(str(i))

primeiro   = tempo_convertido_ord[0] # CHAVE PARA O NOME
segundo    = tempo_convertido_ord[1]
terceiro   = tempo_convertido_ord[2]
primeiro_t = corredores_tempos_media[0]#TEMPOS
segundo_t = corredores_tempos_media[1]
terceiro_t = corredores_tempos_media[2]
print(f'''
O primero colado foi {corredores_e_melhores_tempos.get(primeiro)} com {primeiro_t}s
O Segundo colocado foi {corredores_e_melhores_tempos.get(segundo)} com {segundo_t}s
P Terceiro colocado foi {corredores_e_melhores_tempos.get(terceiro)} com {terceiro_t}s 
''')

