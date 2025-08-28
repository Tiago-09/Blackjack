import random

def criar_baralho():
    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(baralho)
    return baralho

def calcular_pontos(mao):
    total = sum(mao)
    while total > 21 and 11 in mao:
        mao[mao.index(11)] = 1
        total = sum(mao)
    return total

def distribuir_carta(baralho, trapacear=False, pontos_jogador=0):
    if trapacear and pontos_jogador >= 18:
        for carta in sorted(baralho, reverse=True):
            if pontos_jogador < carta <= 21:
                baralho.remove(carta)
                return carta
    return baralho.pop()

def dealer_joga(baralho, dealer, pontos_jogador, rodada):
    while calcular_pontos(dealer) < 17:
        trapacear = rodada % 4 != 0 and pontos_jogador >= 18
        carta = distribuir_carta(baralho, trapacear=trapacear, pontos_jogador=pontos_jogador)
        dealer.append(carta)
        print(f"\nDealer puxa: {carta}")
    return dealer

def jogar_blackjack(saldo, rodada):
    print(f"\n💰 Saldo atual: R${saldo}")
    print(" ")
    try:
        aposta = int(input("Digite o valor da aposta (mínimo R$10, máximo R$999): R$")) 
    except ValueError:
        print("\n❌ Valor inválido. Reiniciando rodada com aposta padrão de R$10.\n")
        return saldo

    if aposta < 10 or aposta > 999:
        print("\n❌ Aposta fora dos limites permitidos (R$10 - R$999). Tente novamente na próxima rodada.\n")
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
                print("\nVocê estourou! Dealer vence. ❌\n")
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
        print("Você venceu! 🤑✅\n")
        saldo += aposta
    elif pontos_jogador == pontos_dealer:
        print("Empate... mas o dealer leva 😈\n")
        saldo -= aposta // 2
    else:
        print("Dealer venceu! ❌\n")
        saldo -= aposta

    return saldo

def iniciar_jogo():
    saldo = 100
    rodada = 1
    print("\n-------------------------------")
    print(" 🔴 Bem-vindo ao cassino!🔴 ")
    print("-------------------------------\n")
    while True:
        if saldo <= 0:
            print("\n😵 Você faliu! ❌\n")
            escolha = input("Deseja adicionar mais créditos para continuar? [s/n] ").lower()
            if escolha == 's':
                try:
                    recarga = int(input("\nDigite o valor da recarga (mínimo R$10, máximo R$999): R$"))
                    if 10 <= recarga <= 999:
                        saldo += recarga
                        print(f"\n✅ Créditos adicionados! Novo saldo: R${saldo}\n")
                    else:
                        print("\n❌ Valor inválido. A recarga deve ser entre R$10 e R$999.\n")
                        continue
                except ValueError:
                    print("\n❌ Entrada inválida. Tente novamente.\n")
                    continue
            else:
                confirmar_saida = input("\nVocê realmente deseja sair? [s/n] ").lower()
                if confirmar_saida == 's':
                    print("\nSaindo do cassino... volte sempre!\n")
                    break
                else:
                    continue

        saldo = jogar_blackjack(saldo, rodada)
        rodada += 1
        print(f"\nSeu novo saldo: R${saldo}\n")
        if saldo > 0:
            continuar = input("Deseja jogar novamente? [s/n] ").lower()
            print(" ")
            if continuar != 's':
                confirmar_saida = input("Você realmente deseja sair? [s/n] ").lower()
                print(" ")
                if confirmar_saida == 's':
                    print("\nSaindo do cassino... volte sempre!👋😁 \n")
                    break

iniciar_jogo()