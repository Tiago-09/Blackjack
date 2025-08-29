from calculopontos import calcular_pontos
from baralho import criar_baralho
from oponente import dealer_joga

def jogar_blackjack(saldo, rodada):
    
    print(f"\n Saldo atual: R${saldo}")
    print(" ")

    try:
        aposta = int(input("Digite o valor da aposta (mínimo R$10, máximo R$999): R$")) 
    except ValueError:
        print("\n Valor inválido. Reiniciando rodada com aposta padrão de R$10.\n")
        return saldo

    if aposta < 10 or aposta > 999:
        print("\n Aposta fora dos limites permitidos (R$10 - R$999). Tente novamente na próxima rodada.\n")
        return saldo

    if aposta > saldo:
        print("\nVocê não tem saldo suficiente. Apostando tudo que resta.\n")
        aposta = saldo

    baralho = criar_baralho()
    jogador = [baralho.pop(), baralho.pop()]
    dealer = [baralho.pop(), baralho.pop()]

    while True:
        print(f"\nSuas cartas: {jogador} | Total: {calcular_pontos(jogador)}\n")
        acao = input("Deseja [P]edir ou [S]top? ").lower()
        if acao == 'p':
         jogador.append(baralho.pop())
        if calcular_pontos(jogador) > 21:
    
        print(f"\nSuas cartas finais: {jogador} | Total: {calcular_pontos(jogador)}")
        print("\nVocê estourou! Dealer vence. \n")
        return saldo - aposta
                print("\nVocê estourou! Dealer vence. \n")
                return saldo - aposta
        else:
            break

    print(f"\nDealer revela cartas: {dealer}\n")
    dealer = dealer_joga(baralho, dealer, calcular_pontos(jogador), rodada)

    pontos_jogador = calcular_pontos(jogador)
    pontos_dealer = calcular_pontos(dealer)

    print(f"\nResultado final:\n")
    print(f"Você: {pontos_jogador} | Dealer: {pontos_dealer}\n")

    if pontos_dealer > 21 or pontos_jogador > pontos_dealer:
        print("Você venceu! \n")
        saldo += aposta
    elif pontos_jogador == pontos_dealer:
        print("Empate... mas o dealer leva \n")
        saldo -= aposta // 2
    else:
        print("Dealer venceu! \n")
        saldo -= aposta

    return saldo