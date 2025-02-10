# ATIVIDADE AULA 3

# 01:

# def classificar_idade(idade):
#     if idade < 12:
#         print("Criança")
#     elif 12 <= idade <=17:
#         print("Adolescente")
#     elif 18 <= idade <= 59:
#         print("Adulto")
#     elif idade >=60:
#         print("Idoso")

# idade_usuario = int(input("Por favor, insira sua idade: "))
# classificar_idade(idade_usuario)

# 02:

# def encontrar_maior_e_menor(num1, num2, num3):
#     maior = num1
#     menor = num1

#     if num2 > maior:
#         maior = num2
#     if num2 < menor:
#         menor = num2

#     if num3 > maior:
#         maior = num3
#     if num3 < menor:
#         menor = num3

#     return maior, menor

# numero1 = float(input("Digite o primeiro numero: "))
# numero2 = float(input("Digite o segundo numero: "))
# numero3 = float(input("Digite o terceiro numero: "))

# maior_numero, menor_numero = encontrar_maior_e_menor(numero1, numero2, numero3)

# print(f"O maior numero é: {maior_numero}")
# print(f"O menor numero é: {menor_numero} ")

# 03

# def contar_pares_impares(numeros):
#     pares = 0
#     impares = 0
#     for numero in numeros :
#         if numero % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
#     return pares, impares

# numeros = []
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}° número inteiro: "))
#     numeros.append(numero)

# quantidade_pares, quantidade_impares = contar_pares_impares(numeros)

# print(f"Quantidade de números pares: {quantidade_pares}")
# print(f"Quantidade de números impares: {quantidade_impares}")

# 04

# def classificar_turma(media_idade):
#     if 0 <= media_idade <= 25:
#         return "Jovem"
#     elif 26 <= media_idade <= 60:
#         return "Adulta"
#     elif media_idade > 60:
#         return "Idosa"
    

# n = int(input("Digite o numero de pessoas na turma: "))

# idades = []

# for i in range(n):
#     idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
#     idades.append(idade)

# media_idade = sum(idades) / n 

# classificacao = classificar_turma(media_idade)

# print(f"A média de idade da turma é: {media_idade:.2f} ")
# print(f"A turma é: {classificacao}")

# 05

# def calcular_estatisticas(numeros):
#     menor_valor = min(numeros)
#     maior_valor = max(numeros)
#     soma_valores = sum(numeros)
#     return menor_valor, maior_valor, soma_valores

# n = int(input("Digite o numero de elementos no conjunto: "))

# numeros = []

# for i in range(n):
#     numero = float(input(f"Digite o {i+1}° numero: "))
#     numeros.append(numero)

# menor, maior, soma = calcular_estatisticas(numeros)

# print(f"O menor valor é: {menor}")
# print(f"O maior valor é: {maior}")
# print(f"A soma dos valores é: {soma}")

# ATV PRATICA

# def gerenciar_compras():
#     total_gasto = 0
#     quantidade_produtos_acima_1000 = 0
#     produto_mais_barato = None
#     preco_mais_barato = float('inf')

#     while True:
#         nome_produto = input("Digite o nome do produto: ")
#         preco_produto = float(input("Digite o preço do produto: "))

#         total_gasto += preco_produto

#         if preco_produto > 1000:
#             quantidade_produtos_acima_1000 += 1

#         if preco_produto > preco_mais_barato:
#             preco_mais_barato = preco_produto 
#             produto_mais_barato = nome_produto

#         continuar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()
#         if continuar != 's':
#             break

#     print("\nResumo da compra:")
#     print(f"A) Total gasto na compra: R%{total_gasto:.2f}")
#     print(f"B) Quantidade de produtos que custam mais de R$1000: {quantidade_produtos_acima_1000}")
#     print(f"C) Nome do produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")

# gerenciar_compras()
