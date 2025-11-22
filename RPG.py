from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, tipo_classe, elemento_bonus):
        self.__nome = nome
        self.__vida = 50
        self.__tipo_classe = tipo_classe
        self.__elemento_bonus = elemento_bonus
        self.__elemento_escolhido = None
        self.__ataque_base = 0
        self.__arma = None

    @abstractmethod
    def reacao_ataque(self):
        pass

    @abstractmethod
    def reacao_de_dano(self):
        pass

    def escolher_elemento(self, elemento):
        self.__elemento_escolhido = elemento
        if elemento == self.__elemento_bonus:
            self.__ataque_base += 2

    def escolher_arma(self, arma):
        self.__arma = arma

    def atacar(self, alvo):
        d10 = D10()
        resultado_dado = d10.rolar()

        info_ataque = {
            'ATACANTE': self.__nome,
            'ALVO': alvo.get_nome(),
            'DADO': resultado_dado,
            'TIPO': 'Normal',
            'DANO': 0,
            'BLOQUEADO': False,
            'DADO_MARRETA': None,
            'DADO_DEFESA': None
        }


        if resultado_dado >= 9:
            info_ataque['TIPO'] = 'Errou o ataque'
            info_ataque['DANO'] = 0
            if isinstance(self.__arma, Chinelos):
                self.__arma.resetar_combo()
            return info_ataque

        dano_arma = self.__arma.calcula_dano()

        if isinstance(self.__arma, Marreta):
            info_ataque['DADO_MARRETA'] = self.__arma.get_ultimo_dado()

        if dano_arma == 0:
            info_ataque['TIPO'] = 'Errou pela arma'
            info_ataque['DANO'] = 0
            return info_ataque

        dano = dano_arma + self.__ataque_base

        if resultado_dado == 8:
            info_ataque['TIPO'] = 'Critico'
            dano += 5

        if isinstance(alvo.get_arma(), PranchaRemo):
            resultado_bloqueio = alvo.get_arma().tentar_bloqueio()
            if resultado_bloqueio is not None:
                info_ataque['DADO_DEFESA'] = resultado_bloqueio
                if resultado_bloqueio == 1:
                    info_ataque['BLOQUEADO'] = True
                    info_ataque['DANO'] = 0
                    return info_ataque


        info_ataque['DANO'] = dano
        alvo.receber_dano(dano)

        if isinstance(alvo.get_arma(), Chinelos):
            alvo.get_arma().resetar_combo()

        return info_ataque

    def get_arma(self):
        return self.__arma

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_tipo_classe(self):
        return self.__tipo_classe

    def get_ataque_base(self):
        return self.__ataque_base

    def get_elemento_bonus(self):
        return self.__elemento_bonus

    def get_elemento_escolhido(self):
        return self.__elemento_escolhido

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def esta_vivo(self):
        return self.__vida > 0


