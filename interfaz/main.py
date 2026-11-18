import flet as ft
from paleta_colores import *

def main(page : ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK

ft.run(main)
