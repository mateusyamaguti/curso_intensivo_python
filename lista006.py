'''
Ricardinho é um menino muito peralta, porém extremamente curioso, e em um passeio de bicicleta percebeu que em seu
bairro existem algumas lanchonetes, com isso, Ricardinho pesquisou os lanches mais vendidos de cada lanchonete, e agora
precisa de ajuda para analisa-los.
'''


lanchonetes = {'Napp Dogão': {'lanche':'Dogão Supremo', 'valor': 24.99,'peso': 500 },
               'Cubo Lanchonete':{'lanche': 'Churrasco de costela', 'valor': 29.99, 'peso' :600},
               'Live Hamburgueria':{'lanche': 'Hambuguer SalesLive', 'valor': 27.99, 'peso': 450},
               'SOS Lanches':{'lanche': 'Catupresunto', 'valor': 18.99, 'peso': 400}}

"""Desafio 042
Desfio: Utilize a função lanchonetes1 e o dicionário lanchonetes, e mostre e retorne quantas lanchonetes existem 
no bairro
"""
def lanchonetes1():
    print(len(lanchonetes))
    return lanchonetes


"""Desafio 043
Desfio: Utilize a função lanchonetes2 e o dicionário lanchonetes, e mostre e retorne o nome de cada lanchonete
obs: não precisa tratar a string de retorno
"""

def lanchonetes2():
    print(lanchonetes.keys())
    return lanchonetes.keys()

"""Desafio 044
Desfio: Utilize a função lanchonetes3 e o dicionário lanchonetes, e mostre o nome de cada lanche mais vendido de cada 
lanchonete, e depois retorne esse lanches em uma tupla
obs: não precisa tratar a string de retorno
"""

def lanchonetes3():
    print(lanchonetes['Napp Dogão']['lanche'])
    print(lanchonetes['Cubo Lanchonete']['lanche'])
    print(lanchonetes['Live Hamburgueria']['lanche'])
    print(lanchonetes['SOS Lanches']['lanche'])

    return (lanchonetes['Napp Dogão']['lanche'], lanchonetes['Cubo Lanchonete']['lanche'],
            lanchonetes['Live Hamburgueria']['lanche'],
            lanchonetes['SOS Lanches']['lanche'])

"""Desafio 045
Desafio: Inesperadamente foi inaugurada uma nova lanchonete no bairro do Ricardinho, lanchonete Conect Lanches. 
E o lanche que eles acreditam que trará maior sucesso é o Frango Gostoso, que custará cerca de R$23.99, com pesoo de 400g.
Utilize a função lanchonetes4 e o dicionário lanchonetes, e faça uma cópia do dicionário lanchonetes.
A partir disso, adicione o novo estabalecimentos e as caracteristica de seu lanche. Mostre e retorne o novo dicionario
obs: não precisa tratar a string de retorno
"""

def lanchonetes4():
    new_dict = lanchonetes.copy()
    new_dict['Conect Lanches'] = {'lanche': 'Frango Gostoso', 'valor': 23.99, 'peso': 400}
    print(new_dict)
    return new_dict

"""Desafio 046
Desfio: Utilize a função lanchonetes5 e o dicionário lanchonetes, para fazer um buscador de lanchonete, e caso o
estabelecimento não exista, retorna uma tupla vazia. Se o estabelecimento existir, retorna o lanche mais vendido e suas
caracteristicas em formato de dicionário
"""

def lanchonetes5(lanchonete):
    tupla = ()
    retorno = lanchonetes.get(lanchonete, tupla)
    print(retorno)
    return retorno

if __name__ == '__main__':
    # lanchonetes1()
    # lanchonetes2()
    # lanchonetes3()
    # lanchonetes4()
    # lanchonetes5('Napp Dogão')
    pass