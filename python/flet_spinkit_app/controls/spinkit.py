from typing import Any, Optional, Union

from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import ResponsiveNumber


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
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        rtl: Optional[bool] = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            disabled=disabled,
            rtl=rtl,
            data=data,
        )

    def _get_control_name(self):
        return "spinkit"
