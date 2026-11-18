import flet as ft
from flet import controls
from flet.controls import border_radius

from navegacion import crear_navegacion
from paleta_colores import *

def main(page : ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK

    def cambiar_seccion(e):
        indice = e.control.selected_index
        print(f"Cambiando a la seccion: {indice}")

    barra_lateral = ft.Container(
        width = 230,
        bgcolor = COLOR_SUPERFICIE_PANEL,
        padding = 20,
        border_radius = 15
    )

    area_principal = ft.Container(
        expand= True,
        padding = 30,
    )

    estructura = ft.Row(
        expand = True,
        spacing = 0,
        controls = [barra_lateral, area_principal]
    )

    page.add(estructura)

    barra_lateral.content = crear_navegacion(cambiar_seccion)

    dashboard = ft.Column(
        expand = True,
        spacing = 20,
        scroll = ft.ScrollMode.AUTO
    )
    area_principal.content=dashboard

    titulo= ft.Text("Dashboard Principal",
                 size=30,
                 weight=ft.FontWeight.BOLD,
                 color=COLOR_TEXTO_PRINCIPAL)
    subtitulo = ft.Text("Supervision general del proceso - Smart-Sort",
                     size=13,
                     color = COLOR_TEXTO_SECUNDARIO)

    encabezado = ft.Column ( spacing = 3,
                          controls = [titulo, subtitulo],)

    dashboard.controls.append(encabezado)

    def crear_kpi(titulo_kpi,valor_ctrl,icono, color_icono):
        return ft.Container (
        expand=1,
        bgcolor= COLOR_SUPERFICIE_PANEL,
        padding= 20,
        border_radius = 16,
        content = ft.Row (
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            controls = [
                ft.Column (
                    spacing = 5,
                    controls = [
                        ft.Text(titulo_kpi,
                                color= COLOR_TEXTO_SECUNDARIO,
                                size=12),
                          valor_ctrl
                    ]
                ),
                ft.Icon(icono,color = color_icono,size =32)
            ]
        )
    )

    val_estado_sistema = ft.Text(
        "En Marcha",
        size = 22,
        weight = ft.FontWeight.BOLD,
        color = COLOR_VERDE_EN_MARCHA
    )

    valor_color = ft.Text(
        "Rojo",
        size = 22,
        weight = ft.FontWeight.BOLD,
        color = COLOR_OBJETO_ROJO
    )

    valor_procesados = ft.Text(
        "142",
        size = 26,
        weight = ft.FontWeight.BOLD,
        color = COLOR_TEXTO_PRINCIPAL
    )

    val_mqtt = ft.Text(
        "Conectado",
        size = 22,
        weight = ft.FontWeight.BOLD,
        color = COLOR_AZUL_PRINCIPAL
    )

    tarjetas_kpi = ft.Row(
        spacing = 15,
        controls = [
            crear_kpi("ESTADO SISTEMA", val_estado_sistema, ft.Icons.POWER_SETTINGS_NEW, COLOR_VERDE_EN_MARCHA),
            crear_kpi("ULTIMO COLOR", valor_color, ft.Icons.PALETTE, COLOR_OBJETO_ROJO),
            crear_kpi("TOTAL PROCESADOS", valor_procesados, ft.Icons.FACTORY, COLOR_NARANJA_ADVERTENCIA),
            crear_kpi("ESTADO MQTT", val_mqtt, ft.Icons.WIFI, COLOR_AZUL_PRINCIPAL)
        ]
    )
    dashboard.controls.append(tarjetas_kpi)

ft.run(main)
