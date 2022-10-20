# Exemplo para FOR
# from time import sleep
#
"""
Desafio 051
Problema: Faça um programa que mostre na tela uma contagem regressiva
          para o estouro de fogos de artifício, indo de 10 até 0, com
          pausa de 0.2 segundo entre eles, e retorne .
Resolução do problema:
"""

# for c in range(10, -1, -1):
#     print(c)
#     sleep(0.5)
# print('FOGOOOOO!!!')

"""
Desafio 052

Problema: Refaça o desafio 009, mostrando tabuada de um
          número que o usuário escolher, só que agora
          utilizando um laço FOR.

Resolução do problema:
"""
# tabuada = int(input('Informe a tabuada que deseja ver: '))
#
# for c in range(0, 11):
#     print(f'{tabuada} X {c:2} = {tabuada*c}')
#__________________________________________________________________________

# Desafios
"""
Desafio 053

Problema: Crie um programa que leia o ano de nascimento
          de sete pessoas. No final, mostre quantas pessoas
          ainda não atingiram a maioridade e quantas já são maiores.

Resolução do problemas:
"""
# from datetime import date
#
# maioresDeIdade = 0
# menoresDeIdade = 0
# for c in range(7):
#     ano_nascimento = int(input('Informe o ano de nascimento da {}º pessoa: '.format(c + 1)))
#
#     if (date.today().year - ano_nascimento) < 21:
#         menoresDeIdade += 1
#     else:
#         maioresDeIdade += 1
# print()
# print('Tem {} pessoas menores de idade\nE {} pessoas maiores de idade.'.format(menoresDeIdade, maioresDeIdade))

"""
Desafio 054

Problema: Desenvolva um programa que leia o nome, idade e sexo
          de 4 pessoas. No final do programa,
          mostre: A média de idade do grupo.
                  Qual é o nome do homem mais velho.
                  Quantas mulheres tem menos de 20 anos.

Resolução do problemas:
"""
# idadeMedia = 0
# nomeHomemMaisVelho = ''
# idadeHomemVelho = 0
# qtdMulherMenor20 = 0
#
# for c in range(4):
#     nome = input('informe o nome da {}º pessoa: '.format(c + 1)).strip().capitalize()
#     idade = int(input('Informe a idade da {}º pessoa: '.format(c + 1)))
#     sexo = input('Informe o sexo da {}º pessoa: [M/F]'.format(c + 1)).strip().upper()
#     print()
#
#     idadeMedia += idade
#
#     if sexo == 'M':
#         if idade > idadeHomemVelho:
#             idadeHomemVelho = idade
#             nomeHomemMaisVelho = nome
#     elif sexo == 'F':
#         if idade < 20:
#             qtdMulherMenor20 += 1
#
# print('A idade média do grupo é de {} anos'.format(idadeMedia / 4))
# print('O {} é o homem mais velho do grupo, com {} anos.'.format(nomeHomemMaisVelho, idadeHomemVelho))
# print('No grupo existe {} mulher(es) com menos de 20 anos'.format(qtdMulherMenor20))



# Exemplo para WHILE
"""
Desafio 055

Problema: Faça um programa que leia o sexo de uma pessoa. Mas só aceite
          os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
          até ter um valor correto.

Resolução do problemas:
"""
# sexo = ''
# while sexo != 'M' and sexo != 'F':
#     sexo = input('Informe o sexo da pessoa [M/F]: ').strip().upper()
#     print()
#
#     if sexo != 'M' and sexo != 'F':
#         print('Sexo inválido, tente novamente.\n')
#
# if sexo == 'M':
#     print('Pessoa do sexo masculino({}) cadastrado'.format(sexo))
# else:
#     print('Pessoa do sexo feminino({}) cadastrada'.format(sexo))

# Reforçar, entrada processamento e saída
"""
Desafio 056

Problema: Melhore o jogo do desafio 028 onde o computador vai "pensar" em um
          número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
          acertar, mostrando no final quantos palpites foram necessários para vencer.

Resolução do problemas:
"""
# from random import randint
# numeroSorteado = randint(0, 10)
#
# chuteJogador = -1
# qtdTentativas = 0
#
# print('Olá, eu sou o J.A.R.V.I.S\nVamos ver se você consegue acertar essa.')
# while chuteJogador != numeroSorteado:
#     chuteJogador = int(input('\nChute um valor númerico entre 0 e 10: '))
#     if chuteJogador != numeroSorteado:
#         if chuteJogador < numeroSorteado:
#             print('Errouuu kkkk. É MAIS que isso, humano!')
#         if chuteJogador > numeroSorteado:
#             print('Errouuu kkkk. É MENOS que isso, humano!')
#
#     qtdTentativas += 1
#
# print('\nParabéns humano, você acertou o valor que escolhi.')
# print('Você tentou {} vezes até acertar.'.format(qtdTentativas))
# ___________________________________________________
# Desafio

"""
Desafio 059

Problema: Crie um programa que leia dois valores
          e mostre um menu na tela.

          -------- Menu --------
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos números
          [5] - Sair do programa
          -----------------------

          Seu programa deverá realizar a operação solicidade em cada caso.

Resolução do problemas:
# """
# menu = '''
# -------- Menu --------
# [1] - Somar
# [2] - Multiplicar
# [3] - Maior
# [4] - Novos números
# [5] - Sair do programa
# -----------------------'''
#
# priValor = int(input('Informe o primeiro valor: '))
# segValor = int(input('Informe o segundo valor: '))
#
# op = 0
# while op != 5:
#     print(menu)
#     op = int(input('Qual das opção deseja realizar: '))
#
#     if op == 1:
#         print('\nA soma de {} + {} é igual a {}'.format(priValor, segValor, priValor + segValor))
#     elif op == 2:
#         print('\nA multiplicação de {} X {} é igual a {}'.format(priValor, segValor, priValor * segValor))
#     elif op == 3:
#         print('\nO maior valor informado é {}'.format(max(priValor, segValor)))
#     elif op == 4:
#         priValor = int(input('\nInforme um novo primeiro valor: '))
#         segValor = int(input('Informe um novo segundo valor: '))
#     elif op == 5:
#         print('Finalizando. . .')
# print('\nPROGRAMA FINALIZADO.')