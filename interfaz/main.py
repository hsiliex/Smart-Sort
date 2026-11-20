import flet as ft
from pathlib import Path
import random
from datetime import datetime
from navegacion import crear_navegacion
from paleta_colores import *
from graficas import crear_grafica
from tablas import crear_tabla, agregar_registro
from vistas import crear_vista_control, crear_vista_eventos


def main(page: ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    ruta_icono = Path(__file__).parent/"assets"/"icon.ico"
    if ruta_icono.exists():
        page.window.icon = str(ruta_icono)

    rojos = 0
    verdes = 0
    azules = 0
    total = 0
    sistema_en_marcha = False
    ultimo_color = "Ninguno"
    eventos_registrados = []

    tabla = crear_tabla()

    val_estado_sistema = ft.Text(
        "Detenido",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=COLOR_ROJO_PELIGRO
    )

    estado_control = ft.Text(
        "Detenido",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=COLOR_ROJO_PELIGRO
    )

    valor_color = ft.Text(
        "Ninguno",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TEXTO_SECUNDARIO
    )

    valor_procesados = ft.Text(
        "0",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TEXTO_PRINCIPAL
    )

    val_mqtt = ft.Text(
        "Simulación",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=COLOR_AZUL_PRINCIPAL
    )

    lista_eventos = ft.Column(
        spacing=8,
        scroll=ft.ScrollMode.AUTO
    )

    def registrar_evento(mensaje):
        hora = datetime.now().strftime("%H:%M:%S")
        eventos_registrados.insert(0, f"[{hora}] {mensaje}")
        if len(eventos_registrados) > 20:
            eventos_registrados.pop()

        lista_eventos.controls.clear()
        for evento in eventos_registrados:
            lista_eventos.controls.append(
                ft.Text(
                    evento,
                    color=COLOR_TEXTO_PRINCIPAL,
                    size=13
                )
            )

    def actualizar_apariencia_marcha():
        if sistema_en_marcha:
            texto_estado = "En Marcha"
            color_estado = COLOR_VERDE_EN_MARCHA
            texto_boton = "Detener sistema"
            icono_boton = ft.Icons.STOP
            color_boton = COLOR_ROJO_PELIGRO
            boton_simular.disabled = False
        else:
            texto_estado = "Detenido"
            color_estado = COLOR_ROJO_PELIGRO
            texto_boton = "Iniciar sistema"
            icono_boton = ft.Icons.PLAY_ARROW
            color_boton = COLOR_VERDE_EN_MARCHA
            boton_simular.disabled = True

        val_estado_sistema.value = texto_estado
        val_estado_sistema.color = color_estado
        estado_control.value = texto_estado
        estado_control.color = color_estado

        for btn in (boton_marcha, boton_marcha_control):
            if isinstance(btn.content, ft.Text):
                btn.content.value = texto_boton
            else:
                btn.content = texto_boton
            btn.icon = icono_boton
            btn.bgcolor = color_boton

    def alternar_marcha(e):
        nonlocal sistema_en_marcha
        sistema_en_marcha = not sistema_en_marcha
        actualizar_apariencia_marcha()

        if sistema_en_marcha:
            registrar_evento("Sistema iniciado")
        else:
            registrar_evento("Sistema detenido")

        page.update()

    def reiniciar_contadores(e):
        nonlocal rojos, verdes, azules, total, ultimo_color
        rojos = 0
        verdes = 0
        azules = 0
        total = 0
        ultimo_color = "Ninguno"

        valor_color.value = ultimo_color
        valor_color.color = COLOR_TEXTO_SECUNDARIO
        valor_procesados.value = "0"
        tabla.rows.clear()
        contenedor_grafica.content = crear_grafica(rojos, verdes, azules)

        registrar_evento("Contadores y tabla reiniciados")
        page.update()

    def elegir_color_simulado():
        modo = dropdown_modo.value
        if modo == "Solo Rojo":
            return "Rojo"
        elif modo == "Solo Verde":
            return "Verde"
        elif modo == "Solo Azul":
            return "Azul"
        else:
            return random.choice(["Rojo", "Verde", "Azul"])

    def simular_objeto(e):
        nonlocal rojos, verdes, azules, total, ultimo_color

        if not sistema_en_marcha:
            registrar_evento("No se puede clasificar: sistema detenido")
            page.update()
            return

        color_detectado = elegir_color_simulado()

        if color_detectado == "Rojo":
            rojos += 1
            valor_color.color = COLOR_OBJETO_ROJO
        elif color_detectado == "Verde":
            verdes += 1
            valor_color.color = COLOR_OBJETO_VERDE
        else:
            azules += 1
            valor_color.color = COLOR_OBJETO_AZUL

        total += 1
        ultimo_color = color_detectado

        valor_color.value = ultimo_color
        valor_procesados.value = str(total)

        contenedor_grafica.content = crear_grafica(
            rojos,
            verdes,
            azules
        )

        hora = datetime.now().strftime("%H:%M:%S")
        agregar_registro(
            tabla,
            total,
            color_detectado,
            hora
        )

        registrar_evento(
            f"Objeto {total} clasificado: {color_detectado}"
        )

        page.update()

    def cambiar_velocidad(e):
        vel = int(slider_velocidad.value)
        texto_velocidad.value = f"Velocidad simulada de banda: {vel}%"
        page.update()

    def crear_kpi(titulo_kpi, valor_ctrl, icono, color_icono):
        return ft.Container(
            expand=1,
            bgcolor=COLOR_SUPERFICIE_PANEL,
            padding=20,
            border_radius=16,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        spacing=5,
                        controls=[
                            ft.Text(
                                titulo_kpi,
                                color=COLOR_TEXTO_SECUNDARIO,
                                size=12
                            ),
                            valor_ctrl
                        ]
                    ),
                    ft.Icon(
                        icono,
                        color=color_icono,
                        size=32
                    )
                ]
            )
        )

    tarjetas_kpi = ft.Row(
        spacing=15,
        controls=[
            crear_kpi(
                "ESTADO SISTEMA",
                val_estado_sistema,
                ft.Icons.POWER_SETTINGS_NEW,
                COLOR_VERDE_EN_MARCHA
            ),
            crear_kpi(
                "ÚLTIMO COLOR",
                valor_color,
                ft.Icons.PALETTE,
                COLOR_OBJETO_ROJO
            ),
            crear_kpi(
                "TOTAL PROCESADOS",
                valor_procesados,
                ft.Icons.FACTORY,
                COLOR_NARANJA_ADVERTENCIA
            ),
            crear_kpi(
                "ESTADO MQTT",
                val_mqtt,
                ft.Icons.WIFI,
                COLOR_AZUL_PRINCIPAL
            )
        ]
    )

    boton_marcha = ft.FilledButton(
        "Iniciar sistema",
        icon=ft.Icons.PLAY_ARROW,
        bgcolor=COLOR_VERDE_EN_MARCHA,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=alternar_marcha
    )

    boton_marcha_control = ft.FilledButton(
        "Iniciar sistema",
        icon=ft.Icons.PLAY_ARROW,
        bgcolor=COLOR_VERDE_EN_MARCHA,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=alternar_marcha
    )

    boton_simular = ft.FilledButton(
        "Simular objeto",
        icon=ft.Icons.ADD,
        bgcolor=COLOR_AZUL_PRINCIPAL,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=simular_objeto,
        disabled=True
    )

    boton_reiniciar = ft.FilledButton(
        "Reiniciar conteo",
        icon=ft.Icons.RESTART_ALT,
        bgcolor=COLOR_NARANJA_ADVERTENCIA,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=reiniciar_contadores
    )

    texto_velocidad = ft.Text(
        "Velocidad simulada de banda: 50%",
        color=COLOR_TEXTO_PRINCIPAL
    )

    slider_velocidad = ft.Slider(
        min=0,
        max=100,
        divisions=10,
        value=50,
        label="{value}%",
        on_change=cambiar_velocidad
    )

    dropdown_modo = ft.Dropdown(
        value="Aleatorio",
        options=[
            ft.dropdown.Option("Aleatorio"),
            ft.dropdown.Option("Solo Rojo"),
            ft.dropdown.Option("Solo Verde"),
            ft.dropdown.Option("Solo Azul"),
        ]
    )

    contenedor_grafica = ft.Container(
        content=crear_grafica(rojos, verdes, azules)
    )

    contenedor_tabla = ft.Container(
        bgcolor=COLOR_SUPERFICIE_PANEL,
        padding=15,
        border_radius=15,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Últimos registros",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=COLOR_TEXTO_PRINCIPAL
                ),
                tabla
            ],
            spacing=10
        )
    )

    dashboard = ft.Column(
        expand=True,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Column(
                spacing=3,
                controls=[
                    ft.Text(
                        "Dashboard",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=COLOR_TEXTO_PRINCIPAL
                    ),
                    ft.Text(
                        "Supervisión general del proceso - Smart-Sort",
                        size=13,
                        color=COLOR_TEXTO_SECUNDARIO
                    )
                ]
            ),
            tarjetas_kpi,
            ft.Row(
                controls=[
                    boton_marcha,
                    boton_simular
                ],
                spacing=10,
                wrap=True
            ),
            contenedor_grafica,
            contenedor_tabla
        ]
    )

    vista_control = crear_vista_control(
        estado_control,
        boton_marcha_control,
        boton_reiniciar,
        texto_velocidad,
        slider_velocidad,
        dropdown_modo,
    )

    vista_eventos = crear_vista_eventos(lista_eventos)

    area_principal = ft.Container(
        expand=True,
        padding=30,
        content=dashboard
    )

    def cambiar_seccion(e):
        indice = e.control.selected_index

        if indice == 0:
            area_principal.content = dashboard
        elif indice == 1:
            area_principal.content = vista_control
        elif indice == 2:
            area_principal.content = vista_eventos

        page.update()

    barra_lateral = ft.Container(
        width=230,
        bgcolor=COLOR_SUPERFICIE_PANEL,
        padding=10,
        border_radius=15,
        content=crear_navegacion(cambiar_seccion)
    )

    estructura = ft.Row(
        expand=True,
        spacing=0,
        controls=[
            barra_lateral,
            area_principal
        ]
    )

    page.add(estructura)

    registrar_evento("Interfaz iniciada en modo simulación")
    page.update()


ft.run(main, assets_dir = "assets")