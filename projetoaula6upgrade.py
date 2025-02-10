tarefas = []

def criar_tarefa(nome, descricao, prioridade, categoria, prazo, frequencia):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'prazo': prazo,
        'frequencia': frequencia,
        'concluida': False
    }
    tarefas.append(tarefa)
    
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (alta, media, baixa)")
    categoria = input("Digite a categoria da tarefa: ")
    prazo = input("Digite o prazo da tarefa: ")
    frequencia = input("Digite a frequencia que a tarefa sera repetida (diaria, semanal, mensal)")
    criar_tarefa(nome, descricao, prioridade, categoria, prazo, frequencia)
    print("Tarefa adicionada com sucesso!")
    
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for tarefa in tarefas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"Nome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nPrioridade: {tarefa['prioridade']}\nCategoria: {tarefa['categoria']}\nPrazo: {tarefa['prazo']}\nFrequencia: {tarefa['frequencia']}")
        
def marcar_concluida(nome_tarefa):
    for tarefa in tarefas:
        if tarefa['nome'].lower() == nome_tarefa.lower():
            tarefa['concluida'] = True
            print(f"Tarefa '{nome_tarefa}' marcada como concluída.")
            return
        print(f"Tarefa '{nome_tarefa}' não encontrada.")
        
def exibir_por_prioridade(prioridade):
    filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'].lower() == prioridade.lower()]
    if not filtradas:
        print(f"Nenhuma tarefa encontrada na prioridade '{prioridade}")
        return
    for tarefa in filtradas:
        print(f"Nome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nCategoria: {tarefa['categoria']}\nStatus: {'concluida' if tarefa['concluida'] else 'Pendente'}\n")
        
def exibir_por_categoria(categoria):
    filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'].lower() == categoria.lower()]
    if not filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return
    for tarefa in filtradas:
        print(f"Nome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nPrioridade: {tarefa['prioridade']}\nStatus {'concluida' if tarefa ['concluida'] else 'Pendente'}\n")
        
def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")        
        print("1. Adicionar tarefa")        
        print("2. Listar tarefas")        
        print("3. Marcar tarefa como concluida")        
        print("4. Exibir tarefa por prioridade")        
        print("5. Exibir tarefas por categoria")        
        print("6. Sair")        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_tarefa()
        elif opcao =='2':
            listar_tarefas()
        elif opcao == '3':
            nome_tarefa = input("Digite o nome da tarefa: ")
            marcar_concluida(nome_tarefa)
        elif opcao == '4':
            prioridade = input("Digite a prioridade (alta, media, baixa): ")
            exibir_por_prioridade(prioridade)
        elif opcao == '5':
            categoria = input("Digite a categoria: ")
            exibir_por_categoria(categoria)
        elif opcao == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 a 6.")
            
if __name__ == "__main__":
    menu()