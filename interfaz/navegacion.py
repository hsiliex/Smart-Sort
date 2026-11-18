import flet as ft
from paleta_colores import *

def crear_navegacion(cambiar_seccion, logo = None):
    return ft.NavigationRail(
        selected_index = 0,
        extended = True,
        min_extended_width = 210,
        bgcolor = COLOR_SUPERFICIE_PANEL,
        leading = logo,
        on_change = cambiar_seccion,
        destinations = [
            ft.NavigationRailDestination(
                icon = ft.Icons.DASHBOARD_OUTLINED,
                selected_icon = ft.Icons.DASHBOARD,
                label = "Dashboard",
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.TUNE,
                label = "Control y Motor",
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.LIST_ALT,
                label = "Eventos y Alertas",
            )
        ]
    )