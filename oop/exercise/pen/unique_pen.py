from oop.exercise.pen import Pen


class UniquePen(Pen):
    PEN_TYPES = ("ball pen", "fountain pen", "golden pen")

    def __init__(self, pen_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pen_type = self._set_pen_type(pen_type)

    def _set_pen_type(self, pen_type):
        if pen_type not in self.PEN_TYPES:
            raise ValueError(f"{pen_type} is not a Unique one.")
        return pen_type
