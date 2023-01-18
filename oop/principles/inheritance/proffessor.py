from oop.principles.inheritance.student import Student


class Professor(Student):
    TITLE = "Professor"

    def __init__(self, faculty, experience_ages, disciplines, *args):
        super().__init__(*args)
        self.__disciplines = disciplines
        self.faculty = faculty
        self.experience_ages = experience_ages

    @property
    def disciplines(self):
        return self.__disciplines

    @disciplines.setter
    def disciplines(self, disciplines):
        # raise TypeError("Disciplines are unchangable")
        self.__disciplines = disciplines

    def add_discipline(self, discipline):
        if discipline in self.__disciplines:
            return "I already have this one in my list"
        self.__disciplines.append(discipline)
        return "Oh, another one for me..."

    def study(self, discipline):
        print(f"{self.name} is mastering {discipline}")

    def read_books(self):
        student_result = super().read_books()
        return student_result * 100


prof = Professor(
    "FMI",
    25,
    ["Math", "Advanced Math 1"],
    3,
    "1701682025",
    "Poli",
    23,
    "f",
    155,
)

prof.study("Astro physics")
print(f"Professor {prof.name} read {prof.read_books()}")

