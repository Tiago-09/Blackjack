def calcular_pontos(mao):
    total = sum(mao)
    while total > 21 and 11 in mao:
        mao[mao.index(11)] = 1
        total = sum(mao)
    return total
