import flet as ft
import random
from datetime import datetime

from navegacion import crear_navegacion
from paleta_colores import *
from graficas import crear_grafica
from tablas import crear_tabla, agregar_registro


def main(page: ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10

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

        lista_eventos.controls.clear()

        for evento in eventos_registrados:
            lista_eventos.controls.append(
                ft.Text(
                    evento,
                    color=COLOR_TEXTO_PRINCIPAL,
                    size=13
                )
            )

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

    def iniciar_sistema(e):
        nonlocal sistema_en_marcha

        sistema_en_marcha = True

        val_estado_sistema.value = "En Marcha"
        val_estado_sistema.color = COLOR_VERDE_EN_MARCHA

        estado_control.value = "En Marcha"
        estado_control.color = COLOR_VERDE_EN_MARCHA

        registrar_evento("Sistema iniciado")
        page.update()

    def detener_sistema(e):
        nonlocal sistema_en_marcha

        sistema_en_marcha = False

        val_estado_sistema.value = "Detenido"
        val_estado_sistema.color = COLOR_ROJO_PELIGRO

        estado_control.value = "Detenido"
        estado_control.color = COLOR_ROJO_PELIGRO

        registrar_evento("Sistema detenido")
        page.update()

    def simular_objeto(e):
        nonlocal rojos, verdes, azules, total, ultimo_color

        if sistema_en_marcha == False:
            registrar_evento(
                "No se puede clasificar: sistema detenido"
            )
            page.update()
            return

        color_detectado = random.choice(
            ["Rojo", "Verde", "Azul"]
        )

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

    boton_iniciar = ft.FilledButton(
        content=ft.Text("Iniciar sistema"),
        icon=ft.Icons.PLAY_ARROW,
        bgcolor=COLOR_VERDE_EN_MARCHA,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=iniciar_sistema
    )

    boton_simular = ft.FilledButton(
        "Simular objeto",
        icon=ft.Icons.ADD,
        bgcolor=COLOR_AZUL_PRINCIPAL,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=simular_objeto
    )

    boton_detener = ft.FilledButton(
        "Detener sistema",
        icon=ft.Icons.STOP,
        bgcolor=COLOR_ROJO_PELIGRO,
        color=COLOR_TEXTO_PRINCIPAL,
        on_click=detener_sistema
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
                        "Dashboard Principal",
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
                    boton_iniciar,
                    boton_simular,
                    boton_detener
                ],
                spacing=10,
                wrap=True
            ),
            contenedor_grafica,
            contenedor_tabla
        ]
    )

    pantalla_control = ft.Column(
        expand=True,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Text(
                "Control y Motor",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=COLOR_TEXTO_PRINCIPAL
            ),
            ft.Container(
                bgcolor=COLOR_SUPERFICIE_PANEL,
                padding=25,
                border_radius=15,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text(
                            "Control del sistema",
                            size=20,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Utilice los botones para controlar la simulación.",
                            color=COLOR_TEXTO_SECUNDARIO
                        ),
                        estado_control,
                        ft.Row(
                            controls=[
                                ft.FilledButton(
                                    "Iniciar",
                                    icon=ft.Icons.PLAY_ARROW,
                                    bgcolor=COLOR_VERDE_EN_MARCHA,
                                    on_click=iniciar_sistema
                                ),
                                ft.FilledButton(
                                    "Detener",
                                    icon=ft.Icons.STOP,
                                    bgcolor=COLOR_ROJO_PELIGRO,
                                    on_click=detener_sistema
                                ),
                                ft.FilledButton(
                                    "Simular objeto",
                                    icon=ft.Icons.ADD,
                                    bgcolor=COLOR_AZUL_PRINCIPAL,
                                    on_click=simular_objeto
                                )
                            ],
                            wrap=True
                        )
                    ]
                )
            ),
            ft.Container(
                bgcolor=COLOR_SUPERFICIE_PANEL,
                padding=25,
                border_radius=15,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Estado del motor",
                            size=20,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Motor simulado - sin conexión física",
                            color=COLOR_TEXTO_SECUNDARIO
                        )
                    ]
                )
            )
        ]
    )

    pantalla_eventos = ft.Column(
        expand=True,
        spacing=15,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Text(
                "Eventos y Alertas",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=COLOR_TEXTO_PRINCIPAL
            ),
            ft.Container(
                bgcolor=COLOR_SUPERFICIE_PANEL,
                padding=20,
                border_radius=15,
                content=lista_eventos
            )
        ]
    )

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
            area_principal.content = pantalla_control
        elif indice == 2:
            area_principal.content = pantalla_eventos

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


ft.run(main)