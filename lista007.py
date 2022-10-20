# Exemplos para IF / ELSE


"""
Desafio 047

Problema: Escreva um programa para aprovar o empréstimo bancário para a
          compra de uma casa. Pergunte o valor da casa, o salário do comprador
          e em quantos anos ele vai pagar. A prestação mensal não pode exceder
          30% do salário ou então o empréstimo será negado.

Resolução do problema:
"""
# valor_casa = float(input('Informe o valor da casa: R$'))
# salario_comprador = float(input('Informe o sálario do comprador: R$'))
# quantidade_anos = int(input('Anos de financiamento: '))
#
# prestacao = valor_casa / (quantidade_anos * 12)
#
# if prestacao < salario_comprador * 30 / 100:
#     print('FINANCIAMENTO ACEITO!!!\nA prestação será de R${:.2f}/Mês durante {} Anos.'.format(prestacao, quantidade_anos))
# else:
#     print('FINANCIAMENTO NEGADO!!!\nSALÁRIO INSUFICIENTE.')


"""
Desafio 048

Problema: Escreva um programa que leia dois números inteiros e compare-os.
          mostrando na tela uma mensagem:
            - O primeiro valor é maior
            - O segundo valor é maior
            - Não existe valor maior, os dois são iguais

Resolução do problema:
"""
# numero_1 = int(input('Informe o primeiro número: '))
# numero_2 = int(input('Informe o segundo número: '))
#
# if numero_1 > numero_2:
#     print('O PRIMEIRO número é MAIOR.')
# elif numero_1 < numero_2:
#     print('O SEGUNDO numero é MAIOR.')
# else:
#     print('Não existe maior, os dois são IGUAIS.')

# DESAFIOS:

"""
Desafio 049

Problema: Desenvolva uma lógica que leia o peso e a altura de
          uma pessoa, calcule seu Índice de Massa Corporal (IMC)
          e mostre seu status, de acordo com a tabela abaixo:
            - IMC abaixo de 18,5: Abaixo do Peso
            - Entre 18,5 e 25: Peso Ideal
            - 25 até 30: Sobrepeso
            - 30 até 40: Obesidade
            - Acima de 40: Obesidade Mórbida

Resolução do problema:
"""
# peso = float(input('Informe seu peso: (kg)'))
# altura = float(input('Informe sua altura: (m)'))
#
# imc = peso / altura ** 2
# print('Seu IMC é {:.1f}'.format(imc))
# if 0 < imc < 18.5:
#     print('Abaixo do peso.')
# elif 18.5 <= imc < 25:
#     print('Peso ideal.')
# elif 25 <= imc < 30:
#     print('Sobrepeso')
# elif 30 <= imc < 40:
#     print('Obesidade')
# elif imc >= 40:
#     print('Obesidade Mórbida')

"""
Desafio 050

Problema: Crie um programa que faça o computador jogar Jokenpô com você.

Resolução do problema:
"""
from random import randint  # Importanda da Lib random o modulo randint
lista_jogada = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)  # Sorteando número de 0 a 2

# Solicitando um valor e subtraindo 1 dele
jogador = int(input('[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura \nEscolha uma opção: ')) - 1

# Verificação da situação do jogo, ganhador/empate
if 0 <= jogador < 3:
    # 1 = Pedra; 2 = Papel; 3 = Tesoura
    print('Você \033[34m{}\033[m X \033[31m{}\033[m Computador'.format(lista_jogada[jogador], lista_jogada[computador]))

    #Empate
    if jogador == computador:
        print('\033[30mJOGO EMPATADO')

    # Jogador escolhendo Pedra
    elif jogador == 0 and computador == 1:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 0 and computador == 2:
        print('\033[30mVOCÊ GANHOU')

    # Jogador Escolhendo Papel
    elif jogador == 1 and computador == 2:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 1 and computador == 0:
        print('\033[30mVOCÊ GANHOU')

    # Jogador Escolhendo Tesoura
    elif jogador == 2 and computador == 0:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 2 and computador == 1:
        print('\033[30mVOCÊ GANHOU')
else:
    print('\033[30;41mJOGADA INVALIDA, TENTE NOVAMENTE.\033[m')
