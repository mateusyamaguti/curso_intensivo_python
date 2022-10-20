from lista002 import parte_inteira
from lista002 import hipotenusa
from lista002 import converte_angulo
from lista002 import escolha_alunos
from lista002 import nome_atributos
from lista002 import grandezas
from lista002 import procura_cidade
from lista002 import procura_nome
from lista002 import ler_letra_a
from lista002 import nome_in_fim
from random import choice

import pytest

def test_parte_inteira(monkeypatch):
    num = 3.14
    answers = iter([num])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert parte_inteira(num) == 3

def test_hipotenusa(monkeypatch):
    cateto_oposto = 3
    cateto_adjacente = 4
    answers = iter([cateto_oposto, cateto_adjacente])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert hipotenusa(cateto_oposto, cateto_adjacente) == 5.00

def test_converter_angulo(monkeypatch):
    angulo = 0
    answers = iter([angulo])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert converte_angulo(angulo) == (0, 1, 0)

def test_escolha_alunos1(monkeypatch):
    nome1 = 'Mateus'
    nome2 = 'Francisco'
    nome3 = 'Jose'
    nome4 = 'Maria'
    answers = iter([nome1, nome2, nome3, nome4])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert isinstance(escolha_alunos(nome1, nome2, nome3, nome4), str)

def test_escolha_alunos2(monkeypatch):
    nome1 = 'Mateus'
    nome2 = 'Francisco'
    nome3 = 'Jose'
    nome4 = 'Maria'
    answers = iter([nome1, nome2, nome3, nome4])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    retorno = choice([nome1, nome2, nome3, nome4])
    assert retorno in [nome1, nome2, nome3, nome4]

def test_nome_atributos(monkeypatch):
    nome = 'Mateus Xavier Yamaguti'
    answers = iter([nome])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert isinstance(nome, str)
    assert nome_atributos(nome) == ('MATEUS XAVIER YAMAGUTI', 'mateus xavier yamaguti', 20, 6)

def test_nome_atributos1(monkeypatch):
    nome = 'Mateus Xavier Yamaguti'
    answers = iter([nome])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    retorno = nome_atributos(nome)
    assert retorno[0] == 'MATEUS XAVIER YAMAGUTI'
    assert retorno[1] == 'mateus xavier yamaguti'
    assert retorno[2] == 20
    assert retorno[3] == 6

def test_grandezas(monkeypatch):
    numero = 1956
    answers = iter([numero])
    monkeypatch.setattr('builtins.input', lambda numbers: next(answers))
    assert grandezas(numero) == (6, 5, 9, 1)

def test_procura_cidade(monkeypatch):
    cidade = 'Santo Amaro'
    answers = iter([cidade])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert procura_cidade(cidade) == True

def test_procura_nome(monkeypatch):
    nome = 'Edson Arantes da Silva'
    answers = iter([nome])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert procura_nome(nome) == True

def test_ler_letra_a(monkeypatch):
    frase = 'A aranha arranha a jarra'
    answers = iter([frase])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert ler_letra_a(frase) == (10, 0, 23)

def test_nome_in_fim(monkeypatch):
    nome = 'Edson Arantes da Silva'
    answers = iter([nome])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert nome_in_fim(nome) == ('Edson', 'Silva')
