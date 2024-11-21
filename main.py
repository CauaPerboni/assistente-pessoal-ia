from modules.tasks import TaskManager
from modules.weather import Weather
from modules.programming import ProgrammingTools
import schedule
import time

task_manager = TaskManager()
weather = Weather(api_key="DIGITE_SUA_KEY")
programming_tools = ProgrammingTools()

def show_help():
    print("""
    Comandos disponíveis:
    ----------------------
    1. Tarefas:
    - 'tarefa adicionar' [descrição]: Adiciona uma nova tarefa.
    - 'tarefa listar': Lista todas as tarefas.
    - 'tarefa remover' [ID]: Remove uma tarefa pelo ID.

    2. Clima:
    - 'clima' [cidade]: Exibe a previsão do tempo para a cidade especificada.

    3. Programação:
    - 'repositório' [URL]: Abre o repositório do GitHub no navegador.
    - 'projeto' [caminho]: Abre um projeto local no VS Code.
    - 'stackoverflow' [dúvida]: Pesquisa uma dúvida no Stack Overflow.

    4. Outros:
    - 'ajuda': Exibe esta lista de comandos.
    - 'sair': Encerra o assistente.
    """)

def main():
    print("Olá! Sou seu assistente pessoal.")
    show_help()
    while True:
        command = input("Digite um comando: ").lower()
        if "tarefa" in command:
            print("O que você quer fazer com as tarefas?")
            sub_command = input("[adicionar|listar|remover]: ").lower()
            if sub_command == "adicionar":
                tarefa = input("Descreva a tarefa: ")
                task_manager.add_task(tarefa)
            elif sub_command == "listar":
                task_manager.list_tasks()
            elif sub_command == "remover":
                id_tarefa = int(input("Digite o ID da tarefa: "))
                task_manager.remove_task(id_tarefa)
            else:
                print("Comando inválido.")
        elif "clima" in command:
            cidade = input("Digite sua cidade: ")
            weather.show_weather(cidade)
        elif "repositório" in command:
            repo_url = input("Digite a URL do repositório no GitHub: ")
            programming_tools.open_github_repo(repo_url)
        elif "projeto" in command:
            project_path = input("Digite o caminho do projeto local: ")
            programming_tools.open_project_in_vscode(project_path)
        elif "stackoverflow" in command:
            query = input("Digite sua dúvida para pesquisar no Stack Overflow: ")
            programming_tools.search_stackoverflow(query)
        elif "ajuda" in command:
            show_help()
        elif "sair" in command:
            print("Até logo!")
            break
        else:
            print("Comando não reconhecido.")

schedule.every().minute.do(main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
