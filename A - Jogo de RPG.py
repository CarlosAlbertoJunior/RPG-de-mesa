import random

import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep
pygame.init()

fundo = pygame.mixer.music.load('musica tema.mp3')
pygame.mixer.music.play(-1)

print('')
print('Seja bem vindo ao MUZ-AMBA, um RPG para novatos!!')

print('-=-'*10,"MUZ-AMBA",'-=-'*10)

print('Precisamos de algumas informações:')
nome = input('Qual o seu nome de JOGADOR? ')
res = nome.upper()
sleep(1)
print(f'Olá,{res}, Vamos a escolher a sua classe!')

print('-=-'*10,"MUZ-AMBA",'-=-'*10)

print('Escolha uma das opções abaixo:')
print(' [01] - Feiticeira')
print(' [02] - Guerreiro')
escolha = int(input(' Escolha:'))
if escolha == 1:
    print('Você escolheu a Feiticeira, rainha das magias ocultas, dona da noite e da lua!!')
    print('')
    print(f' A Feiticeira {nome} anda com seus 3 Guardiões Felinos, Simba o Dourado, Blue o Ofuscante e Flock o Mistico!')
    gatos = int(input(' Você gostaria de INVOCALOS? Sim [01] ou Não [02]: '))
    if gatos == 1:
        print(' INVOCANDO...')
        sleep(1)
        print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
        print('''Os Guardiões foram invocados e so querem saber de se alimentar
        Sairam na noite que se aproxima e que é refletida no colar MUZ
        Um colar poderoso que so quem domina a noite o consegue usar!''')

    print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
    print(' Nossa historia começa ao invadir o castelo abondonado de Amber, um Mago que entregou a sua vida ao protegelo')
    print(' Selando o castelo com uma magia que so com um poder acima de 15 AP consegue quebrar!')
    print('')
    sleep(2)
    magia = int(input(' Você gostaria de atacar? Sim [01] Não [02]'))
    if magia == 1:
            print(' Vamos lá, jogue os dados e mostre o seu poder!!!')
            print('')
            dados = int(input(' Qual o Valor do ataque?'))
            if dados <= 15:
                import random
                life = 50
                portal = 15
                dano = dados - portal

                print('FEITICEIRA: 50 PONTOS DE VIDA')
                print('')
                print(f' Seu ataque foi ineficais e você perdeu {dano} pontos de vida, sua vida agora é de {life+dano}/50')
                print('')
                print(' Ataque novamente, mas cuidado, você pode morrer se tomar um critico, caso contrario, qualquer ataque vence a barreira!!')
                dados1 = int(input(' Qual o valor de ataque? '))
            elif dados == random.randint(1,15):
                 print(' Você MORREU')

            elif dados >= 15:
                print('Seu ataque foi MUITO BOM e com isso conseguiu destruir a barreira. Logo a sua frente surge uma ponte que passa por cima de um rio de lava.')

            passar = int(input(' Você deseja atravessar a ponte? SIM [01] NÃO [02]: '))
            if passar == 1:
               print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
               print(' Você começa a caminhar, mas logo em seguida para ao escutar um vindo de dentro do castelo que diz:')
               sleep(2)
               print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
               sleep(2)
               print('Com isso você se prepara para atacar, pois não sabe quem está gritando e olha com um olhar profundo ao topo do castelo e diz!!')
               print(' ESTOU APENAS CHEGANDO!!!!')
               sleep(2)
               print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
               print('CONTINUA!!!!')
            elif passar == 2:
               print(' Você desiste de toda caminhada até agora, e decidir não invadir o Castelo do MAGO!')
               print(' Sua historia acabou!!!')
               sleep(1)
               print('FIM')
    elif magia == 2:
        print('Você desiste e o JOGO ACABA pra você')
    else:
        print(' Opção INVALIDA')
