from typing import Any, Optional

import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref


class Spinkit(Control):
    """
    Spinkit Control
    """

    def __init__(
        self,
        color: Optional[str] = None,
        #
        # Control
        #
        ref: Optional[Ref] = None,
        opacity: OptionalNumber = None,
        visible: Optional[bool] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            opacity=opacity,
            visible=visible,
            data=data,
        )

        self.color = color

    def _get_control_name(self):
        return "spinkit"

    # color
    @property
    def color(self):
        return self._get_attr("color")

    @color.setter
    def color(self, value):
        self._set_attr("color", value)


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(Spinkit(color=ft.colors.AMBER))


ft.app(main)
