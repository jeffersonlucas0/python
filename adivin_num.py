import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o numero que estou pensando entre 1 e 100.")
    print("Digite 'sair' a qualquer momento para  terminar o jogo.")

    while True:
        palpite = input("Digite seu palpite: ")

        if palpite.lower() == "Sair":
            print("Encerrando o jogo. O numero era:", numero_aleatorio)
            break

        try:
            palpite = int(palpite)
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um numero entre 1 e 100.")
            elif palpite < numero_aleatorio:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_aleatorio:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabens! Você adivinhou o numero em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada invalida. Por favor, digite um numero ou 'sair.")

jogo_adivinhacao()

