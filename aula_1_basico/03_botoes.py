import flet as ft

def main(page: ft.Page):
    page.title = "Formulário Simples"

    page.bgcolor = "#EAF4F4"

    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    nome= ft.TextField(
        label="Seu nome",
        width=280,
        color="#2D3142",
        label_style=ft.TextStyle(color="#6B7B8C"),
        border_color = "#A9C5C6",
        focused_border_color= "#5fa8a0",
    )

    # Checkbox de aceite dos termos
    aceite = ft.Checkbox(
        label="Aceito os termos.",
        check_color="#ffffff",
        active_color="#5FA8A0",
        # Cor do label
        label_style=ft.TextStyle(color="#2D3142"),
    )

    resultado = ft.Text(color="#3e7c7c")

    def enviar(e):
        if not nome.value:
            nome.error_text = "Preencha seu nome corretamente."
            page.update()
            return
        nome.error_text = None
        resultado.value = f"Obrigado, {nome.value}!" if aceite.value else "Você precisa aceitar os termos."
        page.update()

    # Construção dos elementos
    page.add(
    ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            nome,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[aceite],
            ),
            ft.Button(
                "Enviar",
                on_click=enviar,
                bgcolor="#5fa8a0",
                color="#ffffff",
            ),
            resultado,
        ],
    )
)
ft.run(main)