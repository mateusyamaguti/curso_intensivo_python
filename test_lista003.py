from lista003 import jogo_da_adivinhacao
from lista003 import radar
from lista003 import par_impar
from lista003 import passagem
from lista003 import ano_bissexto
from lista003 import maior_menor
from random import randint


import pytest

def test_jogo_da_adivinhacao(monkeypatch):
    maquina = randint(0, 5)
    answers = iter([maquina])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert jogo_da_adivinhacao(maquina) in [0, 1, 2, 3, 4, 5]

def test_radar(monkeypatch):
    velocidade = 95
    answers = iter([velocidade])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert radar(velocidade) == True

def test_par_impar(monkeypatch):
    numero = 10
    answers = iter([numero])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert par_impar(numero) == 'PAR'
    assert isinstance(numero, int)

def test_passagem(monkeypatch):
    distancia = 450
    answers = iter([distancia])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert passagem(distancia) == 202.5

def test_ano_bissexto(monkeypatch):
    ano = 2024
    answers = iter([ano])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert ano_bissexto(ano) == 'BISSEXTO'

def test_maior_menor(monkeypatch):
    num1 = 15
    num2 = 20
    num3 = 5
    answers = iter([num1, num2, num3])
    monkeypatch.setattr('builtins.input', lambda default: next(answers))
    assert maior_menor(num1, num2, num3) == (20, 5)
