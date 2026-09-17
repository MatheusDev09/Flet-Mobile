import flet as ft

def main(page: ft.Page):

    # Título que aparece na barra da janela/aba
    page.title = "Contador"

    # Cor de fundo da página inteira: azul marinho escuro
    page.bgcolor = "#3D0e0e"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Dimensões da página
    page.window.width = 360
    page.window.height= 800 
    
    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Texto que exibe valor atual do contador
    contador=ft.Text("0", size=40, color="#FF6b6b", weight=ft.FontWeight.BOLD)

    # Variável para guardar a contagem

    valor = 0

    # Funcionalidades
    def somar(e):
        # Usamos o nonlocal para dizer ao Python que o valor da variável é sensível a mudanças. Que foi criada na main.
        nonlocal valor
        valor += 1
        contador.value = str(valor)
        page.update()

    def subtrair(e):
        nonlocal valor
        valor -= 1
        contador.value = str(valor)
        page.update()

    def resetar(e):
        nonlocal valor
        valor = 0
        contador.value = str(valor)
        page.update()

    page.add(
        
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=subtrair, icon_color="#ff6b6b"),
                contador,
                ft.IconButton(ft.Icons.ADD, on_click=somar, icon_color="#FF6b6b")
            ],
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(
                    "Resetar",
                    icon=ft.Icons.RESTART_ALT,
                    on_click=resetar,
                    style=ft.ButtonStyle(color="#ffb4b4"),
                ),
            ],
        ),
    )

ft.run(main)