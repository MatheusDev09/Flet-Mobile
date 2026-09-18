import flet as ft
import flet_geolocator as fg
import httpx

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Meu Endereço"
    
    # Cor de fundo da página inteira: azul petróleo escuro
    page.bgcolor = "#101B2D"
    
    # Centraliza os controles no eixo horizontal usando strings diretas (padrão v1.0)
    page.horizontal_alignment = "center"
    
    # Padding de 60px no topo e na base
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    geo = fg.Geolocator()
    page.services.append(geo) # Serviços persistentes na v1.0 ficam em page.services

    # IMPORTANTE: ElevatedButton mudou para Button na versão 1.0!
    botao = ft.Button("Obter meu endereço", bgcolor="#4C8BF5", color="#0B1622")
    
    # Cartão de resultado: começa invisível e só aparece depois que o endereço chega
    cartao_endereco = ft.Container(visible=False)

    def linha(rotulo: str, valor: str | None) -> ft.Row:
        # Monta uma linha "Rótulo: valor" reutilizável para cada campo do endereço
        return ft.Row(
            controls=[
                ft.Text(rotulo, color="#7F9BC2", width=90),
                ft.Text(valor or "-", color="#E8F0FB", expand=True),
            ]
        )

    async def obter_local(e):
        botao.disabled = True
        cartao_endereco.visible = False
        page.update()

        # 1) Pede permissão e lê a posição atual (lat/lon) do dispositivo
        await geo.request_permission()
        posicao = await geo.get_current_position()

        # 2) Geocodificação reversa usando o serviço gratuito Nominatim
        async with httpx.AsyncClient() as client:
            resposta = await client.get(
                "https://openstreetmap.org",
                params={"format": "jsonv2", "lat": posicao.latitude, "lon": posicao.longitude},
                headers={"User-Agent": "meu-app-flet/1.0"},
            )
            dados = resposta.json()

        endereco = dados.get("address", {})
        rua = endereco.get("road")
        numero = endereco.get("house_number")
        rua_numero = f"{rua}, {numero}" if rua and numero else (rua or "-")
        bairro = endereco.get("suburb") or endereco.get("neighbourhood")
        cidade = endereco.get("city") or endereco.get("town") or endereco.get("village")
        estado = endereco.get("state")
        cep = endereco.get("postcode")
        pais = endereco.get("country")

        # 3) Monta o cartão com uma linha para cada campo do endereço
        cartao_endereco.content = ft.Column(
            spacing=6,
            controls=[
                ft.Text("Endereço encontrado", size=16, weight="bold", color="#4C8BF5"),
                linha("Rua", rua_numero),
                linha("Bairro", bairro),
                linha("Cidade", cidade),
                linha("Estado", estado),
                linha("CEP", cep),
                linha("País", pais),
            ],
        )
        cartao_endereco.visible = True
        botao.disabled = False
        page.update()

    botao.on_click = obter_local

    # Adiciona os elementos na tela usando alinhamento por string simplificada
    page.add(
        ft.Row(alignment="center", controls=[botao]),
        cartao_endereco,
    )

ft.run(main)