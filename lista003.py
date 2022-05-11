from random import randint
from datetime import date
"""
Desafio 020
Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.
Resolução do problema:
"""
def jogo_da_adivinhacao(maquina):
    maquina = randint(0, 5)
    chute = int(input('Adivinhe o número um número entre 0 e 5: '))
    if chute == maquina:
        print('Você ACERTOU.')
    else:
        print('Você ERROU.')
        print('O número era {}'.format(maquina))
    return maquina

"""
Desafio 021
Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.
Resolução do problema:
"""
def radar(velocidade):
    velocidade = int(input('Informe a velocidade do carro: '))
    if velocidade > 80:
        print('Você foi multado.')
        multa = (velocidade - 80) * 7.00
        print('Você vai pagar R$ {:.2f} de multa.'.format(multa))
    return velocidade > 80

"""
Desafio 022
Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
Resolução do problema:
"""
def par_impar(numero):
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        resultado = 'PAR'
        print(f'O número {numero} é PAR.')
    else:
        resultado = 'IMPAR'
        print(f'O número {numero} é IMPAR.')
    return resultado

"""
Desafio 023
Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 parta
          viagens mais longas.
Resolução do problema:
"""
def passagem(distancia):
    distancia = int(input('Informe a distância em KM: '))
    if distancia > 200:
        preco_passagem = distancia * 0.45
    else:
        preco_passagem = distancia * 0.5
    print('O valor da passagem será R$ {:.2f}'.format(preco_passagem))
    return preco_passagem

"""
Desafio 024
Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Resolução do problema:
"""
def ano_bissexto(ano):
    ano = int(input('Informe o ano: '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        resultado = 'BISSEXTO'
        print(f'O ano de {ano} é BISSEXTO.')
    else:
        resultado = 'NÃO é BISSEXTO'
        print(f'O ano de {ano} NÃO é BISSEXTO.')
    return resultado
"""
Desafio 025
Problema: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
Resolução do problema:
"""
def maior_menor(num1, num2, num3):
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    num3 = int(input('Informe o terceiro número: '))
    maior = num1
    menor = num1
    # Maior
    if num2 > num1 and num2 > num3:
        maior = num2
    if num3 > num1 and num3 > num2:
        maior = num3
    # Menor
    if num2 < num1 and num2 < num3:
        menor = num2
    if num3 < num1 and num3 < num2:
        menor = num3
    print('O número {} é o MAIOR'.format(maior))
    print('O número {} é o MENOR'.format(menor))
    return (maior, menor)

if __name__ == '__main__':
    # jogo_da_adivinhacao(maquina = randint(0, 5))
    # radar(velocidade= 95)
    # par_impar(numero=10)
    # passagem(distancia=450)
    # ano_bissexto(ano=2024)
    maior_menor(num1=15, num2=20, num3=5)
    pass