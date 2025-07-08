import random

alvo = 10
tentativas = 1
# saída para o usuário
print("→ Você tem 3 rodadas para somar o resultado dos lançamentos do dado.")
print(f"→ Seu objetivo é alcançar uma soma maior que os pontos do seu adversário para ganhar.")

while True:
    try:
        escolha = int(input("Escolha:\n1. Jogar\n2. Sair do jogo\nOpção:"))
        if escolha == 1:
            while tentativas <= 3:
                print(f"Você está na {tentativas}º tentativa")
                # entrada do jogador
                jogador1 = input("1º jogador, digite 'Lançar' para lançar o dado: ").strip().lower()
                # verificação
                if jogador1 == "lançar":
                    # jogando dado
                    numero_dado = random.randint(1,6)
                    print(f"Resultado do lançamento: {numero_dado}")
                    # somando aos pontos
                    jogador1_pontos += numero_dado
                    print(f"Sua pontuação atual é: {jogador1_pontos}")
                jogador2 = input("2º jogador, digite 'Lançar' para lançar o dado: ").strip().lower()
                # verificação
                if jogador2 == "lançar":
                    # jogando dado
                    numero_dado = random.randint(1,6)
                    print(f"Resultado do lançamento: {numero_dado}")
                    # somando aos pontos
                    jogador2_pontos += numero_dado
                    print(f"Sua pontuação atual é: {jogador2_pontos}")
                tentativas += 1
            else:
                tentativas = 1
                # verificação
                if jogador1_pontos > jogador2_pontos:
                    print("Jogador 1, você ganhou!")
                    print(f"Seus pontos foram: {jogador1_pontos}")
                elif jogador2_pontos > jogador1_pontos:
                    print("Jogador 2, você ganhou!")
                    print(f"Seus pontos foram: {jogador2_pontos}")
                else:
                    print("Houve um empate!")
                jogador1_pontos = 0
                jogador2_pontos = 0
        else:
            print("Obrigado. Até logo!")
            break
    except ValueError:
        print("Somente aceita dígitos")
    