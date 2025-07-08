import random

def main():
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    # saída para o usuário
    print("→ Você tem 3 rodadas para somar o resultado dos lançamentos do dado.")
    print("→ Seu objetivo é alcançar uma soma maior que os pontos do seu adversário para ganhar.")
    while True:
        try:
            escolha = int(input("Escolha:\n1. Jogar\n2. Sair do jogo\nOpção:"))
            if escolha == 1:
                jogar_rodada(pontos_jogador1,pontos_jogador2)
            else:
                print("Obrigado. Até logo!")
                break
        except ValueError:
            print("Somente aceita dígitos")
    
def jogar_rodada(pontos_jogador1,pontos_jogador2):
    tentativas = 1
    while tentativas <= 3:
        print(f"Você está na {tentativas}º tentativa\n")
        # entrada do jogador
        jogador1 = input("1º jogador, digite 'Lançar' para lançar o dado: ").strip().lower()
        pontos_jogador1 = lancar_dados(jogador1,pontos_jogador1)
        # entrada do jogador
        jogador2 = input("2º jogador, digite 'Lançar' para lançar o dado: ").strip().lower()
        pontos_jogador2 = lancar_dados(jogador2,pontos_jogador2)
        # acrescentando tentativas
        tentativas += 1
    else:
        # verificação
        if pontos_jogador1 > pontos_jogador2:
            print("Jogador 1, você ganhou!")
            print(f"Seus pontos foram: {pontos_jogador1}")
        elif pontos_jogador2 > pontos_jogador1:
            print("Jogador 2, você ganhou!")
            print(f"Seus pontos foram: {pontos_jogador2}")
        else:
            print("Houve um empate!")
    tentativas = 1
    pontos_jogador1 = 0
    pontos_jogador2 = 0

def lancar_dados(jogador,pontos_jogador):
    while jogador != "lançar":
        print("Você não digitou corretamente")
        jogador = input("Jogador, digite 'Lançar' para lançar o dado: ").strip().lower()
    else:
        # jogando dado
        numero_dado = random.randint(1,6)
        print(f"Resultado do lançamento: {numero_dado}")
        # somando aos pontos
        pontos_jogador += numero_dado
        print(f"Sua pontuação atual é: {pontos_jogador}\n")
    return pontos_jogador

main()