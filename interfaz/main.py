import flet as ft
import random
from navegacion import crear_navegacion
from graficas import crear_grafica
from paleta_colores import *

def main(page : ft.Page):
    page.title = "Smart-Sort - Panel de Supervisión"
    page.window.width = 1200
    page.window.height = 720
    page.window.min_width = 900
    page.window.min_height = 600
    page.bgcolor = COLOR_FONDO_OSCURO
    page.theme_mode = ft.ThemeMode.DARK

    sistema_en_marcha = False
    conteo = {
        "rojos": 0,
        "verdes": 0,
        "azules": 0,
    }

    def cambiar_seccion(e):
        indice = e.control.selected_index
        print(f"Cambiando a la seccion: {indice}")

    def alternar_marcha(e: ft.ControlEvent):
        nonlocal sistema_en_marcha
        sistema_en_marcha = not sistema_en_marcha

        if sistema_en_marcha:
            val_estado_sistema.value = "En Marcha"
            val_estado_sistema.color = COLOR_VERDE_EN_MARCHA

            boton_marcha.content = "Detener Sistema"
            boton_marcha.icon = ft.Icons.STOP
            boton_marcha.bgcolor = COLOR_OBJETO_ROJO

            boton_simular.disabled = False
        else:
            val_estado_sistema.value = "Detenido"
            val_estado_sistema.color = COLOR_NARANJA_ADVERTENCIA

            boton_marcha.content = "Iniciar Sistema"
            boton_marcha.icon = ft.Icons.PLAY_ARROW
            boton_marcha.bgcolor = COLOR_VERDE_EN_MARCHA

            boton_simular.disabled = True

        page.update()

    def simular_deteccion(e: ft.ControlEvent):
        if not sistema_en_marcha:
            return

        opcion = random.choice(["Rojo", "Verde", "Azul"])

        if opcion == "Rojo":
            conteo["rojos"] += 1
            valor_color.value = "Rojo"
            valor_color.color = COLOR_OBJETO_ROJO

        elif opcion == "Verde":
            conteo["verdes"] += 1
            valor_color.value = "Verde"
            valor_color.color = COLOR_OBJETO_VERDE

        else:
            conteo["azules"] += 1
            valor_color.value = "Azul"
            valor_color.color = COLOR_OBJETO_AZUL


        total_actual = conteo["rojos"] + conteo["verdes"] + conteo["azules"]
        valor_procesados.value = str(total_actual)

        contenedor_grafica.content = crear_grafica(
            rojos=conteo["rojos"],
            verdes=conteo["verdes"],
            azules=conteo["azules"],
        )

        page.update()

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

    encabezado_texto = ft.Column ( spacing = 3,
                          controls = [titulo, subtitulo],)

    boton_marcha = ft.Button(
        content = "Iniciar Sistema",
        icon = ft.Icons.PLAY_ARROW,
        bgcolor = COLOR_VERDE_EN_MARCHA,
        color = COLOR_TEXTO_PRINCIPAL,
        on_click = alternar_marcha

    )

    boton_simular = ft.Button(
        content = "Simular Objeto",
        icon = ft.Icons.ADD_CIRCLE_OUTLINE,
        bgcolor = COLOR_AZUL_PRINCIPAL,
        color = COLOR_TEXTO_PRINCIPAL,
        on_click = simular_deteccion
    )

    botones_accion = ft.Row(
        spacing = 10,
        controls = [boton_marcha, boton_simular]
    )

    encabezado = ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls = [encabezado_texto, botones_accion]
    )

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
        "Detenido",
        size = 22,
        weight = ft.FontWeight.BOLD,
        color = COLOR_NARANJA_ADVERTENCIA
    )

    valor_color = ft.Text(
        "Ninguno",
        size = 22,
        weight = ft.FontWeight.BOLD,
        color = COLOR_TEXTO_SECUNDARIO
    )

    valor_procesados = ft.Text(
        "0",
        size = 26,
        weight = ft.FontWeight.BOLD,
        color = COLOR_TEXTO_PRINCIPAL
    )

    val_mqtt = ft.Text(
        "Simulación",
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
            crear_kpi("MODO DE DATOS", val_mqtt, ft.Icons.SCIENCE, COLOR_AZUL_PRINCIPAL)
        ]
    )
    dashboard.controls.append(tarjetas_kpi)

    contenedor_grafica = ft.Container(
        content = crear_grafica(
            rojos = conteo["rojos"],
            verdes = conteo["verdes"],
            azules = conteo["azules"],
        )
    )
    dashboard.controls.append(contenedor_grafica)

ft.run(main)
