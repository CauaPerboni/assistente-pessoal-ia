import webbrowser
import os

class ProgrammingTools:
    def __init__(self):
        pass

    def open_github_repo(self, repo_url):
        """Abre um repositório no navegador"""
        try:
            webbrowser.open(repo_url)
            print(f"Abrindo repositório: {repo_url}")
        except Exception as e:
            print(f"Erro ao abrir o repositório: {e}")

    def open_project_in_vscode(self, project_path):
        """Abre um projeto local no VS Code"""
        try:
            if os.path.exists(project_path):
                os.system(f'code "{project_path}"') 
                print(f"Abrindo projeto no VS Code: {project_path}")
            else:
                print("Caminho do projeto não encontrado.")
        except Exception as e:
            print(f"Erro ao abrir o projeto: {e}")

    def search_stackoverflow(self, query):
        """Abre o navegador com uma busca no Stack Overflow"""
        try:
            search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            print(f"Pesquisando no Stack Overflow: {query}")
        except Exception as e:
            print(f"Erro ao realizar a busca: {e}")
