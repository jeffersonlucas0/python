def soma(num1, num2):
    return num1 + num2

def subtraçao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

def calculadora():
    while True:
        print("\nEscolha uma opção:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite números válidos.")
                continue

            if escolha == '1':
                resultado = soma(num1, num2)
                print(f"O resultado da soma é: {resultado}")
            elif escolha == '2':
                resultado = subtraçao(num1, num2)
                print(f"O resultado da subtração é: {resultado}")
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
                print(f"O resultado da multiplicação é: {resultado}")
            elif escolha == '4':
                resultado = divisao(num1, num2)
                print(f"O resultado da divisão é: {resultado}")

        else:
            print("Opção inválida! Escolha uma opçao entre 1 e 5.")

calculadora() 
                

    