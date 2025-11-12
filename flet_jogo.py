import flet as ft

def main(page: ft.Page):
    # 1. Configurar a página (título, tamanho)
    page.title = "Meu App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Centraliza o conteúdo

    # 2. Criar um controle (ex: um texto)
    welcome_text = ft.Text("Olá, mundo! Esta é sua primeira interface.", size=30)

    # 3. Adicionar o controle à página
    page.add(welcome_text)
    
    page.update() 
    
if __name__ == "__main__":
    # Inicia a aplicação. target=main diz ao Flet qual função deve ser executada.
    ft.app(target=main)
