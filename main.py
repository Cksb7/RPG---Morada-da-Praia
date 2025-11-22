from RPG import criar_personagem, batalha

print("╔════════════════════════════════════════════╗")
print("║             BEM-VINDO AO M&P               ║")
print("╚════════════════════════════════════════════╝")
print()
input("Pressione ENTER para começar...")
print("\n" * 2)

print(" Preparando Jogador 1...\n")
jogador1 = criar_personagem(1)

print(" Preparando Jogador 2...\n")
jogador2 = criar_personagem(2)


print("⚔️ Todos prontos! A batalha vai começar!\n")
input("Pressione ENTER para iniciar a batalha...")
print("\n" * 2)

vencedor = batalha(jogador1, jogador2)