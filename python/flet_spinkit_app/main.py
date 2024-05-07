from typing import Any, Optional

import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref


class Spinkit(Control):
    """
    Spinkit Control.
    """

    def __init__(
        self,
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

    def _get_control_name(self):
        return "spinkit"


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(Spinkit())


ft.app(main)
