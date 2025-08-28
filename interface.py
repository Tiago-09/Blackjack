import tkinter as tk
from tkinter import messagebox
from baralho import criar_baralho
from calculopontos import calcular_pontos
from oponente import dealer_joga

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack 🃏")
        self.saldo = 100
        self.rodada = 1
        self.baralho = []
        self.jogador = []
        self.dealer = []
        self.aposta = 10

        self.setup_widgets()
        self.nova_rodada()

    def setup_widgets(self):
        self.label_saldo = tk.Label(self.root, text=f"Saldo: R${self.saldo}", font=("Arial", 14))
        self.label_saldo.pack()

        self.label_mao = tk.Label(self.root, text="", font=("Arial", 14))
        self.label_mao.pack()

        self.label_status = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_status.pack()

        self.botao_pedir = tk.Button(self.root, text="Pedir Carta", command=self.pedir_carta)
        self.botao_pedir.pack(side="left", padx=20, pady=20)

        self.botao_parar = tk.Button(self.root, text="Parar", command=self.parar)
        self.botao_parar.pack(side="right", padx=20, pady=20)

    def nova_rodada(self):
        if self.saldo <= 0:
            messagebox.showinfo("Game Over", "Você faliu!")
            self.root.quit()
            return

        self.label_status.config(text="")
        self.baralho = criar_baralho()
        self.jogador = [self.baralho.pop(), self.baralho.pop()]
        self.dealer = [self.baralho.pop(), self.baralho.pop()]
        self.atualizar_mao()

    def atualizar_mao(self):
        total = calcular_pontos(self.jogador)
        self.label_mao.config(text=f"Suas cartas: {self.jogador} | Total: {total}")
        self.label_saldo.config(text=f"Saldo: R${self.saldo}")

    def pedir_carta(self):
        self.jogador.append(self.baralho.pop())
        total = calcular_pontos(self.jogador)
        self.atualizar_mao()

        if total > 21:
            self.label_status.config(text="Você estourou! ❌")
            self.saldo -= self.aposta
            self.finalizar_rodada()

    def parar(self):
        pontos_jogador = calcular_pontos(self.jogador)
        self.label_status.config(text=f"Dealer revela cartas: {self.dealer}")
        self.root.after(1000, self.resultado, pontos_jogador)

    def resultado(self, pontos_jogador):
        self.dealer = dealer_joga(self.baralho, self.dealer, pontos_jogador, self.rodada)
        pontos_dealer = calcular_pontos(self.dealer)

        if pontos_dealer > 21 or pontos_jogador > pontos_dealer:
            self.label_status.config(text="Você venceu! ✅")
            self.saldo += self.aposta
        elif pontos_jogador == pontos_dealer:
            self.label_status.config(text="Empate. 😐")
            self.saldo -= self.aposta // 2
        else:
            self.label_status.config(text="Dealer venceu! ❌")
            self.saldo -= self.aposta

        self.rodada += 1
        self.label_saldo.config(text=f"Saldo: R${self.saldo}")
        self.root.after(2000, self.nova_rodada)

    def finalizar_rodada(self):
        self.root.after(2000, self.nova_rodada)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
