"""
Desafio 001
Problema: Crie um programa que declare uma variavel "x" e atribua a ela "Hello, World!" e print na tela.
Resolução do problema:
"""
def hello_world():
    x = 'Hello, World!'
    print(x)
    return str(x)

"""
Desafio 002
Problema: Faça dois programas, um que leia o nome de uma pessoa e ou que mostre
          uma mensagem de boas-vindas.
Resolução do problema:
"""

def digite_seu_nome():
    name = str(input("Digite seu nome:"))
    return name

def seja_bem_vindo(name):
    print(f'Seja bem-vindo, {name}')
    return 'Seja bem-vindo, Mateus'

"""
Desafio 003
Problema: Crie um programa que leia dois números e mostre a soma entre eles.
Resolução do problema:
"""
def soma1 ():
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    soma = numero1 + numero2
    print('A soma entre {} e {} vale {}'.format(numero1, numero2, soma))
    return soma

"""
Desafio 004
Problema: Faça vários programas que possam ler a informação do teclado e identifique cada item asseguir: 
classe, númerico, alfabético e alfanúmerico.
Resolução do problema:
"""
def tipo_primitivo(valor):
    valor = input('Digite algo: ')
    print('O tipo primitivo desse valor é \033[31m{}\033[m'.format(type(valor)))
    return 'O tipo primitivo desse valor é {}'.format(type(valor))

def numerico(valor):
    valor = input('Digite algo: ')
    print('É um número? \033[34m{}\033[m'.format(valor.isnumeric()))
    return 'É um número? {}'.format(valor.isnumeric())

def alfabetico(valor):
    valor = input('Digite algo: ')
    print('É texto? \033[33m{}\033[m'.format(valor.isalpha()))
    return 'É texto? {}'.format(valor.isalpha())

def alfanumerico(valor):
    valor = input('Digite algo: ')
    print('É um valor alphanúmerico? \033[35m{}\033[m'.format(valor.isalnum()))
    return 'É um valor alphanúmerico? {}'.format(valor.isalnum())

"""
Desafio 005
Problema: Faça um programa que leia um número inteiro e mostre na tela
          o seu sucessor.
Resolução do problema:
"""
def sucessor(valor):
    valor = int(input('Informe um valor: '))
    sucessor = valor + 1
    print('Informado: {}\nSucessor: {}' .format(valor, sucessor))
    return sucessor

"""
Desafio 006
Problema: Crie um algoritmo que leia um número e mostre o seu drobro,
          triplo e raiz quadrada.
Resolução do problema:
"""
def operacoes(valor):
    valor = int(input('Informe um valor: '))
    dobro = valor * 2
    triplo = valor * 3
    raiz = valor ** (1 / 2)  # Também pode-se utilizar a função pow(), de sintaxe: pow(num, (1/2))
    print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(dobro, triplo, raiz))
    return dobro, triplo, raiz

"""
Desafio 007
Problema: Desenvolva um programa que leia as duas notas de um aluno,
          calcule e mostre a sua média.
Resolução do problema:
"""
def media(nota1, nota2):
    nota1 = int(input('Informe a primeira nota: '))
    nota2 = int(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    print('Média: {:.1f}'.format(media))
    return media

"""
Desafio 008
Problema: Escreva um programa que leia um valor em metros e o
          exiba convertido em centímetros e milímetros.
Resolução do problema:
"""
def conversao(metro):
    metro = int(input('Informe o valor em metro(s): '))
    centimetro = metro * 100
    milimetro = metro * 1000
    print(f'Centrimento: {centimetro}cm')
    print(f'Milimetro {milimetro}mm')
    return centimetro, milimetro

"""
Desafio 009
Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
          na carteira e mostre quantos dólares ela pode comprar.
Resolução do problema:
"""
def carteira(real):
    real = float(input('Informe seu dinheiro: R$ '))
    dolar = 5.03
    conversao_dolar = real / dolar
    print(f'Com R$ {real:.2f} você pode comprar $ {conversao_dolar:.2f}')
    return conversao_dolar


if __name__== '__main__':
    # seja_bem_vindo("Mateus")
    # soma1()
    # tipo_primitivo(valor= 'Teste')
    # numerico(valor= 'Teste')
    # alfanumerico(valor= 'Teste')
    # alfabetico(valor= 'Teste')
    # operacoes(valor= 10)
    # conversao(metro= 10)
    # carteira(real = 10.06)
    pass
