import flet as ft

def main(page: ft.Page):
    page.title = "Seja Bem-Vindo!"
    page.theme_mode = "dark"
    page.window.height = 400
    page.window.width = 400

    # Campos de entrada
    Real = ft.TextField(label='Valor em Reais',
                        hint_text='Digite o valor',
                        bgcolor='white',
                        color='black')

    Dólar = ft.TextField(label='Valor em Dólares',
                         hint_text='Digite o valor',
                         bgcolor='white',
                         color='black')

    # Texto para mostrar o resultado
    resultado = ft.Text(value="", color=ft.colors.WHITE)

    # Função para converter as moedas
    def converter(e):
        try:
            real_digitado = float(Real.value) if Real.value else 0
            dolar_digitado = float(Dólar.value) if Dólar.value else 0
            taxa_conversao = 5.0  # Exemplo de taxa de conversão

            # Realizando os cálculos
            dolares_convertidos = real_digitado / taxa_conversao
            reais_convertidos = dolar_digitado * taxa_conversao

            # Atualizando o resultado
            resultado.value = (
                f"{real_digitado} Reais equivalem a {dolares_convertidos:.2f} Dólares.\n"
                f"{dolar_digitado} Dólares equivalem a {reais_convertidos:.2f} Reais."
            )
        except ValueError:
            resultado.value = "Por favor, insira valores válidos."

        # Atualizando o componente de resultado
        resultado.update()

    # Botão de cálculo
    btn_calcular = ft.ElevatedButton(text='Calcular',
                                     width=400,
                                     bgcolor='orange',
                                     color='white',
                                     on_click=converter)  # Chama a função converter

    # Texto de título
    texto = ft.Text(value="Conversor de Moedas",
                    color=ft.colors.GREY_100)

    # Configuração da AppBar
    page.appbar = ft.AppBar(title=texto, center_title=True)

    # Adicionando elementos à página
    page.add(Real, Dólar, btn_calcular, resultado)
    page.update()

# Inicia o aplicativo
ft.app(target=main)