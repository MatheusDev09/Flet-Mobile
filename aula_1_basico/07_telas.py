import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Navegação"

    def view_inicio():
        return ft.View(
            route='/', # Rota da página principal.
            appbar=ft.AppBar(title=ft.Text("Inicío")),
            bgcolor="#221A3D",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=ft.Padding(top=60, bottom=60, left=0, right=0),
            controls=[ 
                ft.Text("Tela inicial", color="#C9B6F2", size=18),
                # Lambda serve como uma forma rápida e eficiente de ser fazer uma função (oneline)
                ft.Button("Ir para Sobre", bgcolor="#9B7EDE", on_click=lambda e: page.navigate("/sobre"), color="#221A3D"),
            ],
        )
    
    def view_sobre():
        return ft.View(
            route="/sobre",
            appbar=ft.AppBar(title=ft.Text("Sobre")),
            bgcolor="#1A2E3D",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=ft.Padding(top=60, bottom=60, left=0, right=0),
            controls=[
                ft.Text("Esta é a tela sobre", color="#9FD3E8"),
                ft.Button("Ir para a página principal", bgcolor="#9B7EDE", on_click=lambda e: page.navigate("/"), color="#221A3D")
            ]
        )

    def route_change():
        # Reconstrói a pilha de views a partir da rota atual
        page.views.clear()
        page.views.append(view_inicio())
        if page.route == "/sobre":
            page.views.append(view_sobre())
        page.update()

    def view_pop(e):
        # Função acionada quando o usuário clica no "Voltar"
        page.views.pop() # Remove a view de toda pilha
        # Após remover é preciso dizer para onde ir "page.views[-1] ou seja, início"
        page.navigate(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change() # Constrói a view da rota inicial.

ft.run(main)