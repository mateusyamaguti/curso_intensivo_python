#Ensinar modulo
from math import floor
from math import hypot
from math import radians, sin, cos, tan
from random import choice

"""
Desafio 010
Problema: Crie um programa que leia um número Real qualquer
          pelo teclado e mostre na tela a sua porção Inteira.
Resolução do problema:
"""

def parte_inteira(num):
    # num = float(input('Informe um número flutuante: '))
    # print(math.trunc(num))  # Metodo floor() tem o mesmo resultado
    # return math.trunc(num)
    num = float(input('informe um número flutuante: '))
    return floor(num)

"""
Desafio 011
Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.
Resolução do problema:
"""
def hipotenusa(cateto_oposto, cateto_adjacente):
    cateto_oposto = int(input('Informe o cateto oposto: '))
    cateto_adjacente = int(input('Informe o cateto adjacente: '))
    valor_hipotenusa = hypot(cateto_oposto, cateto_adjacente)  # H² = C² + C² // H² = (C² + C²) ** (1/2)
    print('Hipotenusa: {:.2f}'.format(valor_hipotenusa))
    return valor_hipotenusa

"""
Desafio 012
Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.
Resolução do problema:
"""
def converte_angulo(angulo):
    angulo = int(input('Informe o angulo: '))
    ang_radiano = radians(angulo)
    seno = sin(ang_radiano)
    cosseno = cos(ang_radiano)
    tangente = tan(ang_radiano)
    print('Seno: {:.4f}'.format(seno))
    print('Cosseno: {:.4f}'.format(cosseno))
    print('Tangente: {:.4f}'.format(tangente))
    return seno, cosseno, tangente

"""
Desafio 013
Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.
Resolução do problema:
"""
def escolha_alunos(nome1, nome2, nome3, nome4):
    nome1 = input('1º aluno(a): ')
    nome2 = input('2º aluno(a): ')
    nome3 = input('3º aluno(a): ')
    nome4 = input('4º aluno(a): ')
    escolhido = choice([nome1, nome2, nome3, nome4])
    print('O aluno escolhido foi: ', escolhido)
    return escolhido

"""Desafio 014
Problema: Crie um programa que leia o nome completo de uma pessoa e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.
Resolução do problema:
"""
def nome_atributos(nome):
    nome = str(input('Informe seu nome completo: ')).split()
    print('Nome Maíusculo: ', ' '.join(nome).upper())
    print('Nome minúsculo: ', ' '.join(nome).lower())
    print('Quantas letras que o nome possue sem espaços: ', len(''.join(nome)))
    print('Quantas letras tem o primeiro nome: ', len(nome[0]))
    return (' '.join(nome).upper(), ' '.join(nome).lower(), len(''.join(nome)), len(nome[0]))

"""
Desafio 015
Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Resolução do problema:
"""
def grandezas(numero):
    numero = int(input('Informe o número: '))
    uni = numero // 1 % 10
    de = numero // 10 % 10
    ce = numero // 100 % 10
    mi = numero // 1000 % 10
    print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(uni, de, ce, mi))
    return (uni, de, ce, mi)

"""
Desafio 016
Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
Resolução do problema:
"""
def procura_cidade(cidade):
    nome = input('Cidade: ').strip().split()
    print('O nome da cidade digitada começa com "SANTO": ', 'SANTO' in nome[0].upper())
    return ('SANTO' in nome[0].upper())

"""
Desafio 017
Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
Resolução do problema:
"""
def procura_nome(nome):
    nome = input('Nome: ').strip()
    print('Tem "SILVA" no seu nome: ', 'SILVA' in nome.upper())
    return ('SILVA' in nome.upper())

"""
Desafio 018
Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.
Resolução do problema:
"""
def ler_letra_a(frase):
    frase = input('Digite uma frase: ').strip()
    contar = frase.upper().count('A')
    pos_in = frase.upper().find('A')
    pos_fin = frase.upper().rfind('A')
    print(f'Quantas vezes a letra "A" apareceu: {contar}')
    print(f'Ela aparece a primeira vez na posição: {pos_in}')
    print(f'Ela aparece a ultima vez na posição: {pos_fin}')
    return (contar, pos_in, pos_fin)

"""
Desafio 019
Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.
Resolução do problema:
"""
def nome_in_fim(nome):
    nome = input('Informe seu nome: ').strip().split()
    print('Primeiro {} \nUltimo: {}'.format(nome[0], nome[-1]))
    return (nome[0], nome[-1])


if __name__ == '__main__':
    # parte_inteira(num=10)
    # hipotenusa(cateto_oposto=4,cateto_adjacente=3)
    # converte_angulo(angulo=10)
    # escolha_alunos(nome1 = 'Mateus', nome2 = 'Francisco', nome3 = 'Jose', nome4 = 'Maria')
    # nome_atributos(nome= 'Mateus Xavier Yamaguti')
    # grandezas(numero= 1956)
    # procura_cidade(cidade= 'Santo Amaro')
    # procura_nome(nome= 'Edson Arantes da Silva')
    # ler_letra_a('A aranha arranha a jarra')
    pass