class Druida(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Maconheiro", "Fogo")

    def reacao_ataque(self):
        return "Sou eu bola de fogo hahah"

    def reacao_de_dano(self):
        return "As fumaças falaram por mim"


class Ladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Velho", "Ar")

    def reacao_ataque(self):
        return "Na minha epoca a gente resolvia assim mesmo, criança malcriada"

    def reacao_de_dano(self):
        return "Isso é coisa que se faça com um idoso?"


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Pedreiro", "Terra")

    def reacao_ataque(self):
        return "Receba"

    def reacao_de_dano(self):
        return "Isso não quebra nem tijolo, rapaz"


class Bardo(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Surfista", "Agua")

    def reacao_ataque(self):
        return "Toma essa brother"

    def reacao_de_dano(self):
        return "Sinistro, paz e amor"



import random

class D2:
    def rolar(self):
        """Rola um dado de 2 lados (0 ou 1)"""
        return random.randint(0, 1)


class D10:
    def rolar(self):
        """Rola um dado de 10 lados (1 a 10)"""
        return random.randint(1, 10)




class Arma(ABC):
    def __init__(self, nome, dano_base, vantagem, desvantagem):
        self.__nome = nome
        self.__dano_base = dano_base
        self.__vantagem = vantagem
        self.__desvantagem = desvantagem

    def get_nome(self):
        return self.__nome

    def get_dano_base(self):
        return self.__dano_base

    @abstractmethod
    def calcula_dano(self):
        pass

    def __str__(self):
        return f"  {self.__nome} - Dano: {self.__dano_base}\n+ {self.__vantagem}\n- {self.__desvantagem}"


class PranchaRemo(Arma):
    def __init__(self):
        super().__init__(
            nome="Prancha e Remo",
            dano_base=12,
            vantagem="Pode bloquear 1 único ataque no combate",
            desvantagem="Dano moderado sem efeitos especiais"
        )
        self.__bloqueios_disponiveis = 1
        self.__d2 = D2()

    def get_bloqueios_disponiveis(self):
        return self.__bloqueios_disponiveis

    def tentar_bloqueio(self):
        if self.__bloqueios_disponiveis > 0:
            self.__bloqueios_disponiveis -= 1
            resultado = self.__d2.rolar()
            return resultado
        return None

    def resetar_bloqueio(self):
        self.__bloqueios_disponiveis = 1

    def calcula_dano(self):
        return self.get_dano_base()


class Cigarro(Arma):
    def __init__(self):
        super().__init__(
            nome="Cigarro",
            dano_base=8,
            vantagem="Ataca 2 vezes no mesmo turno (16 de dano total)",
            desvantagem="No turno seguinte causa metade do dano (8)"
        )
        self.__turno = False

    def calcula_dano(self):
        if self.__turno:
            self.__turno = False
            return self.get_dano_base()
        else:
            self.__turno = True
            return self.get_dano_base() * 2



class Marreta(Arma):
    def __init__(self):
        super().__init__(
            nome="Marreta",
            dano_base=20,
            vantagem="Dano brutal instantâneo",
            desvantagem="50% de chance de errar o golpe"
        )
        self.__d2 = D2()
        self.__ultimo_dado = None

    def calcula_dano(self):
        self.__ultimo_dado = self.__d2.rolar()
        if self.__ultimo_dado == 0:
            return 0
        else:
            return self.get_dano_base()

    def get_ultimo_dado(self):
        return self.__ultimo_dado


class Chinelos(Arma):
    def __init__(self):
        super().__init__(
            nome="Chinelos",
            dano_base=10,
            vantagem="Cada acerto consecutivo adiciona +2 de dano",
            desvantagem="Se levar dano, o combo reseta"
        )
        self.__combo = 0

    def calcula_dano(self):
        dano = self.get_dano_base() + (self.__combo * 2)
        self.__combo += 1
        return dano

    def resetar_combo(self):
        self.__combo = 0

    def get_combo(self):
        return self.__combo



def batalha(jogador1, jogador2):

    print("╔" + "=" * 68 + "╗")
    print(f"{' ' * 20}🗡️  INÍCIO DA BATALHA  ⚔️{' ' * 20}")
    print("" + " " * 68 + "")
    print(
        f"  {jogador1.get_nome()} ({jogador1.get_tipo_classe()}) VS {jogador2.get_nome()} ({jogador2.get_tipo_classe()}){' ' * (68 - len(jogador1.get_nome()) - len(jogador2.get_nome()) - len(jogador1.get_tipo_classe()) - len(jogador2.get_tipo_classe()) - 13)}")
    print("╚" + "=" * 68 + "╝")
    print()

    print("📋 INFORMAÇÕES DAS ARMAS:")
    print(f"\n🔹 {jogador1.get_nome()} equipou: {jogador1.get_arma().get_nome()}")
    print(jogador1.get_arma())
    print(f"\n🔹 {jogador2.get_nome()} equipou: {jogador2.get_arma().get_nome()}")
    print(jogador2.get_arma())
    print()
    input("Pressione ENTER para começar a luta...")
    print("\n" + "=" * 70 + "\n")

    turno = 1
    atacante = jogador1
    defensor = jogador2

    while jogador1.esta_vivo() and jogador2.esta_vivo():
        print(f"╔{'═' * 68}╗")
        print(f"║{f'  TURNO {turno}  '.center(68)}║")
        print(f"╚{'═' * 68}╝")
        print()

        print(
            f"💚 {jogador1.get_nome()}: {jogador1.get_vida()} HP [{jogador1.get_arma().get_nome()}]  |  💚 {jogador2.get_nome()}: {jogador2.get_vida()} HP [{jogador2.get_arma().get_nome()}]")
        print()

        print(f"⚔️  {atacante.get_nome()} ataca!")
        print(f'💬 "{atacante.reacao_ataque()}"')
        print()

        resultado = atacante.atacar(defensor)

        print(f"🎲 Posição do dado de 10 lados: {resultado['DADO']}")
        print()

        if resultado['DADO_MARRETA'] is not None:
            resultado_texto = "acertou" if resultado['DADO_MARRETA'] == 1 else "errou"
            print(f"🎲 Dado de 2 lados: {resultado['DADO_MARRETA']} ({resultado_texto})")
            print()

        if resultado['BLOQUEADO']:
            print("🛡️  " + "=" * 60)
            print(f"🛡️  {defensor.get_nome()} BLOQUEOU O ATAQUE com {defensor.get_arma().get_nome()}!")
            print("🛡️  " + "=" * 60)
            if resultado['DADO_DEFESA'] is not None:
                print(f"🎲 Dado de defesa: {resultado['DADO_DEFESA']} (bloqueou com sucesso!)")
            print(f"💬 {defensor.get_nome()}: \"{defensor.reacao_de_dano()}\"")
            print(f"✅ Dano anulado! {defensor.get_nome()} não perdeu vida!")

        elif resultado['DADO_DEFESA'] == 0:
            print("🛡️  " + "=" * 60)
            print(f"🛡️  {defensor.get_nome()} TENTOU BLOQUEAR mas FALHOU!")
            print("🛡️  " + "=" * 60)
            print(f"🎲 Dado de 2 lados: 0 (falhou na defesa!)")
            print(f"💥 {atacante.get_nome()} causou {resultado['DANO']} de dano!")
            print(f"💬 {defensor.get_nome()}: \"{defensor.reacao_de_dano()}\"")
            print(f"💔 {defensor.get_nome()} perdeu {resultado['DANO']} HP!")

        elif resultado['TIPO'] == 'Errou o ataque':
            print("❌ " + "=" * 60)
            print(f"❌ {atacante.get_nome()} ERROU O ATAQUE! (Dado: {resultado['DADO']})")
            print("❌ " + "=" * 60)
            print(f"{defensor.get_nome()} não recebeu dano!")

        elif resultado['TIPO'] == 'Errou pela arma':
            print("❌ " + "=" * 60)
            print(f"❌ ERROU O GOLPE PELO DADO DE 2 LADOS!")
            print("❌ " + "=" * 60)
            print(f"{defensor.get_nome()} não recebeu dano!")

        elif resultado['TIPO'] == 'Critico':
            print("💥 " + "=" * 60)
            print(f"💥 ATAQUE CRÍTICO! +5 de dano bônus!")
            print("💥 " + "=" * 60)
            print(f"⚡ {atacante.get_nome()} causou {resultado['DANO']} de dano!")
            print(f"💬 {defensor.get_nome()}: \"{defensor.reacao_de_dano()}\"")
            print(f"💔 {defensor.get_nome()} perdeu {resultado['DANO']} HP!")

        else:
            print("⚔️  " + "=" * 60)
            print(f"⚔️  ATAQUE NORMAL")
            print("⚔️  " + "=" * 60)
            print(f"💥 {atacante.get_nome()} causou {resultado['DANO']} de dano!")
            print(f"💬 {defensor.get_nome()}: \"{defensor.reacao_de_dano()}\"")
            print(f"💔 {defensor.get_nome()} perdeu {resultado['DANO']} HP!")

        print()
        print("─" * 70)
        print()

        atacante, defensor = defensor, atacante
        turno += 1

    vencedor = jogador1 if jogador1.esta_vivo() else jogador2
    perdedor = jogador2 if vencedor == jogador1 else jogador1

    print("\n" + "=" * 70)
    print("╔" + "=" * 68 + "╗")
    print(f"{' ' * 20}🏆  FIM DA BATALHA  🏆{' ' * 21}")
    print("" + " " * 68 + "")
    print(
        f"  VENCEDOR: {vencedor.get_nome()} ({vencedor.get_tipo_classe()}){' ' * (68 - len(vencedor.get_nome()) - len(vencedor.get_tipo_classe()) - 15)}")
    print(f"  HP Restante: {vencedor.get_vida()}{' ' * (68 - 15 - len(str(vencedor.get_vida())))}")
    print("" + " " * 68 + "")
    print(f"  Derrotado: {perdedor.get_nome()}{' ' * (68 - 14 - len(perdedor.get_nome()))}")
    print("╚" + "=" * 68 + "╝")
    print("=" * 70 + "\n")

    return vencedor



def limpar_tela():
    print("\n" * 2)


def mostrar_etapas():
    print("╔════════════════════════════════════╗")
    print("║           ETAPAS DO JOGO           ║")
    print("║                                    ║")
    print("║     Escolha de Classe              ║")
    print("║     Escolha de Elemento            ║")
    print("║     Escolha de Arma                ║")
    print("╚════════════════════════════════════╝")
    input("\nPressione ENTER para continuar...")
    limpar_tela()


def obter_nome_jogador(numero_jogador):
    print("╔════════════════════════════════════╗")
    print(f"      JOGADOR {numero_jogador} - CADASTRO        ")
    print("╚════════════════════════════════════╝")
    print()
    nome = input("Digite o nome do seu personagem: ").strip()
    while not nome:
        print("❌ Nome não pode ser vazio!")
        nome = input("Digite o nome do seu personagem: ").strip()
    limpar_tela()
    return nome


def escolher_classe():
    print("╔════════════════════════════════════╗")
    print("║        ESCOLHA SUA CLASSE          ║")
    print("║                                    ║")
    print("║  1. Maconheiro (Druida)            ║")
    print("║     → Elemento bônus: Fogo 🔥      ║")
    print("║                                    ║")
    print("║  2. Velho (Ladino)                 ║")
    print("║     → Elemento bônus: Ar 💨        ║")
    print("║                                    ║")
    print("║  3. Pedreiro (Guerreiro)           ║")
    print("║     → Elemento bônus: Terra 🌍     ║")
    print("║                                    ║")
    print("║  4. Surfista (Bardo)               ║")
    print("║     → Elemento bônus: Água 💧      ║")
    print("╚════════════════════════════════════╝")
    print()

    while True:
        try:
            escolha = int(input("Digite o número da classe (1-4): "))
            if escolha in [1, 2, 3, 4]:
                limpar_tela()
                return escolha
            else:
                print("❌ Opção inválida! Escolha entre 1 e 4.")
        except ValueError:
            print("❌ Digite apenas números!")


def escolher_elemento():
    print("╔════════════════════════════════════╗")
    print("║       ESCOLHA SEU ELEMENTO         ║")
    print("║                                    ║")
    print("║  1. Fogo 🔥                        ║")
    print("║  2. Água 💧                        ║")
    print("║  3. Terra 🌍                       ║")
    print("║  4. Ar 💨                          ║")
    print("║                                    ║")
    print("║  DICA: Se escolher o elemento      ║")
    print("║  bônus da sua classe, ganha        ║")
    print("║  +2 de ataque!                     ║")
    print("╚════════════════════════════════════╝")
    print()

    while True:
        try:
            escolha = int(input("Digite o número do elemento (1-4): "))
            if escolha in [1, 2, 3, 4]:
                limpar_tela()
                elementos = {1: "Fogo", 2: "Agua", 3: "Terra", 4: "Ar"}
                return elementos[escolha]
            else:
                print("❌ Opção inválida! Escolha entre 1 e 4.")
        except ValueError:
            print("❌ Digite apenas números!")


def escolher_arma():
    print("╔════════════════════════════════════════════════════╗")
    print("║              ESCOLHA SUA ARMA                      ║")
    print("║                                                    ║")
    print("║  1. Prancha e Remo - Dano: 12                      ║")
    print("║     + Pode bloquear 1 único ataque no combate      ║")
    print("║     - Dano moderado sem efeitos especiais          ║")
    print("║                                                    ║")
    print("║  2. Cigarro - Dano: 8                              ║")
    print("║     + Ataca 2 vezes no mesmo turno (16 total)      ║")
    print("║     - No turno seguinte causa metade do dano (8)   ║")
    print("║                                                    ║")
    print("║  3. Marreta - Dano: 20                             ║")
    print("║     + Dano brutal instantâneo                      ║")
    print("║     - 50% de chance de errar o golpe               ║")
    print("║                                                    ║")
    print("║  4. Chinelos - Dano: 10                            ║")
    print("║     + Cada acerto adiciona +2 (combo crescente)    ║")
    print("║     - Se levar dano, o combo reseta                ║")
    print("╚════════════════════════════════════════════════════╝")
    print()

    while True:
        try:
            escolha = int(input("Digite o número da arma (1-4): "))
            if escolha in [1, 2, 3, 4]:
                limpar_tela()
                armas = {
                    1: PranchaRemo(),
                    2: Cigarro(),
                    3: Marreta(),
                    4: Chinelos()
                }
                return armas[escolha]
            else:
                print("❌ Opção inválida! Escolha entre 1 e 4.")
        except ValueError:
            print("❌ Digite apenas números!")


def mostrar_resumo_personagem(personagem):
    emoji_elemento = {
        "Fogo": "🔥",
        "Agua": "💧",
        "Terra": "🌍",
        "Ar": "💨"
    }

    bonus = " ✓ (BÔNUS!)" if personagem.get_ataque_base() == 2 else ""

    print("╔════════════════════════════════════╗")
    print("      PERSONAGEM CRIADO!            ")
    print("                                    ")
    print(f"  Nome: {personagem.get_nome():<28}")
    print(f"  Classe: {personagem.get_tipo_classe():<26}")
    elemento = personagem.get_elemento_escolhido()
    emoji = emoji_elemento.get(elemento, "")
    print(f"  Elemento: {elemento} {emoji:<21}")
    print(f"  Ataque Base: {personagem.get_ataque_base()}{bonus:<20}")
    print(f"  Arma: {personagem.get_arma().get_nome():<27}")
    print("╚════════════════════════════════════╝")
    print()


def criar_personagem(numero_jogador):
    nome = obter_nome_jogador(numero_jogador)

    mostrar_etapas()

    classe_escolhida = escolher_classe()
    classes = {
        1: Druida(nome),
        2: Ladino(nome),
        3: Guerreiro(nome),
        4: Bardo(nome)
    }
    personagem = classes[classe_escolhida]

    elemento = escolher_elemento()
    personagem.escolher_elemento(elemento)

    arma = escolher_arma()
    personagem.escolher_arma(arma)

    mostrar_resumo_personagem(personagem)
    input("Pressione ENTER para continuar...")
    limpar_tela()

    return personagem