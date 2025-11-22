import tkinter as tk
from tkinter import messagebox
from RPG import Druida, Ladino, Guerreiro, Bardo
from RPG import PranchaRemo, Cigarro, Marreta, Chinelos


class JanelaRPG(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("M&P - RPG de Combate")
        self.geometry("800x700")
        self.resizable(False, False)

        self.jogador1 = None
        self.jogador2 = None
        self.turno_atual = 1
        self.atacante = None
        self.defensor = None

        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(
            self,
            text=" BEM-VINDO AO M&P",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=50)

        subtitulo = tk.Label(
            self,
            text="RPG de Combate em Turnos",
            font=("Arial", 14)
        )
        subtitulo.pack(pady=10)

        btn_iniciar = tk.Button(
            self,
            text="INICIAR JOGO",
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            command=self.criar_jogador1
        )
        btn_iniciar.pack(pady=30)

    def criar_jogador1(self):
        self.limpar_tela()

        tk.Label(
            self,
            text="JOGADOR 1 - Criação de Personagem",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(self, text="Nome do Personagem:", font=("Arial", 12)).pack(pady=5)
        self.entry_nome1 = tk.Entry(self, font=("Arial", 12), width=30)
        self.entry_nome1.pack(pady=5)

        tk.Label(self, text="Escolha a Classe:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_classe1 = tk.StringVar(value="Druida")

        classes = [
            ("Maconheiro (Druida) - Bônus: Fogo", "Druida"),
            ("Velho (Ladino) - Bônus: Ar", "Ladino"),
            ("Pedreiro (Guerreiro) - Bônus: Terra", "Guerreiro"),
            ("Surfista (Bardo) - Bônus: Água", "Bardo")
        ]

        for texto, valor in classes:
            tk.Radiobutton(
                self,
                text=texto,
                variable=self.var_classe1,
                value=valor,
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Label(self, text="Escolha o Elemento:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_elemento1 = tk.StringVar(value="Fogo")

        elementos = ["Fogo", "Agua", "Terra", "Ar"]
        for elem in elementos:
            tk.Radiobutton(
                self,
                text=elem,
                variable=self.var_elemento1,
                value=elem.split()[0],
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Label(self, text="Escolha a Arma:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_arma1 = tk.StringVar(value="PranchaRemo")

        armas = [
            ("Prancha e Remo (Dano: 12)", "PranchaRemo"),
            ("Cigarro (Dano: 8/16 alternado)", "Cigarro"),
            ("Marreta (Dano: 20, 50% erro)", "Marreta"),
            ("Chinelos (Dano: 10+ combo)", "Chinelos")
        ]

        for texto, valor in armas:
            tk.Radiobutton(
                self,
                text=texto,
                variable=self.var_arma1,
                value=valor,
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Button(
            self,
            text="CONFIRMAR",
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            width=20,
            height=2,
            command=self.salvar_jogador1
        ).pack(pady=30)

    def salvar_jogador1(self):
        nome = self.entry_nome1.get().strip()

        if not nome:
            messagebox.showerror("Erro", "Digite um nome para o personagem!")
            return

        classe = self.var_classe1.get()
        if classe == "Druida":
            self.jogador1 = Druida(nome)
        elif classe == "Ladino":
            self.jogador1 = Ladino(nome)
        elif classe == "Guerreiro":
            self.jogador1 = Guerreiro(nome)
        else:
            self.jogador1 = Bardo(nome)

        elemento = self.var_elemento1.get()
        self.jogador1.escolher_elemento(elemento)

        arma_escolhida = self.var_arma1.get()
        if arma_escolhida == "PranchaRemo":
            self.jogador1.escolher_arma(PranchaRemo())
        elif arma_escolhida == "Cigarro":
            self.jogador1.escolher_arma(Cigarro())
        elif arma_escolhida == "Marreta":
            self.jogador1.escolher_arma(Marreta())
        else:
            self.jogador1.escolher_arma(Chinelos())

        self.criar_jogador2()

    def criar_jogador2(self):
        self.limpar_tela()

        tk.Label(
            self,
            text="JOGADOR 2 - Criação de Personagem",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(self, text="Nome do Personagem:", font=("Arial", 12)).pack(pady=5)
        self.entry_nome2 = tk.Entry(self, font=("Arial", 12), width=30)
        self.entry_nome2.pack(pady=5)

        tk.Label(self, text="Escolha a Classe:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_classe2 = tk.StringVar(value="Druida")

        classes = [
            ("Maconheiro (Druida) - Bônus: Fogo", "Druida"),
            ("Velho (Ladino) - Bônus: Ar", "Ladino"),
            ("Pedreiro (Guerreiro) - Bônus: Terra", "Guerreiro"),
            ("Surfista (Bardo) - Bônus: Água", "Bardo")
        ]

        for texto, valor in classes:
            tk.Radiobutton(
                self,
                text=texto,
                variable=self.var_classe2,
                value=valor,
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Label(self, text="Escolha o Elemento:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_elemento2 = tk.StringVar(value="Fogo")

        elementos = ["Fogo", "Agua", "Terra", "Ar"]
        for elem in elementos:
            tk.Radiobutton(
                self,
                text=elem,
                variable=self.var_elemento2,
                value=elem.split()[0],
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Label(self, text="Escolha a Arma:", font=("Arial", 12, "bold")).pack(pady=10)
        self.var_arma2 = tk.StringVar(value="PranchaRemo")

        armas = [
            ("Prancha e Remo (Dano: 12)", "PranchaRemo"),
            ("Cigarro (Dano: 8/16 alternado)", "Cigarro"),
            ("Marreta (Dano: 20, 50% erro)", "Marreta"),
            ("Chinelos (Dano: 10+ combo)", "Chinelos")
        ]

        for texto, valor in armas:
            tk.Radiobutton(
                self,
                text=texto,
                variable=self.var_arma2,
                value=valor,
                font=("Arial", 10)
            ).pack(anchor=tk.W, padx=100)

        tk.Button(
            self,
            text="INICIAR BATALHA",
            font=("Arial", 14, "bold"),
            bg="#F44336",
            fg="white",
            width=20,
            height=2,
            command=self.salvar_jogador2_e_iniciar
        ).pack(pady=30)

    def salvar_jogador2_e_iniciar(self):
        nome = self.entry_nome2.get().strip()

        if not nome:
            messagebox.showerror("Erro", "Digite um nome para o personagem!")
            return

        classe = self.var_classe2.get()
        if classe == "Druida":
            self.jogador2 = Druida(nome)
        elif classe == "Ladino":
            self.jogador2 = Ladino(nome)
        elif classe == "Guerreiro":
            self.jogador2 = Guerreiro(nome)
        else:
            self.jogador2 = Bardo(nome)

        elemento = self.var_elemento2.get()
        self.jogador2.escolher_elemento(elemento)

        arma_escolhida = self.var_arma2.get()
        if arma_escolhida == "PranchaRemo":
            self.jogador2.escolher_arma(PranchaRemo())
        elif arma_escolhida == "Cigarro":
            self.jogador2.escolher_arma(Cigarro())
        elif arma_escolhida == "Marreta":
            self.jogador2.escolher_arma(Marreta())
        else:
            self.jogador2.escolher_arma(Chinelos())

        self.iniciar_batalha()

    def iniciar_batalha(self):
        self.atacante = self.jogador1
        self.defensor = self.jogador2
        self.mostrar_tela_batalha()

    def mostrar_tela_batalha(self):
        self.limpar_tela()

        tk.Label(
            self,
            text=f"TURNO {self.turno_atual}",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        frame_status = tk.Frame(self)
        frame_status.pack(pady=20)

        cor1 = "green" if self.jogador1.get_vida() > 25 else "orange" if self.jogador1.get_vida() > 10 else "red"
        tk.Label(
            frame_status,
            text=f"{self.jogador1.get_nome()}\n{self.jogador1.get_vida()} HP\n{self.jogador1.get_arma().get_nome()}",
            font=("Arial", 14, "bold"),
            fg=cor1
        ).pack(side=tk.LEFT, padx=50)

        tk.Label(
            frame_status,
            text="VS ",
            font=("Arial", 18, "bold")
        ).pack(side=tk.LEFT, padx=20)

        cor2 = "green" if self.jogador2.get_vida() > 25 else "orange" if self.jogador2.get_vida() > 10 else "red"
        tk.Label(
            frame_status,
            text=f"{self.jogador2.get_nome()}\n{self.jogador2.get_vida()} HP\n{self.jogador2.get_arma().get_nome()}",
            font=("Arial", 14, "bold"),
            fg=cor2
        ).pack(side=tk.LEFT, padx=50)

        tk.Label(
            self,
            text=f"É a vez de {self.atacante.get_nome()}!",
            font=("Arial", 16, "bold"),
            fg="#FF5722"
        ).pack(pady=20)

        tk.Button(
            self,
            text=f"{self.atacante.get_nome()} ATACAR!",
            font=("Arial", 16, "bold"),
            bg="#FF5722",
            fg="white",
            width=30,
            height=3,
            command=self.executar_ataque
        ).pack(pady=30)

    def executar_ataque(self):
        resultado = self.atacante.atacar(self.defensor)

        mensagem = f" Dado D10: {resultado['DADO']}\n\n"

        if resultado['DADO_MARRETA'] is not None:
            mensagem += f" Dado Marreta: {resultado['DADO_MARRETA']}\n\n"

        if resultado['BLOQUEADO']:
            mensagem += "ATAQUE BLOQUEADO!\n"
            mensagem += f"{self.defensor.get_nome()} não recebeu dano!"
        elif resultado['TIPO'] == 'Critico':
            mensagem += "ATAQUE CRÍTICO!\n"
            mensagem += f"Dano causado: {resultado['DANO']}"
        elif resultado['TIPO'] == 'Errou o ataque':
            mensagem += "ERROU O ATAQUE!\n"
            mensagem += f"{self.defensor.get_nome()} não recebeu dano!"
        elif resultado['TIPO'] == 'Errou pela arma':
            mensagem += "A ARMA ERROU!\n"
            mensagem += f"{self.defensor.get_nome()} não recebeu dano!"
        else:
            mensagem += "ATAQUE NORMAL\n"
            mensagem += f"Dano causado: {resultado['DANO']}"

        messagebox.showinfo("Resultado do Ataque", mensagem)

        if not self.defensor.esta_vivo():
            self.fim_de_jogo()
            return

        self.atacante, self.defensor = self.defensor, self.atacante
        self.turno_atual += 1

        self.mostrar_tela_batalha()

    def fim_de_jogo(self):
        vencedor = self.jogador1 if self.jogador1.esta_vivo() else self.jogador2

        self.limpar_tela()

        tk.Label(
            self,
            text=" FIM DA BATALHA ",
            font=("Arial", 24, "bold"),
            fg="#FFD700"
        ).pack(pady=50)

        tk.Label(
            self,
            text=f"VENCEDOR: {vencedor.get_nome()}",
            font=("Arial", 20, "bold"),
            fg="green"
        ).pack(pady=20)

        tk.Label(
            self,
            text=f"HP Restante: {vencedor.get_vida()}",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Button(
            self,
            text="JOGAR NOVAMENTE",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            command=self.mostrar_tela_inicial
        ).pack(pady=30)

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = JanelaRPG()
    app.mainloop()