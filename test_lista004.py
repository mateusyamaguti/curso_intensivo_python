from lista004 import numero_extenso
from lista004 import brasileirao1
from lista004 import brasileirao2
from lista004 import brasileirao3
from lista004 import brasileirao4
from lista004 import brasileirao5
import pytest

def test_numero_extenso():
    assert numero_extenso() == 'dez'

def test_brasileirao1():
    assert isinstance(brasileirao1(), tuple)
    assert brasileirao1() == ('Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional')

def test_brasileirao2():
    assert isinstance(brasileirao2(), tuple)
    assert brasileirao2() == ('Avaí', 'CSA', 'Grêmio', 'Vasco da Gama')

def test_brasileirao3():
    assert isinstance(brasileirao3(), tuple)
    assert len(brasileirao3()) == 20
    assert brasileirao3() == ('Athletico-PR', 'Atlético', 'Avaí', 'Bahia', 'Botafogo', 'CSA', 'Ceará SC',
                                          'Chapecoense', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza',
                                          'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco da Gama')

def test_brasileirao4():
    assert brasileirao4() == 16

def test_brasileirao5():
    assert brasileirao5() == (('Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional'),
                             ('Avaí', 'CSA', 'Grêmio', 'Vasco da Gama'),
                             ['Athletico-PR', 'Atlético', 'Avaí', 'Bahia', 'Botafogo', 'CSA', 'Ceará SC',
                              'Chapecoense', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás',
                              'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco da Gama'], 16)