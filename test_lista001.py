from lista001 import hello_world
from lista001 import digite_seu_nome
from lista001 import seja_bem_vindo
from lista001 import soma1
from lista001 import tipo_primitivo
from lista001 import numerico
from lista001 import alfabetico
from lista001 import alfanumerico
from lista001 import sucessor
from lista001 import operacoes
from lista001 import media
from lista001 import conversao
from lista001 import carteira

import pytest


def test_hello_world():
    assert isinstance(hello_world(), str)
    assert len(hello_world()) == 13
    assert hello_world().split(" ")[0][0] == "H"
    assert hello_world().split(" ")[1][0] == "W"

def test_digite_seu_nome(monkeypatch):
    # provided inputs
    name = 'Mateus'
    # creating iterator object
    answers = iter([name])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert digite_seu_nome() == name

def test_seja_bem_vindo(monkeypatch):
    name = 'Mateus'
    answers = iter([name])
    monkeypatch.setattr('builtins.input', lambda name: (answers))
    assert seja_bem_vindo(name) == 'Seja bem-vindo, Mateus'

def test_soma1(monkeypatch):
    numero1 = 3
    numero2 = 4
    answers = iter([str(numero1), str(numero2)])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert soma1() == 7
    assert isinstance(numero1 and numero2, int)

def test_tipo_primitivo(monkeypatch):
    valor = 'Teste'
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert tipo_primitivo(valor) == "O tipo primitivo desse valor é <class 'str'>"

def test_numerico(monkeypatch):
    valor = 'Teste'
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert numerico(valor) == 'É um número? False'

def test_alfabetico(monkeypatch):
    valor = 'Teste'
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert alfabetico(valor) == 'É texto? True'

def test_alfanumerico(monkeypatch):
    valor = 'Teste'
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert alfanumerico(valor) == 'É um valor alphanúmerico? True'

def test_sucessor(monkeypatch):
    valor = 10
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert sucessor(valor) == 11

def test_operacoes(monkeypatch):
    valor = 16
    answers = iter([valor])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert operacoes(valor) == (32, 48, 4)

def test_media(monkeypatch):
    nota1 = 9
    nota2 = 7
    answers = iter([str(nota1), str(nota2)])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert media(nota1, nota2) == 8
    assert isinstance(nota1 and nota2, int)

def test_conversao(monkeypatch):
    metro = 10
    answers = iter([metro])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert conversao(metro) == (1000, 10000)

def test_carteira(monkeypatch):
    real = 10.06
    answers = iter([real])
    monkeypatch.setattr('builtins.input', lambda number: next(answers))
    assert carteira(real) == 2
