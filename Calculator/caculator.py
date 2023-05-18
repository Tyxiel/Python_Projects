import math
import time


# Main code

def main():
    while True:
        print('''
        =-=-=-=-=-=-=-=
          Calculadora
        =-=-=-=-=-=-=-=
        ''')
        time.sleep(1)
        print('O que você deseja calcular?')
        time.sleep(0.3)
        print('[1] Soma')
        time.sleep(0.3)
        print('[2] Subtração')
        time.sleep(0.3)
        print('[3] Multiplicação')
        time.sleep(0.3)
        print('[4] Divisão')
        time.sleep(0.3)
        print('[5] Exponênciação')
        time.sleep(0.3)
        print('[6] Raiz Quadrada')
        time.sleep(0.3)
        choice = int(input('R: '))

        # Verifica se foi inserido um número válido

        if choice in (1, 2, 3, 4, 5, 6):

            # Soma

            if choice == 1:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão somados? '))
                if choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                # Soma depois da verificação da quantidade de números

                if choice_numb == 2:
                    result = num1 + num2
                    print('{:,} + {:,} = {:,}'.format(num1, num2, result).replace(',', '.'))
                elif choice_numb == 3:
                    result = (num1 + num2) + num3
                    print('{:,} + {:,} + {:,} = {:,}'.format(num1, num2, num3, result).replace(',', '.'))
                elif choice_numb == 4:
                    result = ((num1 + num2) + num3) + num4
                    print('{:,} + {:,} + {:,} + {:,} = {:,}'.format(num1, num2, num3, num4, result).replace(',', '.'))

            # Subtração

            elif choice == 2:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão subtraidos? '))
                if choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                    # Subtração depois da verificação da quantidade de números

                if choice_numb == 2:
                    result = num1 - num2
                    print('{:,} - {:,} = {:,}'.format(num1, num2, result).replace(',', '.'))
                elif choice_numb == 3:
                    result = (num1 - num2) - num3
                    print('{:,} - {:,} - {:,} = {:,}'.format(num1, num2, num3, result).replace(',', '.'))
                elif choice_numb == 4:
                    result = ((num1 - num2) + num3) + num4
                    print('{:,} - {:,} - {:,} - {:,} = {:,}'.format(num1, num2, num3, num4, result).replace(',', '.'))

            # Multiplicação

            elif choice == 3:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão multiplicados? '))
                if choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                # Multiplicação depois da verificação da quantidade de números

                if choice_numb == 2:
                    result = num1 * num2
                    print('{:,} * {:,} = {:,}'.format(num1, num2, result).replace(',', '.'))
                elif choice_numb == 3:
                    result = (num1 * num2) * num3
                    print('{:,} * {:,} * {:,} = {:,}'.format(num1, num2, num3, result).replace(',', '.'))
                elif choice_numb == 4:
                    result = ((num1 * num2) * num3) * num4
                    print('{:,} * {:,} * {:,} * {:,} = {:,}'.format(num1, num2, num3, num4, result).replace(',', '.'))

            elif choice == 4:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão divididos? '))
                if choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                # Division depois da verificação da quantidade de números

                if choice_numb == 2:
                    result = num1 / num2
                    print('{:,} * {:,} = {:,}'.format(num1, num2, result).replace(',', '.'))
                elif choice_numb == 3:
                    result = (num1 / num2) / num3
                    print('({:,} / {:,}) / {:,} = {:,}'.format(num1, num2, num3, result).replace(',', '.'))
                elif choice_numb == 4:
                    result = ((num1 / num2) / num3) / num4
                    print('[({:,} / {:,}) / {:,}] / {:,} = {'.format(num1, num2, num3, num4, result).replace(',', '.'))

            elif choice == 5:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão potencializados? '))
                if choice_numb == 1:
                    num1 = float(input('Primeiro número: '))
                    exp_num = int(input('Em quantas vezes?'))
                elif choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    exp_num = int(input('Em quantas vezes?'))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    exp_num = int(input('Em quantas vezes?'))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                    exp_num = int(input('Em quantas vezes?'))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                # Potência depois da verificação da quantidade de números

                if choice_numb == 1:
                    result = num1 ** exp_num
                    print('{:,} ** {:,} = {:,}'.format(num1, exp_num, result).replace(',', '.'))
                elif choice_numb == 2:
                    result = num1 ** exp_num
                    result_2 = num2 ** exp_num
                    print('{:,} ** {:,} = {:,}'.format(num1, exp_num, result).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num2, exp_num, result_2).replace(',', '.'))
                elif choice_numb == 3:
                    result = num1 ** exp_num
                    result_2 = num2 ** exp_num
                    result_3 = num3 ** exp_num
                    print('{:,} ** {:,} = {:,}'.format(num1, exp_num, result).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num2, exp_num, result_2).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num3, exp_num, result_3).replace(',', '.'))
                elif choice_numb == 4:
                    result = num1 ** exp_num
                    result_2 = num2 ** exp_num
                    result_3 = num3 ** exp_num
                    result_4 = num3 ** exp_num
                    print('{:,} ** {:,} = {:,}'.format(num1, exp_num, result).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num2, exp_num, result_2).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num3, exp_num, result_3).replace(',', '.'))
                    print('{:,} ** {:,} = {:,}'.format(num1, exp_num, result_4).replace(',', '.'))

            # Raiz Quadrada

            elif choice == 6:

                # Pergunta quantos números serão utilizados

                choice_numb = int(input('Quantos números serão tirados a raíz quadrada? '))
                if choice_numb == 1:
                    num1 = float(input('Primeiro número: '))
                elif choice_numb == 2:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                elif choice_numb == 3:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                elif choice_numb == 4:
                    num1 = float(input('Primeiro número: '))
                    num2 = float(input('Segundo número: '))
                    num3 = float(input('Terceiro número: '))
                    num4 = float(input('Quarto número: '))
                else:
                    print('Escolha um número entre 1 e 4. Tente novamente')
                    continue

                # Raiz quadrada depois da verificação da quantidade de números

                if choice_numb == 1:
                    result = math.sqrt(num1)
                    print('_/{:,} = {:,}'.format(num1, result).replace(',', '.'))
                elif choice_numb == 2:
                    result = math.sqrt(num1)
                    result_2 = math.sqrt(num2)
                    print('_/{:,} = {:,}'.format(num1, result).replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num2, result_2).replace(',', '.'))
                elif choice_numb == 3:
                    result = math.sqrt(num1)
                    result_2 = math.sqrt(num2)
                    result_3 = math.sqrt(num3)
                    print('_/{:,} = {:,}'.format(num1, result).replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num2, result_2) .replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num3, result_3).replace(',', '.'))
                elif choice_numb == 4:
                    result = math.sqrt(num1)
                    result_2 = math.sqrt(num2)
                    result_3 = math.sqrt(num3)
                    result_4 = math.sqrt(num4)
                    print('_/{:,} = {:,}'.format(num1, result).replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num2, result_2).replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num3, result_3).replace(',', '.'))
                    print('_/{:,} = {:,}'.format(num4, result_4).replace(',', '.'))

        else:
            print('Escolha uma das seis possibilidades de calculo disponível! Tente novamente')
            continue


main()
