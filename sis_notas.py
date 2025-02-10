def adicionar_alunos_e_notas():
    alunos_notas = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para terminar):")
        if nome.lower() == 'sair':
            break
        try:
            nota= float(input(f"Digite a nota de {nome}:"))
            alunos_notas[nome] = nota
        except ValueError:
            print("Por favor, insira um valor valido para a nota.")

    return alunos_notas

def exibir_resultados(alunos_notas):
    if not alunos_notas:
        print("Nenhum aluno foi adicionado.")
        return
    
    print("\nNotas dos Alunos:")
    for nome, nota in alunos_notas.items():
        print(f"{nome}: {nota}")

    media = sum(alunos_notas.values()) / len(alunos_notas)
    maior_nota = max(alunos_notas.values())
    menor_nota = min(alunos_notas.values())

    aluno_maior_nota = [nome for nome, nota in alunos_notas.items() if nota == maior_nota ]
    aluno_menor_nota = [nome for nome, nota in alunos_notas.items() if nota == menor_nota ]

    print(f"\nMedia das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota} - Aluno(s): {', '.join(aluno_maior_nota)}")
    print(f"Menor nota: {menor_nota} - Aluno(s): {', '.join(aluno_menor_nota)}")

def main():
    alunos_notas = adicionar_alunos_e_notas()
    exibir_resultados(alunos_notas)

if __name__ == "__main__":
    main()