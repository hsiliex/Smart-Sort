import flet as ft

from interfaz.estilos import (
    COLOR_TEXTO_PRINCIPAL,COLOR_TEXTO_SECUNDARIO,
    COLOR_AZUL_PRINCIPAL)

def crear_tabla ():

    tabla= ft.DataTable(
        columns= [
            ft.DataColumn(
                ft.Text("N.°",
         color =COLOR_AZUL_PRINCIPAL)
            ),
            ft.DataColumn (
                ft.Text("Color",
            color =COLOR_AZUL_PRINCIPAL)
            ),
            ft.Datacolumn(
                FT.Text("clasificacion",
            COLOR_AZUL_PRINCIPAL)
            ),
            ft.DataColumn(
                ft.Text("Hora",
            color = COLOR_AZUL_PRINCIPAL)
            )
        ],
        rows=[]
        heading_row_height=45,
        data_row_min_height=45,
        column_spacing=25
    )
    return tabla
##### funciones para agregar un registro

def agregar_registro(tabla,numero,color,hora):

    fila = ft.DataRow(
        cells=[
            ft.DataCell(
                ft.Text(str(numero),
            color= COLOR_TEXTO_PRINCIPAL)
            ),
            ft.DataCell(
                ft.Text("Clasificado",
            COLOR =COLOR_TEXTO_SECUNDARIO)
            )
        ]
    )
    tabla.rows.append(fila)