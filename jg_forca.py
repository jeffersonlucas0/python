import random 

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'inteligencia', 'artificial', 'conhecimento',]
    return random.choice(palavras)

def mostrar_progresso(palavra, letras_adivinhadas):
    progresso = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            progresso += letra
        else:
            progresso += '_'
    return progresso

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra.")

    while tentativas > 0:
        print("\nPalavra:", mostrar_progresso(palavra, letras_adivinhadas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif letra in palavra:
            letras_adivinhadas.add(letra)
            print("Bom trabalho! A letra está na palavra.")
        else:
            letras_adivinhadas.add(letra)
            tentativas -= 1
            print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

        if set(palavra) <= letras_adivinhadas:
            print("\nParabens! Você adivinhou a palavra:", palavra)
            break

    else:
        print("\nVocê ficou sem tentativas. A palavra era:", palavra)

jogo_da_forca()