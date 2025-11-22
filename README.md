# M&P: RPG de Combate em Turnos

## Integrantes

**Caick Santos Batista de Araújo** (caick.santos@unisantos.br)  
**Gustavo Pereira da Silva** (gpsilva@unisantos.br)  
**Maria Alice Melek Gervasio** (gervasio@unisantos.br)

---

## Descrição

O M&P é um jogo de RPG desenvolvido em Python com foco em Programação Orientada a Objetos, que apresenta um sistema de combate tático em turnos entre dois jogadores. Foram implementadas entidades principais: **Personagem**, que é uma classe abstrata contendo atributos como nome, vida, tipo de classe, elemento bônus, elemento escolhido, ataque base e arma equipada; e **Arma**, também abstrata, que possui nome, dano base, vantagem e desvantagem. As classes concretas de personagem incluem Druida (Maconheiro), Ladino (Velho), Guerreiro (Pedreiro) e Bardo (Surfista), cada uma com seu elemento bônus específico. As armas implementadas são Prancha e Remo (bloqueio único), Cigarro (ataque alternado forte/fraco), Marreta (alto dano com chance de erro) e Chinelos (sistema de combo crescente).

O sistema utiliza mecânicas baseadas em dados, com a classe D10 determinando resultados de ataque (1-7 acerto normal, 8 crítico, 9-10 erro) e D2 para decisões binárias como bloqueio e acerto da Marreta. Cada jogador escolhe classe, elemento e arma antes da batalha, e o combate se desenvolve em turnos alternados até que um jogador chegue a 0 HP. O projeto objetiva demonstrar a aplicação prática de conceitos fundamentais de POO, como herança, polimorfismo, encapsulamento e composição, em um contexto de desenvolvimento de software interativo. O jogo pode ser jogado tanto pelo terminal (main.py) quanto por interface gráfica Tkinter (gui.py), que também utiliza herança ao estender a classe tk.Tk.

---

## Rodando o Projeto

### Pré-requisitos
- Python 3.8 ou superior

### Em Linux:
```bash
git clone https://github.com/seu-usuario/rpg-mp.git
cd rpg-mp

# Execute o jogo via terminal
python3 main.py

# OU execute com interface gráfica
python3 gui.py
```

### Em Windows (no cmd):
```bash
git clone https://github.com/seu-usuario/rpg-mp.git
cd rpg-mp

# Execute o jogo via terminal
python main.py

# Ou execute com interface gráfica
python gui.py
```

### Observação
Os arquivos `main.py`, `gui.py` e `RPG.py` devem estar na mesma pasta para o correto funcionamento do programa, pois ambos importam os módulos necessários de `RPG.py`. Não são necessárias bibliotecas externas, apenas as bibliotecas padrão do Python (`abc`, `random` e `tkinter`).

---

## Estrutura do Projeto
```
rpg-mp/
│
├── main.py          # Arquivo principal - jogo via terminal com menus interativos
├── gui.py           # Interface gráfica com Tkinter (aplicando herança de tk.Tk)
├── RPG.py           # Classes abstratas e concretas (Personagens, Armas, Dados, Sistema de Batalha)
└── README.md        # Este arquivo
```

---

## Conceitos de POO Aplicados

- **Classes Abstratas (ABC)**: `Personagem` e `Arma` definem contratos que classes filhas devem implementar. A interface gráfica também demonstra herança ao estender `tk.Tk`
- **Herança**: Classes como `Druida`, `Ladino`, `Guerreiro` e `Bardo` herdam de `Personagem`; armas herdam de `Arma`; `JanelaRPG` herda de `tk.Tk`
- **Polimorfismo**: Métodos como `calcula_dano()` e `reacao_ataque()` implementados de forma única em cada classe
- **Encapsulamento**: Atributos privados (prefixo `__`) protegidos e acessados via getters
- **Composição**: Personagem possui uma Arma (relação "tem um"); JanelaRPG possui Personagens

---

## Informações Acadêmicas

**Instituição**: Universidade Católica de Santos (UNISANTOS)  
**Disciplina**: Programação Orientada a Objetos  
**Professor**: Dr. Thiago Ferauche  
**Ano**: 2025
