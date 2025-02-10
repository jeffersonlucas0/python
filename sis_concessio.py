def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar Carro")
    print("2. Listar Carro")
    print("3. Vender Carro")
    print("4. Sair")

def adicionar_carro(carros):
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    preco = input("Digite o preço do carro: ")
    carro = {'modelo': modelo, 'ano' : ano, 'preco': preco}
    carros.append(carro)
    print(f"Carro {modelo} adicionado com sucesso!")

def listar_carros(carros):
    if carros:
        print("n\Carros Disponiveis:")
        for i, carro in enumerate(carros, 1):
            print(f"{i}. Modelo: {carro['modelo']}, Ano: {carro['ano']}, Preco: {carro['preco']}") 

    else:
        print("Nenhum carro disponivel no estoque. ")

def vender_carro(carros):
    listar_carros(carros)
    try:
        indice= int(input("Digite o numero do carro que deseja vender: ")) - 1
        if 0 <= indice < len(carros):
            carro_vendido = carros.pop(indice)
            print(f"Carro {carro_vendido['modelo']} vendido com sucesso!")
        else:
            print("Indice invalido. Tent6e novamente.")
    except ValueError:
        print("Entrada invalida. Digite um numero valido.")

def sistema_concessionaria():
    carros = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_carro(carros)
        elif opcao =="2":
            listar_carros(carros)
        elif opcao  == "3":
            vender_carro(carros)
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção invalida. Tente novamente.")
    
sistema_concessionaria()


