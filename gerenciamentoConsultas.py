import flet as ft
import json

class Consulta:
    """Classe para armazenar os dados de uma consulta."""
    def __init__(self, nome_paciente, data, horario, cargo_medico, medico, descricao):
        self.nome_paciente = nome_paciente
        self.data = data
        self.horario = horario
        self.cargo_medico = cargo_medico
        self.medico = medico
        self.descricao = descricao

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Consulta(
            data["nome_paciente"],
            data["data"],
            data["horario"],
            data["cargo_medico"],
            data["medico"],
            data["descricao"]
        )

def main(page: ft.Page):
    # Lista para armazenar consultas
    consultas = []

    # Dicionário de médicos por cargo
    medicos_por_cargo = {
        "Cardiologista": ["Dr. João", "Dra. Maria"],
        "Pediatra": ["Dr. Clara", "Dr. Pedro"],
        "Dermatologista": ["Dra. Ana", "Dr. Marcos"],
        "Ortopedista": ["Dr. Lucas", "Dr. Helena"],
        "Clínico Geral": ["Dr. Fernando", "Dra. Paula"],
        "Neurologista": ["Dr. Roberto", "Dra. Juliana"],
        "Oftalmologista": ["Dr. Carlos", "Dra. Sofia"]
    }

    # Carregar dados salvos
    def carregar_consultas():
        try:
            with open("consultas.json", "r") as f:
                dados = json.load(f)
                for c in dados:
                    consultas.append(Consulta.from_dict(c))
        except FileNotFoundError:
            pass

    # Salvar dados em JSON
    def salvar_consultas():
        with open("consultas.json", "w") as f:
            json.dump([c.to_dict() for c in consultas], f)

    # Atualiza a exibição das consultas
    def atualizar_lista():
        lista_consultas.controls.clear()
        for i, consulta in enumerate(consultas):
            lista_consultas.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Paciente: {consulta.nome_paciente}"),
                    subtitle=ft.Text(
                        f"Data: {consulta.data} | Horário: {consulta.horario}\n"
                        f"Cargo Médico: {consulta.cargo_medico} | Médico: {consulta.medico}\n"
                        f"Descrição: {consulta.descricao}"
                    ),
                    trailing=ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="Excluir",
                        on_click=lambda e, index=i: excluir_consulta(index)
                    ),
                )
            )
        page.update()

    # Função para adicionar uma nova consulta
    def adicionar_consulta(e):
        if not nome_paciente.value or not data.value or not horario.value or not cargo_medico.value or not medico.value:
            mensagem_erro.value = "Preencha todos os campos obrigatórios!"
            mensagem_erro.visible = True
            page.update()
            return
        mensagem_erro.visible = False

        # Cria uma nova consulta e adiciona à lista
        nova_consulta = Consulta(
            nome_paciente.value,
            data.value,
            horario.value,
            cargo_medico.value,
            medico.value,
            descricao.value
        )
        consultas.append(nova_consulta)

        # Salva os dados
        salvar_consultas()

        # Limpa os campos
        nome_paciente.value = ""
        data.value = ""
        horario.value = ""
        cargo_medico.value = None
        medico.value = None
        descricao.value = ""

        # Atualiza a exibição
        atualizar_lista()

    # Função para excluir uma consulta
    def excluir_consulta(index):
        consultas.pop(index)
        salvar_consultas()
        atualizar_lista()

    # Função para filtrar consultas
    def filtrar_consultas(e):
        lista_consultas.controls.clear()
        for i, consulta in enumerate(consultas):
            if filtro_cargo.value and filtro_cargo.value != consulta.cargo_medico:
                continue
            lista_consultas.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Paciente: {consulta.nome_paciente}"),
                    subtitle=ft.Text(
                        f"Data: {consulta.data} | Horário: {consulta.horario}\n"
                        f"Cargo Médico: {consulta.cargo_medico} | Médico: {consulta.medico}\n"
                        f"Descrição: {consulta.descricao}"
                    ),
                    trailing=ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="Excluir",
                        on_click=lambda e, index=i: excluir_consulta(index)
                    ),
                )
            )
        page.update()

    # Atualizar médicos ao selecionar cargo
    def atualizar_medicos(e):
        medico.options = [ft.dropdown.Option(m) for m in medicos_por_cargo.get(cargo_medico.value, [])]
        medico.value = None
        page.update()

    # Componentes da interface
    nome_paciente = ft.TextField(label="Nome do Paciente", expand=True)
    data = ft.TextField(label="Data (DD/MM/AAAA)", expand=True, keyboard_type="number")
    horario = ft.TextField(label="Horário (HH:MM)", expand=True, keyboard_type="number")
    cargo_medico = ft.Dropdown(
        label="Cargo Médico",
        options=[ft.dropdown.Option(cargo) for cargo in medicos_por_cargo.keys()],
        expand=True,
        on_change=atualizar_medicos
    )
    medico = ft.Dropdown(label="Selecione o Médico", expand=True)
    descricao = ft.TextField(label="Descrição", multiline=True, expand=True)
    mensagem_erro = ft.Text(value="", color=ft.colors.RED, visible=False)
    filtro_cargo = ft.Dropdown(
        label="Filtrar por Cargo Médico",
        options=[ft.dropdown.Option(cargo) for cargo in medicos_por_cargo.keys()],
        expand=True
    )
    botao_filtrar = ft.ElevatedButton("Filtrar", on_click=filtrar_consultas)
    lista_consultas = ft.Column()

    # Layout principal
    page.title = "Gerenciamento de Consultas"
    page.add(
        ft.Column(
            [
                ft.Image(src="unimed_logo.png.png", width=150, height=50),
                ft.Text("Cadastrar Consulta", style="headlineMedium"),
                nome_paciente,
                data,
                horario,
                cargo_medico,
                medico,
                descricao,
                ft.ElevatedButton("Adicionar Consulta", on_click=adicionar_consulta),
                mensagem_erro,
                ft.Divider(),
                ft.Text("Filtrar Consultas", style="headlineSmall"),
                ft.Row([filtro_cargo, botao_filtrar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(),
                ft.Text("Consultas Cadastradas", style="headlineSmall"),
                lista_consultas,
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )
    )

    # Carregar dados e atualizar lista
    carregar_consultas()
    atualizar_lista()

# Executa o app
ft.app(target=main)
