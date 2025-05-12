import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.jogador = "X"
        self.tabuleiro = [""] * 9
        self.botoes = []
        self.criar_interface()

    def criar_interface(self):
        for i in range(9):
            botao = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                              command=lambda i=i: self.jogada(i))
            botao.grid(row=i//3, column=i%3)
            self.botoes.append(botao)

    def jogada(self, i):
        if self.tabuleiro[i] == "":
            self.tabuleiro[i] = self.jogador
            self.botoes[i].config(text=self.jogador, state="disabled")
            if self.verificar_vencedor(self.jogador):
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador} venceu!")
                self.reiniciar_jogo()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"

    def verificar_vencedor(self, jogador):
        combinacoes = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
            (0, 4, 8), (2, 4, 6)              # diagonais
        ]
        return any(self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] == jogador
                   for a, b, c in combinacoes)

    def reiniciar_jogo(self):
        self.jogador = "X"
        self.tabuleiro = [""] * 9
        for botao in self.botoes:
            botao.config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
