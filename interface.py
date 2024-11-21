import sys
import pystray
from pystray import MenuItem, Menu
from PIL import Image, ImageDraw
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
import threading

from main import show_help, task_manager, weather, programming_tools 

def create_image():
    image = Image.new('RGB', (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, 64, 64], fill="blue")
    return image

def on_quit(icon, item, app):
    icon.stop()
    app.quit()

def process_command(input_text, output_text):
    command = input_text.text().strip().lower()
    input_text.clear()

    if not command:
        output_text.append("Digite um comando válido.")
        return

    output_text.append(f"Comando recebido: {command}")

    if "tarefa adicionar" in command:
        tarefa = command.replace("tarefa adicionar", "").strip()
        if tarefa:
            task_manager.add_task(tarefa)
            output_text.append(f"Tarefa '{tarefa}' adicionada.")
        else:
            output_text.append("Por favor, descreva a tarefa a ser adicionada.")
    elif "tarefa listar" == command:
        tasks = task_manager.list_tasks()
        output_text.append("Tarefas:")
        output_text.append("\n".join(tasks))
    elif "tarefa remover" in command:
        try:
            id_tarefa = int(command.replace("tarefa remover", "").strip())
            task_manager.remove_task(id_tarefa)
            output_text.append(f"Tarefa com ID {id_tarefa} removida.")
        except ValueError:
            output_text.append("Por favor, forneça um ID de tarefa válido.")
    elif "clima" in command:
        cidade = command.replace("clima", "").strip()
        if cidade:
            weather_data = weather.show_weather(cidade)
            output_text.append(weather_data)
        else:
            output_text.append("Por favor, forneça uma cidade para a previsão do tempo.")
    elif "repositório" in command:
        repo_url = command.replace("repositório", "").strip()
        if repo_url:
            programming_tools.open_github_repo(repo_url)
            output_text.append(f"Repositório {repo_url} aberto no navegador.")
        else:
            output_text.append("Por favor, forneça a URL do repositório do GitHub.")
    elif "projeto" in command:
        project_path = command.replace("projeto", "").strip()
        if project_path:
            programming_tools.open_project_in_vscode(project_path)
            output_text.append(f"Projeto em {project_path} aberto no VS Code.")
        else:
            output_text.append("Por favor, forneça o caminho do projeto local.")
    elif "stackoverflow" in command:
        query = command.replace("stackoverflow", "").strip()
        if query:
            programming_tools.search_stackoverflow(query)
            output_text.append(f"Pesquisa no Stack Overflow iniciada para: {query}")
        else:
            output_text.append("Por favor, forneça uma dúvida para pesquisa.")
    elif "ajuda" == command:
        help_text = """
        Comandos disponíveis:
        - 'tarefa adicionar [descrição]'
        - 'tarefa listar'
        - 'tarefa remover [ID]'
        - 'clima [cidade]'
        - 'repositório [URL]'
        - 'projeto [caminho]'
        - 'stackoverflow [dúvida]'
        - 'ajuda'
        - 'sair'
        """
        output_text.append(help_text)
    elif "sair" == command:
        output_text.append("Até logo!")
        QApplication.quit()
    else:
        output_text.append(f"Comando não reconhecido: {command}")



def start_assistant():
    app = QApplication(sys.argv) 
    window = QWidget()
    window.setWindowTitle("Assistente Pessoal com IA")

    layout = QVBoxLayout()

    text_input = QLineEdit()
    text_input.setPlaceholderText("Digite um comando...")
    layout.addWidget(text_input)

    send_button = QPushButton("Enviar")
    layout.addWidget(send_button)

    output_text = QTextEdit()
    output_text.setReadOnly(True)
    layout.addWidget(output_text)

    send_button.clicked.connect(lambda: process_command(text_input, output_text))

    text_input.returnPressed.connect(lambda: process_command(text_input, output_text))

    window.setLayout(layout)
    window.setGeometry(100, 100, 400, 300)
    window.show()

    icon = pystray.Icon("assistente", create_image(), menu=Menu(MenuItem("Sair", lambda item: on_quit(item, None, app))))
    icon.run_detached() 

    sys.exit(app.exec_())

def main():
    start_assistant()

if __name__ == "__main__":
    main()
