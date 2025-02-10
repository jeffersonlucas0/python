def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_letras(texto):
    letras = [caractere for caractere in texto if caractere.isalpha()]
    return len(letras)

def inverter_texto(texto):
    return texto[::-1]

def substituir_palavras(texto, palavra_antiga, palavra_nova):
    return texto.replace(palavra_antiga, palavra_nova)

def processador_texto(texto):
    print("Escolha uma operação:")
    print("1. Contar palavras")
    print("2. Contar letras")
    print("3. Inverter texto")
    print("4. Substituir palavras-chave")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        print(f"Total de palavras: {contar_palavras(texto)}")
    elif escolha == '2':
        print(f"Total de letras: {contar_letras(texto)}")
    elif escolha == '3':
        print(f"Texto invertido: {inverter_texto(texto)}")
    elif escolha == '4':
        palavra_antiga = input("Digite a palavra a ser substituída: ")
        palavra_nova = input("Digite a nova palavra: ")
        texto_substituido = substituir_palavras(texto, palavra_antiga, palavra_nova)
        print(f"Texto após substituição: {texto_substituido}")
    elif escolha == '5':
        print("Saindo do processador de texto. Até mais!")
        return False
    else:
        print("Opção inválida! Escolha uma opção entre 1 e 5.")

    return True

texto_entrada = input("Digite o texto para processamento: ")

while processador_texto(texto_entrada):
    continue



def processador_texto(texto, **kwargs):
    # Funções lambda para cada operação
    operacoes = {
        'contar_palavras': lambda txt: len(txt.split()),
        'contar_letras': lambda txt: len([c for c in txt if c.isalpha()]),
        'inverter_texto': lambda txt: txt[::-1],
        'substituir_palavra': lambda txt, antiga, nova: txt.replace(antiga, nova)
    }
    
    for operacao, funcao in kwargs.items():
        if operacao in operacoes:
            if operacao == 'substituir_palavra':
                # Para substituição de palavras, precisa de dois argumentos adicionais
                palavra_antiga = funcao.get('palavra_antiga', '')
                palavra_nova = funcao.get('palavra_nova', '')
                texto = operacoes[operacao](texto, palavra_antiga, palavra_nova)
            else:
                resultado = operacoes[operacao](texto)
                print(f"{operacao.replace('_', ' ').capitalize()}: {resultado}")
    
    return texto

# Exemplo de uso
texto_entrada = input("Digite o texto para processamento: ")

# Definindo as operações que queremos realizar
resultante_texto = processador_texto(
    texto_entrada,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=True,
    substituir_palavra={'palavra_antiga': 'velho', 'palavra_nova': 'novo'}
)

print(f"Texto resultante após substituição: {resultante_texto}")


def processador_texto(texto, **kwargs):
    # Funções lambda para cada operação
    operacoes = {
        'contar_palavras': lambda txt: len(txt.split()),
        'contar_letras': lambda txt: len([c for c in txt if c.isalpha()]),
        'inverter_texto': lambda txt: txt[::-1],
        'substituir_palavra': lambda txt, antiga, nova: txt.replace(antiga, nova)
    }
    
    # Processar operações
    for operacao, valor in kwargs.items():
        if operacao in operacoes:
            if operacao == 'substituir_palavra':
                # Verificar se palavras-chave adicionais foram fornecidas
                palavra_antiga = valor.get('antiga', '')
                palavra_nova = valor.get('nova', '')
                texto = operacoes[operacao](texto, palavra_antiga, palavra_nova)
            else:
                resultado = operacoes[operacao](texto)
                print(f"{operacao.replace('_', ' ').capitalize()}: {resultado}")
    
    return texto

# Exemplo de uso
texto_entrada = input("Digite o texto para processamento: ")

# Definindo as operações que queremos realizar
resultante_texto = processador_texto(
    texto_entrada,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=True,
    substituir_palavra={'antiga': 'velho', 'nova': 'novo'}
)

print(f"Texto resultante após operações: {resultante_texto}")
