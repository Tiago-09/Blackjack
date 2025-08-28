from baralho import criar_baralho
from calculopontos import calcular_pontos
from oponente import dealer_joga
from aposta import jogar_blackjack

def iniciar_jogo():
    saldo = 100
    rodada = 1
    print("\n-------------------------------")
    print(" 🔴 Bem-vindo ao cassino!🔴 ")
    print("-------------------------------\n")
    while True:
        if saldo <= 0:
            print("\n Você faliu! \n")
            escolha = input("Deseja adicionar mais créditos para continuar? [s/n] ").lower()
            if escolha == 's':
                try:
                    recarga = int(input("\nDigite o valor da recarga (mínimo R$10, máximo R$999): R$"))
                    if 10 <= recarga <= 999:
                        saldo += recarga
                        print(f"\n Créditos adicionados! Novo saldo: R${saldo}\n")
                    else:
                        print("\n Valor inválido. A recarga deve ser entre R$10 e R$999.\n")
                        continue
                except ValueError:
                    print("\n Entrada inválida. Tente novamente.\n")
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
                    print("\nSaindo do cassino... volte sempre! \n")
                    break

iniciar_jogo()
