import flet as ft

def card_produto(nome, preco):
    return ft.Container(
        width=140,
        height=140,
        padding=12,
        bgcolor="#fff3E0",
        border_radius=12,
        content=ft.Column(
            # Alinhamento vertical
            alignment=ft.MainAxisAlignment.CENTER,
            # Alinhamento horizontal
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Icon("local_mall", size=22, color="#E65100"),
                ft.Text(nome, weight=ft.FontWeight.BOLD, color="#4E342E"),
                ft.Text(f"R$ {preco:.2f}", color="#6D4C41")
            
            ],
        ),
    )

def main(page: ft.Page):
    page.title = "Prateleira"

    # Define o tamanho da tela.
    page.window.width = 360
    page.window.height = 800

    # Cor de fundo na tela.
    page.bgcolor = "#2E1A47"

    # Centralizar elementos.
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Tupla (nome, preço)
    produtos = [
        ("Caneta", 3.5),
        ("Caderno", 6.0),
        ("Boneca da Teto", 12.0),
        ("Boneca da Miku", 7.0),
        ("Gambarimasu", 0.06),
    ]
    page.add(
        ft.Row(
            scroll=ft.ScrollMode.AUTO,
            #scroll=ft.ScrollMode.HIDDEN, # For mobile.
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[card_produto(nome, preco) for nome, preco in produtos],
    )
    )
ft.run(main)