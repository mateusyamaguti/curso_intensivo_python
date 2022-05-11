tabelaBrasileiro = ('Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional',
                    'Goiás', 'Botafogo', 'Corinthians', 'Flamengo', 'Athletico-PR',
                    'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza', 'Cruzeiro',
                    'Chapecoense', 'Avaí', 'CSA', 'Grêmio', 'Vasco da Gama')

"""
Desafio 026
Problema: Crie uma tupla de números por extenso, de 1 a 15, e retorne o número 10 na tela
"""

def numero_extenso():
    tupla = ('um', 'dois', 'três', 'quarto', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
    return tupla[9]

"""
Desafio 027
Problema: Utilize a função brasileirao1 e a tupla tabela_brasileiro, e mostre
e retorne uma tupla com os 5 primeiros colocados
"""
def brasileirao1():
    retorno = tabelaBrasileiro[0: 5]
    print(retorno)
    return retorno

"""
Desafio 028
Problema: Utilize a função brasileirao2 e a tupla tabela_brasileiro, e mostre e retorne
os últimos 4 colocados da tabela
"""
def brasileirao2():
    retorno = tabelaBrasileiro[-4:]
    print(retorno)
    return retorno

"""
Desafio 029
Problema: Utilize a função brasileirao3 e a tupla tabela_brasileiro, e mostre e retorne
uma tupla com os times em ordem alfabética;
"""
def brasileirao3():
    retorno = tuple(sorted(tabelaBrasileiro))
    print(retorno)
    return retorno

"""
Desafio 030
Problema: Utilize a função brasileirao4 e a tupla tabela_brasileiro, e mostre e retorne
em que posição da tabela está o time da Chapecoense.
"""
def brasileirao4():
    retorno = tabelaBrasileiro.index('Chapecoense') + 1
    print(retorno)
    return retorno

"""
Desafio 031
Problema: Utilize a função brasileirao5 e a tupla tabela_brasileiro, e mostre e retorne as opções abaixo em uma punica tupla:
            A) Apenas mostre os 5 primeiros colocados;
            B) Os últimos 4 colocados da tabela;
            C) Uma lista com os times em ordem alfabética;
            D) Em que posição da tabela está o time da Chapecoense.
            Exemplo: ((A), (B), (C), (D))
Resolução do problema:
"""
def brasileirao5():
    print(f'5 Primeiros colocados: {tabelaBrasileiro[0: 5]}')
    print(f'4 Últimos colocados: {tabelaBrasileiro[-4:]}')
    print(f'Times em Ordem Alfabética: {sorted(tabelaBrasileiro)}')
    print(f'Posição Chapecoense: {tabelaBrasileiro.index("Chapecoense") + 1}º Posição')
    return ((tabelaBrasileiro[0: 5]), (tabelaBrasileiro[-4:]), (sorted(tabelaBrasileiro)),
            (tabelaBrasileiro.index("Chapecoense")+1))


if __name__ == '__main__':
    # numero_extenso()
    # brasileiro1()
    # brasileirao2()
    # brasileirao3()
    # brasileirao4()
    # brasileirao5()
    pass