from lista006 import lanchonetes
from lista006 import lanchonetes1
from lista006 import lanchonetes2
from lista006 import lanchonetes3
from lista006 import lanchonetes4
from lista006 import lanchonetes5

import pytest

def test_lanchonetes1():
    assert len(lanchonetes1()) == 4

def test_lanchonetes2():
    chaves = lanchonetes2()
    lista = []
    for item in chaves:
        lista.append(item)
    assert lista == ['Napp Dogão', 'Cubo Lanchonete', 'Live Hamburgueria', 'SOS Lanches']


def test_lanchonetes3():
    assert lanchonetes3() == (lanchonetes['Napp Dogão']['lanche'], lanchonetes['Cubo Lanchonete']['lanche'],
            lanchonetes['Live Hamburgueria']['lanche'],
            lanchonetes['SOS Lanches']['lanche'])

def test_lanchonetes4():
    assert lanchonetes4() == {'Napp Dogão': {'lanche': 'Dogão Supremo', 'valor': 24.99, 'peso': 500},
                              'Cubo Lanchonete': {'lanche': 'Churrasco de costela', 'valor': 29.99, 'peso': 600},
                              'Live Hamburgueria': {'lanche': 'Hambuguer SalesLive', 'valor': 27.99, 'peso': 450},
                              'SOS Lanches': {'lanche': 'Catupresunto', 'valor': 18.99, 'peso': 400},
                              'Conect Lanches': {'lanche': 'Frango Gostoso', 'valor': 23.99, 'peso': 400}}

def test_lanchonetes5():
    assert isinstance(lanchonetes5('Napp Dogão'), dict)
    assert lanchonetes5('Napp Dogão') == {'lanche': 'Dogão Supremo', 'valor': 24.99, 'peso': 500}
    assert lanchonetes5('Esquina Lanche') == ()



