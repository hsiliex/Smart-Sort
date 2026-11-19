import flet as ft
from flet.controls import alignment

from interfaz.estilos import (
    COLOR_OBJETO_ROJO,COLOR_OBJETO_VERDE,COLOR_OBJETO_AZUL,
    COLOR_TEXTO_PRINCIPAL,COLOR_TEXTO_SECUNDARIO )

def crear_barra_color(nombre,cantidad,color,porcentaje):

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.text(nombre,color=COLOR_TEXTO_PRINCIPAL),
                    ft.Text(
                        f"{cantidad} objetos",
                        color = COLOR_TEXTO_SECUNDARIO
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Progressbar(
                value=porcentaje,
                color=color,
                bgcolor="424242",
                height=10
            )
        ],
        spacing = 8
    )

def crear_grafica(rojos, verdes, azules):
   total= rojo+verde+azul

   if total == 0:
       porcentaje_rojo = 0
       porcentaje_verde = 0
       porcentaje_azul = 0
   else:
       porcentaje_rojo = rojos / total
       porcentaje_verde = verdes / total
       porcentaje_azul = azules / total


    return ft.Column(
        controls=[
            ft.Text(
                "clasificaicon de objetos",
                size=18,
                weight=ft.FontWeight.BOLD,
                color = COLOR_TEXTO_PRINCIPAL
            ),
            crear_barra_color(
                "Rojo",rojos,COLOR_OBJETO_ROJO, porcentaje_rojo
            ),
            crear_barra_color(
                "Verde", verdes, COLOR_OBJETO_VERDE, porcentaje_verde
            ),
            crear_barra_color(
                "Azul", azules, COLOR_OBJETO_AZUL, porcentaje_azul
            )
        ],
        spacing = 18
    )