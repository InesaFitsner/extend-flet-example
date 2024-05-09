from flet_core.control import Control


class Spinkit(Control):
    """
    Spinkit Control.
    """

    def __init__(self):
        Control.__init__(self)

    def _get_control_name(self):
        return "spinkit"
