import flet as ft

def main(page: ft.Page):
    page.title = "Seja bem-vindo!"
    
    page.theme_mode = "dark"

    page.window.height = 400
    page.window.width = 400

    def calcular_imc(e):
        peso_digitado = float(peso.value)
        altura_digitada = float(altura.value)
        imc = peso_digitado / altura_digitada ** 2

        resultado = ft.Text(f"Seu IMC é = {imc:.2f}")
        alerta = ft.AlertDialog(title=resultado)
        page.dialog = alerta
        alerta.open = True
        page.update()



    peso = ft.TextField(label='Peso',
                        hint_text='Digite o seu peso',
                        bgcolor='white',
                        color='black')
    
    altura = ft.TextField(label='Altura',
                          hint_text='Digite sua altura',
                          color='black',
                          bgcolor='white')
    btn_calcular = ft.ElevatedButton(text='Calcular',
                                    width=400,
                                    bgcolor='orange',
                                    color='white',
                                    on_click=calcular_imc
                                    )


    texto = ft.Text(value="Calculadora de IMC",
                    color=ft.colors.GREY_100)


    page.appbar = ft.AppBar(title=texto, center_title=True)

    page.update()
    page.add(peso, altura, btn_calcular)

ft.app(target=main)