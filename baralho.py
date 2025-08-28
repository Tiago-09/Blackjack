import random

def criar_baralho():
    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(baralho)
    return baralho

def distribuir_carta(baralho, trapacear=False, pontos_jogador=0):
    if trapacear and pontos_jogador >= 18:
        for carta in sorted(baralho, reverse=True):
            if pontos_jogador < carta <= 21:
                baralho.remove(carta) 
                return carta
    return baralho.pop()