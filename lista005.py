tabelaBrasileiro = ['Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional',
                    'Goiás', 'Botafogo', 'Corinthians', 'Flamengo', 'Athletico-PR',
                    'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza', 'Cruzeiro',
                    'Chapecoense', 'Avaí', 'CSA', 'Grêmio', 'Vasco da Gama']

tabelaNumerica = [12, 11, 12, 9, 15, 14, 12, 2, 15, 5, 1, 15, 0, 11, 4]


"""Desafio 032
Problema: Utilize a função brasileirao6 e a lista tabela_brasileiro, e mostre e retorne
em que posição da tabela está o time da Corinthians.
"""

def brasileirao6():
    retorno = tabelaBrasileiro.index('Corinthians') + 1
    print(retorno)
    return retorno

"""Desafio 033
Problema: Utilize a função brasileirao7 e a lista tabela_brasileiro, e mostre e retorne
o tamanho da lista tabela_brasileiro.
"""

def brasileirao7():
    retorno = len(tabelaBrasileiro)
    print(retorno)
    return retorno

"""Desafio 034
Problema: Utilize a função brasileirao8 e a lista tabela_brasileiro, faça uma cópia da lista tabela_brasileira e
substituia o time São Paulo pelo Ituano
"""

def brasileirao8():
    nova_lista = tabelaBrasileiro[:]
    identificar = nova_lista.index('São Paulo')
    nova_lista[identificar] = 'Ituano'
    print(nova_lista)
    return nova_lista

"""Desafio 035
Desfio: Utilize a função brasileirao9 e a lista tabela_brasileiro, e mostre e retorne uma lista com os últimos 
quatro colocados.
"""

def brasileirao9():
    print(tabelaBrasileiro[-4:])
    return tabelaBrasileiro[-4:]
"""Desafio 036
Problema: Utilize a função brasileirao10 e a lista tabela_brasileiro, para retornar e mostra a tabela_brasileiro 
em ordem decrescente 
"""

def brasileirao10():
    tabelaBrasileiro.reverse()
    print(tabelaBrasileiro)
    return tabelaBrasileiro

"""Desafio 037
Problema: Utilize a função brasileirao11 e a lista tabela_brasileiro, faça uma cópia da lista tabela_brasileiro e
inverta os times de posição e coloque-os em ordem alfabética, mostre e retorne o resultado
"""

def brasileirao11():
    nova_lista = tabelaBrasileiro[:]
    nova_lista.sort(reverse=True)
    print(nova_lista)
    return nova_lista

"""Desafio 038
Desfio: Utilize a função numerica1 e a lista tabela_Numerica, e mostre e retorne uma lista com os dados duplicados
"""

def numerica1():
    print(2 * tabelaNumerica)
    return 2 * tabelaNumerica

"""Desafio 039
Desfio: Utilize a função numerica2 e a lista tabela_Numerica, e mostre e retorne a quantidade de números 12
"""

def numerica2():
    print(tabelaNumerica.count(12))
    return tabelaNumerica.count(12)

"""Desafio 040
Desfio: Utilize a função numerica3 e a lista tabela_Numerica, e mostre e retorne o maior número
"""

def numerica3():
    tabelaNumerica.sort()
    print(tabelaNumerica[-1])
    return tabelaNumerica[-1]

"""Desafio 041
Desfio: Utilize a função numerica3 e a lista tabela_Numerica, e mostre e retorne o menor número
"""

def numerica4():
    tabelaNumerica.sort()
    print(tabelaNumerica[0])
    return tabelaNumerica[0]


if __name__ == '__main__':
    # brasileirao6()
    # brasileirao7()
    # brasileirao8()
    # brasileirao9()
    # brasileirao10()
    # brasileirao11()
    # numerica1()
    # numerica2()
    # numerica3()
    numerica4()
    pass