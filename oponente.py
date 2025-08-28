from calculopontos import calcular_pontos
from baralho import distribuir_carta

def dealer_joga(baralho, dealer, pontos_jogador, rodada):
    while calcular_pontos(dealer) < 17:
        trapacear = rodada % 4 != 0 and pontos_jogador >= 18
        carta = distribuir_carta(baralho, trapacear=trapacear, pontos_jogador=pontos_jogador)
        dealer.append(carta)
        print(f"\nDealer puxa: {carta}")
    return dealer
