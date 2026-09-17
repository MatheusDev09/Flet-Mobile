import flet as ft

def main(page: ft.Page):
    page.title = "Árvore de controles"

    # Define o tamanho da tela.
    page.window.width = 360
    page.window.height = 800

    # Cor de fundo na tela.
    page.bgcolor = "#0B3D3A"

    # Centralizar elementos.
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Container principal que representa o cartão visual.
    cartao = ft.Container(
        # Conteúdo do cartão distribuído em colunas.
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, #Centraliza tudo no centro do cartão.
            controls=[
                # Título do cartão: texto maior, negrito, e cor de destaque.
                ft.Text(
                    "Matheus Boogers da Silva",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FF5500",
                ),
                # Texto descritivo (abaixo do título)
                ft.Text(
                    "Desenvolvedor Back-End em formação.",
                    color="#D3D3D3",
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Button(
                            "Ação 1",
                            bgcolor="#FF0000",
                            color="#0b3d3a",
                        ),
                        ft.OutlinedButton("Ação 2"), # Botão Secundário
                    ]
                ),
            ]
        ),
        padding=16, # Espaçamento interno entre o contéudo
        bgcolor="#123C3C", # Cor de fundo ("Row" - Arranjo em linha)
        border_radius=12, # Arredondamento.
    )
    page.add(cartao)

ft.run(main)