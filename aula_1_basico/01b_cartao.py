import flet as ft

def main(page: ft.Page):
    page.title = "Primeiro exercício autônomo."

    # Define o tamanho da tela.
    page.window.width = 360
    page.window.height = 800

    # Cor de fundo na tela.
    page.bgcolor = "#2B1B3D"

    # Centralizar elementos.
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Criação dos elementos da página
    page.add(
        # Nome em destaque
        ft.Text(
            "Kauã Mariano Santinho Ebola.",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#FF6FB5",
            text_align=ft.TextAlign.CENTER,
        ),
        ft.Text(
            "Estudante de programação mobile",
            size=14,
            color="#D9C4E8",
            text_align=ft.TextAlign.CENTER,
        )
    )

ft.run(main)