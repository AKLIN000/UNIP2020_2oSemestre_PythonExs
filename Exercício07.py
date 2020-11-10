'''
07-Escrever um algoritmo que lê um par de coordenadas (x,y) inteiras e imprima uma mensagem
informando em qual quadrante está o ponto. O algoritmo deve também ser capaz de identificar se o ponto
está sobre um dos eixos ou no ponto central.
'''

while True:
    x = float(input('Coordenada do eixo x : '))
    y = float(input('Coordenada do eixo Y : '))
    if x>0 and y>0:
        print('O ponto está localizado no 1o quadrante do Plano')
    elif x<0 and y>0:
        print('O ponto está localizado no 2o quadrante do Plano')
    elif x<0 and y<0 :
        print('O ponto está localizado no 3o quadrante do Plano')
    elif x>0 and y<0 :
        print('O ponto está localizado no 4o quadrante do Plano')
    elif x==0 and y==0:
        print('O ponto está localizado no ponto central do Plano')
    elif x == 0 and y>0 :
        print('O ponto está localizado no eixo y do Plano')
    else:
        print('O ponto está localizado no eixo x do Plano')
    
    print()

    pergunta = str.lower(input('Deseja saber o qaudrante de outro ponto??'))
    if pergunta == 'não' or pergunta == 'n' or pergunta == 'nao':
        break