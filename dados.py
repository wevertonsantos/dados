import random

alvo = 10
tentativas = 1
total_pontos = 0
# saída para o usuário
print("→ Você tem 3 rodadas para somar o resultado dos lançamentos do dado.")
print(f"→ Seu objetivo é alcançar uma soma maior que {alvo} pontos para ganhar.")

while tentativas <= 3:
    print(f"Você está na {tentativas}º tentativa")
    # entrada do jogador
    jogador1 = input("Digite 'Lançar' para lançar o dado: ").strip()
    if jogador1 == "Lançar":
        # jogando dado
        numero_dado = random.randint(1,6)
        print(f"Resultado do lançamento: {numero_dado}")
        # somando aos pontos
        total_pontos += numero_dado
    tentativas += 1

if total_pontos >= alvo:
    print(f"Seus pontos foram: {total_pontos}")
    print("Você ganhou!")
else:
    print(f"Seus pontos foram: {total_pontos}")
    print("Você perdeu!")