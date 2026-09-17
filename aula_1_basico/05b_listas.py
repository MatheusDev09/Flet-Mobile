import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Lista de compras"

    # Cor de fundo da página inteira
    page.bgcolor = "#0F2E1D"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Local para guardar os itens da lista
    itens = ["Leite", "Pão", "Café"]

    # Rolagem vertical
    list_view = ft.ListView(expand=True, spacing=8, width=320)

    # Campo de texto para adicionar itens na lista.
    campo = ft.TextField(
        label="Novo item",
        expand=True,
        color="#ffffff",
        label_style=ft.TextStyle(color="#8FD9B6"),
        border_color="#3F8F6C",
        focused_border_color="#5fe0a0",
    )

    def atualizar_lista():
        list_view.controls.clear()
        for nome in itens:
            list_view.controls.append(build_item(nome))
        page.update()

    def adicionar(e):
        # Se o campo de escrita tiver algo, ele coloca a escrita na coluna itens, limpa o input, e atualiza a lista.
        if campo.value:
            itens.append(campo.value)
            campo.value = ""
            atualizar_lista()

    def build_item(nome):
        # Função: Recebe nome e devolve uma nova linha na lista.
        def remover(e):
            itens.remove(nome)
            atualizar_lista()
        
        return ft.Row(
            controls = [
            ft.Text(nome, expand=True, color="#E5F5EC"),
            ft.IconButton(ft.Icons.DELETE, on_click=remover, icon_color="#FF8585"),
            ]
        )

    page.add(
        ft.Row(
            width=320,
            controls=[
                campo,
                ft.Button(
                    "Adicionar", on_click=adicionar, bgcolor="#5FE0A0", color= "#0F2E1D"
                ),
            ],
        ),
        list_view
    )
    atualizar_lista()
        
ft.run(main)