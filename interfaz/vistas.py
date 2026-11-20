import flet as ft
from paleta_colores import *


def crear_vista_control(
    estado_control,
    boton_marcha_control,
    boton_reiniciar,
    texto_velocidad,
    slider_velocidad,
    dropdown_modo,
):
    return ft.Column(
        expand = True,
        spacing = 20,
        scroll = ft.ScrollMode.AUTO,
        controls = [
            ft.Text(
                "Control y Motor",
                size = 30,
                weight = ft.FontWeight.BOLD,
                color = COLOR_TEXTO_PRINCIPAL,
            ),
            ft.Container(
                bgcolor = COLOR_SUPERFICIE_PANEL,
                padding = 25,
                border_radius = 15,
                content = ft.Column(
                    spacing = 15,
                    controls = [
                        ft.Text(
                            "Estado de marcha y pruebas",
                            size = 20,
                            weight = ft.FontWeight.BOLD,
                            color = COLOR_TEXTO_PRINCIPAL,
                        ),
                        ft.Text(
                            "Controle el estado general de la simulación o reinicie los contadores.",
                            color = COLOR_TEXTO_SECUNDARIO,
                        ),
                        estado_control,
                        ft.Row(
                            spacing = 10,
                            wrap = True,
                            controls = [
                                boton_marcha_control,
                                boton_reiniciar,
                            ],
                        ),
                    ],
                ),
            ),
            ft.Container(
                bgcolor = COLOR_SUPERFICIE_PANEL,
                padding = 25,
                border_radius = 15,
                content = ft.Column(
                    spacing = 12,
                    controls = [
                        ft.Text(
                            "Parámetros simulados del motor y clasificación",
                            size = 20,
                            weight = ft.FontWeight.BOLD,
                            color = COLOR_TEXTO_PRINCIPAL,
                        ),
                        texto_velocidad,
                        slider_velocidad,
                        ft.Text(
                            "Modo de simulación de color:",
                            color = COLOR_TEXTO_SECUNDARIO,
                        ),
                        dropdown_modo,
                        ft.Text(
                            "Nota: Sin conexión física al ESP32; valores de prueba local.",
                            size = 12,
                            color = COLOR_TEXTO_SECUNDARIO,
                        ),
                    ],
                ),
            ),
        ],
    )


def crear_vista_eventos(lista_eventos):
    return ft.Column(
        expand = True,
        spacing = 15,
        scroll = ft.ScrollMode.AUTO,
        controls = [
            ft.Text(
                "Eventos y Alertas",
                size = 30,
                weight = ft.FontWeight.BOLD,
                color = COLOR_TEXTO_PRINCIPAL,
            ),
            ft.Container(
                bgcolor = COLOR_SUPERFICIE_PANEL,
                padding = 20,
                border_radius = 15,
                content = lista_eventos,
            ),
        ],
    )