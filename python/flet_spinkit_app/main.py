import flet as ft
from controls.spinkit import Spinkit


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(Spinkit(opacity=0.5))


ft.app(main)
