import flet as ft
from flet import controls

from paleta_colores import *

def main(page : ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK


area_principal = ft.Container (
    expand= True,
    padding = 30,
)
 page.add(area_principal)
 dashboard=ft.Column (
     expand=True,
     spacing =20,
     scroll=ft.ScrollMode.AUTO
 )
 area_principal.content=dashboard

 titulo= ft.Text("Dashboard Principal",
                 size=30,
                 weight=ft.FontWeight.BOLD,
                 color=COLOR_TEXTO_PRINCIPAL)
 subtitulo = ft.Text("Supervision general del proceso -Smart-Sort",
                     size=13,
                     color = COLOR_TEXTO_SECUNDARIO
                    )
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





ft.run(main)
