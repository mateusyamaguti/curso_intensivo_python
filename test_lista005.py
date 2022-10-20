from lista005 import brasileirao6
from lista005 import brasileirao7
from lista005 import brasileirao8
from lista005 import brasileirao9
from lista005 import brasileirao10
from lista005 import brasileirao11
from lista005 import numerica1
from lista005 import numerica2
from lista005 import numerica3
from lista005 import numerica4

import pytest

def test_brasileirao6():
    assert brasileirao6() == 8

def test_brasileirao7():
    assert brasileirao7() == 20

def test_brasileriao8():
    assert brasileirao8() == ['Palmeiras', 'Atlético', 'Ituano', 'Santos', 'Internacional', 'Goiás', 'Botafogo',
                              'Corinthians', 'Flamengo', 'Athletico-PR', 'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza',
                              'Cruzeiro', 'Chapecoense', 'Avaí', 'CSA', 'Grêmio', 'Vasco da Gama']

def test_brasileirao9():
    assert brasileirao9() == ['Avaí', 'CSA', 'Grêmio', 'Vasco da Gama']

def test_brasileirao10():
    assert brasileirao10() == ['Vasco da Gama', 'Grêmio', 'CSA', 'Avaí', 'Chapecoense', 'Cruzeiro', 'Fortaleza',
                               'Fluminense', 'Ceará SC', 'Bahia', 'Athletico-PR', 'Flamengo', 'Corinthians',
                               'Botafogo', 'Goiás', 'Internacional', 'Santos', 'São Paulo', 'Atlético', 'Palmeiras']

def test_brasileirao11():
    assert brasileirao11() == ['Vasco da Gama', 'São Paulo', 'Santos', 'Palmeiras', 'Internacional', 'Grêmio', 'Goiás',
                               'Fortaleza', 'Fluminense', 'Flamengo', 'Cruzeiro', 'Corinthians', 'Chapecoense',
                               'Ceará SC', 'CSA', 'Botafogo', 'Bahia', 'Avaí', 'Atlético', 'Athletico-PR']

def test_numerica1():
    assert numerica1() == [12, 11, 12, 9, 15, 14, 12, 2, 15, 5, 1, 15, 0, 11, 4,
                           12, 11, 12, 9, 15, 14, 12, 2, 15, 5, 1, 15, 0, 11, 4]

def test_numerica2():
    assert isinstance(numerica2(), int)
    assert numerica2() == 3

def test_numerica3():
    assert isinstance(numerica3(), int)
    assert numerica3() == 15

def test_numerica4():
    assert isinstance(numerica4(), int)
    assert numerica4() == 0
