class Pen:
    COLORS = {
        "YELLOW": (255, 255, 0),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
    }

    def __init__(self, brand: str, capacity: int, color: str, pen_id: int):
        self.id = pen_id
        self.brand = brand
        self.capacity = capacity
        self.color = color.upper()

    def write(self, string):
        if len(string) > self.capacity:
            print("Not enough ink")
            return

        self.capacity -= len(string)
        self.color_printer(self.color, string)

    @classmethod
    def color_printer(cls, color, text):
        try:
            r, g, b = cls.COLORS[color]
            print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        except KeyError:
            print(text)

    def __str__(self):
        return f"I am {self.color} color pen. I have ink for {self.capacity} more chars"


if __name__ == "__main__":
    PEN_MAKES = ["Mont Blanc", "Cross", "Parker", "Reynolds", "NoName"]
    pen1 = Pen(PEN_MAKES[0], 77, "yellow", 1011)
    pen2 = Pen(PEN_MAKES[1], 55, "Blue", 1012)
    pen3 = Pen(PEN_MAKES[2], 65, "green", 1013)
    pen4 = Pen(PEN_MAKES[3], 65, "red", 1014)

    pen1.write("CodeAcademy group is so strong!")
    print(pen1.capacity)
