import flet as ft
from paleta_colores import *

MAX_FILAS_VISIBLES = 6

def crear_tabla ():
    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("N.°", color=COLOR_AZUL_PRINCIPAL)),
            ft.DataColumn(ft.Text("Color", color=COLOR_AZUL_PRINCIPAL)),
            ft.DataColumn(ft.Text("Clasificación", color=COLOR_AZUL_PRINCIPAL)),
            ft.DataColumn(ft.Text("Hora", color=COLOR_AZUL_PRINCIPAL))
        ],
        rows=[],
        heading_row_height=45,
        data_row_min_height=45,
        column_spacing=25
    )

##### funciones para agregar un registro

def agregar_registro(tabla, numero, color, hora):

    fila = ft.DataRow(
        cells=[
            ft.DataCell(ft.Text(str(numero),color= COLOR_TEXTO_PRINCIPAL)),
            ft.DataCell(ft.Text(color.capitalize(), color= COLOR_TEXTO_PRINCIPAL)),
            ft.DataCell(ft.Text("Clasificado", color=COLOR_TEXTO_SECUNDARIO)),
            ft.DataCell(ft.Text(hora,color= COLOR_TEXTO_SECUNDARIO)
            )
        ]
    )
    tabla.rows.insert(0, fila)
    if len(tabla.rows) > MAX_FILAS_VISIBLES:
        tabla.rows.pop()