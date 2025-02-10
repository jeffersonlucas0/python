def exibir_menu():
    print("\nMenu de opções:")
    print("1. Adicionar produto")
    print("2. Ver lista de produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Encerrar programa")

def adicionar_produto(lista, total_produtos):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor unitário: "))
    total = quantidade * valor
    produto = {"produto '{nome}' adicionado com sucesso"}
    lista.append(produto)
    total_produtos[0] += total
    print(f"Produto '{nome}' adicionado com sucesso!\n")
    return total_produtos

def ver_lista_produtos(lista, total_produtos):
    print("\nLista de produtos:")
    for produto in lista:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, "f"Valor unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
    print(f"\nValor total de todos os produtos: R${total_produtos[0]:.2f}")

def atualizar_produto(lista, total_produtos):
    nome = input("Nome do produto a ser atualizado: ")
    for produto in lista:
        if produto["produto"] == nome:
            total_produtos[0] -= produto["total"]
            produto["produto"] = input("Novo nome do produto: ")
            produto["quantidade"] = int(input("Nova quantidade: "))
            produto["valor"] = float(input("Novo valor unitário: "))
            produto["total"] = produto["quantidade"] * produto["valor"]
            total_produtos[0] +=produto["total"]
            print(f"Produto '{produto['produto']}' atualizado com sucesso!\n")
            return
        print("Produto não encontrado.")

def remover_produto(lista, total_produtos):
    nome = input("Nome do produto a ser removido: ")
    for produto in lista:
        if produto["produto"] == nome:
            total_produtos[0] -= produto["total"]
            lista.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!\n")
            return
        print("Produto não encontrado.")

def main():
    lista_produtos = []
    total_produtos = [0.0]

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(lista_produtos, total_produtos)
        elif opcao == "2":
            ver_lista_produtos(lista_produtos, total_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos, total_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos, total_produtos)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()