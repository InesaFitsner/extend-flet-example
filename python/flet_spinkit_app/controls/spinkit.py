from typing import Any, Optional

from flet_core.control import Control, OptionalNumber


class Spinkit(Control):
    """
    Spinkit Control.
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
        )

    def _get_control_name(self):
        return "spinkit"
