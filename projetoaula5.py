def menu():
    print("\nMenu:")
    print("1. Cadastrar um carro")
    print("2. Visualizar carros cadastrados")
    print("3. Editar  um carro cadastrado")
    print("4. Excluir um carro cadastrado")
    print("5. Sair")

def cadastrar_carro(cadastro):
    placa = input("Digite a placa do carro: ").upper()
    if placa in cadastro:
        print("Carro já cadastrado.")
        return
    modelo = input("Qual o modelo do carro: ")
    ano = input("Qual o ano do carro: ")
    cadastro[placa] = {"modelo": modelo, "ano": ano}
    print("Carro cadastro com sucesso!")

def visualizar_carros(cadastro):
    if not cadastro:
        print("Nenhum carro cadastrado.")
        return
    print("\nCarros cadastrados:")
    for placa, info in cadastro.items():
        print(f"Placa: {placa}, Modelo: {info['modelo']}, Ano:{info['ano']}")

def editar_carro(cadastro):
    placa = input("Digite a placa do carro que deseja editar: ").upper()
    if placa not in cadastro:
        print("Carro não encontrado.")
        return
    modelo = input("Qual o novo modelo do carro: ")
    ano = input("Qual o novo ano do carro: ")
    cadastro[placa] = {'modelo': modelo, 'ano': ano}
    print("Carro atualizado com sucesso!")

def excluir_carro(cadastro):
    placa = input("Qual carro deseja excluir: ").upper()
    if placa not in cadastro:
        print("Carro não encontrado.")
        return
    del cadastro[placa]
    print("Carro excluido com sucesso!")

def main():
    cadastro = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_carro(cadastro)
            case "2":
                visualizar_carros(cadastro)
            case "3":
                editar_carro(cadastro)
            case "4":
                excluir_carro(cadastro)
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()