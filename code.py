import json

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(descricao):
    tarefas = carregar_tarefas()
    tarefas.append(descricao)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa(indice):
    tarefas = carregar_tarefas()
    if 1 <= indice <= len(tarefas):
        removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{removida}' removida.")
    else:
        print("Índice inválido.")

def limpar_tarefas():
    salvar_tarefas([])
    print("Todas as tarefas foram apagadas.")

def menu():
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Limpar Todas as Tarefas")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            indice = int(input("Digite o número da tarefa para remover: "))
            remover_tarefa(indice)
        elif opcao == "4":
            limpar_tarefas()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
