import random
# 1 - entrada do usuário
entrada_usuario = "Jogar" #input("Digite 'Jogar' para jogar o dado: ")

if entrada_usuario == "Jogar":
    dado = random.randint(1,6)
    print(dado)