elif escolha == 2:
    print(f' Você escolheu o GUERREIRO {nome}, Dono das maiores terras do mundo, senhor do SOL')
    print(' E sempre bem acompanhado de sua fiel escudeira Lylla, um Cachorro que carrega em si, uma energia inexplicavel')
    print(' Capaz de atravessar o deserto sem para, com uma velocidade jamais vista')
    print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
    print(' Nossa historia começa dentro do castelo abondonado de Amber, um Mago que entregou a sua vida ao protegelo')
    print(' Selando o castelo com uma magia que so com um poder acima de 15 AP consegue quebrar!')
    sleep(2)
    print('')
    print(' Mas você é AD e nada funcionará para quebrar a barreira!')
    print('')
    print(' Ao caminhar no castelo, você encontra uma espada quebrada e ao lado uma pedra brilhante...')
    sleep(2)
    print(' É a pedra AMBA, deixada para atras em uma batalha épica contra o mago AMBER!')
    pegar = int(input(' Você gostaria de pegar a pedra? Sim [01] Não [02]: '))
    print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
    if pegar == 1:
       print(' Você se curva para coletar a pedra e ao toca-la, algo estranho acontece!!!')
       print('Uma energia toma conta do seu corpo, uma fumaça vermelha lhe cobre e uma voz sussurra ao seu ouvido')
       sleep(1)
       print('ME LIBERTE!!')
       print('')
       print('Sem entender nada, mais uma vez a voz sussurra, quebre a pedra e me liberte!!')
       pedra = int(input(' Você gostaria de quebrar a pedra? [01] SIM [02] NÃO '))
       print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
       if pedra == 1:
           print('Pego e quebro a pedra e no exato momento surge um mago, o MAGO AMBER, onde acaba te dominando e possuindo o seu corpo...')
           print(f' Triste fim para o guerreiro {res}')
           print('UM TEMPO DEPOIS...')
           sleep(3)
           print('O mago AMBER escuta um som de explosão vindo do lado de fora do castelo, e percebe que a sua barreira foi rompida')
           print('')
           print('')
           print(' Logo em seguida diz em voz alta!!!')
           print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
           print('')
           print(' E ao chegar na Janela, avista de longe, a imagem de uma Feiticeira que com um olhar profundo diz')
           print('')
           print(' ESTOU APENAS CHEGANDO!')

       elif pedra == 2:
           print(' A decisão de não quebrar a pedra, so deixa a voz que sussurra mais incomodada e com isso faz mudar de decisão')
           print(' Você volta e pega a pedra de precisa dar um dano de 10 AD para quebrar a pedra!')
           dano = int(input('Qual o valor do dano? '))
           if dano <= 10:
               pedra = 10 - dano
               vida = 50 - pedra
               print(f' Você deu {dano} de dano, e com isso levou {pedra} de dano na sua vida de {vida}/50, mas conseguiu quebrar')
               print(' a pedra e com isso libertou o espirito do mago AMBER....')
               print('')
               print(' Que no exato momento acaba possuindo o seu corpo!!')
               print('Você tenta lutar mais não consegue, tarde de mais, você foi possuido pelo mago AMBER')
               print('UM TEMPO DEPOIS...')
               sleep(3)
               print('O mago AMBER escuta um som de explosão vindo do lado de fora do castelo, e percebe que a sua barreira foi rompida')
               print('')
               print('')
               print(' Logo em seguida diz em voz alta!!!')
               print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
               print('')
               print(' E ao chegar na Janela, avista de longe, a imagem de uma Feiticeira que com um olhar profundo diz')
               print('')
               print(' ESTOU APENAS CHEGANDO!')
           elif dano >= 10:
               print(' Seu dano foi muito forte e destruiu a pedra, mas logo em seguida surge a imagem de um ancião!')
               print(' Que no exato momento vai pra cima de você')
               print('Você tenta lutar mais não consegue, tarde de mais, você foi possuido pelo mago AMBER')
               print('UM TEMPO DEPOIS...')
               sleep(3)
               print('O mago AMBER escuta um som de explosão vindo do lado de fora do castelo, e percebe que a sua barreira foi rompida')
               print('')
               print('')
               print(' Logo em seguida diz em voz alta!!!')
               print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
               print('')
               print(' E ao chegar na Janela, avista de longe, a imagem de uma Feiticeira que com um olhar profundo diz')
               print('')
               print(' ESTOU APENAS CHEGANDO!')


    elif pegar == 1:
        print('Você arremersa a pedra no chão, e com sua espada da um golpe altamente destrutivo e qubra a pedra.')
        print('Porem...')
        print('A fumaça se transforma em uma imagem de um ancião, o mago AMBER resurge e acaba possuindo o seu corpo!!')
        sleep(1)
        print('Você tenta lutar mais não consegue, tarde de mais, você foi possuido pelo mago AMBER')
        print('UM TEMPO DEPOIS...')
        sleep(3)
        print('O mago AMBER escuta um som de explosão vindo do lado de fora do castelo, e percebe que a sua barreira foi rompida')
        print('')
        print('')
        print(' Logo em seguida diz em voz alta!!!')
        print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
        print('')
        print(' E ao chegar na Janela, avista de longe, a imagem de uma Feiticeira que com um olhar profundo diz')
        print('')
        print(' ESTOU APENAS CHEGANDO!')
        sleep(3)
    elif pegar == 2:
        print(' Você se recusa, mas a sua curiosidade o acaba cedendo e volta para pegar a pedra!')
        print(' E ao pegar a pedra percebe que a algo estranho')
        print('A pedra se quebra e uma nevoa vermelha o arrodeia, um mago surge, o mago AMBER')
        print('')
        print(' E uma vez liberto, ele precisa de um corpo e é o seu, você é possuido')
        print(' Você acaba de ser possuido pelo mago AMBER')
        print('')
        print('UM TEMPO DEPOIS...')
        sleep(3)
        print('O mago AMBER escuta um som de explosão vindo do lado de fora do castelo, e percebe que a sua barreira foi rompida')
        print('')
        print(' Logo em seguida diz em voz alta!!!')
        print(' QUEM OUSA A DESTRUI A MINHA BARREIRA E INVADIR O MEU CASTELO???')
        print('')
        print(' E ao chegar na Janela, avista de longe, a imagem de uma Feiticeira que com um olhar profundo diz')
        print('')
        print(' ESTOU APENAS CHEGANDO!')
    else:
        print(' Opção Invalida, TENTE NOVAMENTE')
else:
    print(' Opção Invalida, TENTE NOVAMENTE')
print('-=-' * 10, "MUZ-AMBA", '-=-' * 10)
print(' MUZ-AMBA - Obrigado por JOGAR!!!')
sleep(2)
print('RPG Training!')

