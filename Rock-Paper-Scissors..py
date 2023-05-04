import time
import random

# Pergunta

while True:
    print('''
    =-=-=-=-=-=-=-=
        \033[1;37mJokenpô\033[m
    =-=-=-=-=-=-=-=''')
    time.sleep(0.5)
    print('Escolha o que jogar!')
    time.sleep(1)
    print('[1] Pedra')
    time.sleep(0.5)
    print('[2] Papel')
    time.sleep(0.5)
    print('[3] Tesoura')
    time.sleep(0.5)

    plyr = int(input('R: '))
    pc = random.randrange(1, 4)

    # Condições Player

    if plyr == 1:
        time.sleep(0.5)
        print('Você jogou\033[1;37m PEDRA\033[m!')
    elif plyr == 2:
        time.sleep(0.5)
        print('Você jogou\033[1;34m PAPEL\033[m')
    elif plyr == 3:
        time.sleep(0.5)
        print('Você jogou\033[1;35m TESOURA\033[m')

    # Condições Máquina

    if pc == 1:
        time.sleep(0.5)
        print('A máquina jogou\033[1;37m PEDRA\033[m!')
    elif pc == 2:
        time.sleep(0.5)
        print('A máquina jogou\033[1;34m PAPEL\033[m')
    elif pc == 3:
        time.sleep(0.5)
        print('A máquina jogou\033[1;35m TESOURA\033[m')

    # Condições Jogo

    if plyr == pc:
        print('\033[1;33mEMPATE!\033[m')

    # Vitórias

    elif plyr == 1 and pc == 3:
        time.sleep(0.5)
        print('\033[1;32mVITÓRIA!\033[m')
    elif plyr == 2 and pc == 1:
        time.sleep(0.5)
        print('\033[1;32mVITÓRIA!\033[m')
    elif plyr == 3 and pc == 2:
        time.sleep(0.5)
        print('\033[1;32mVITÓRIA!\033[m')

    # Derrotas

    elif plyr == 1 and pc == 2:
        time.sleep(0.5)
        print('\033[1;31mDERROTA!\033[m')
    elif plyr == 2 and pc == 3:
        time.sleep(0.5)
        print('\033[1;31mDERROTA!\033[m')
    elif plyr == 3 and pc == 1:
        time.sleep(0.5)
        print('\033[1;31mDERROTA!\033[m')
