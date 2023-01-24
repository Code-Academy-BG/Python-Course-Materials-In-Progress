from oop.exercise.pen import Pen
from oop.mixins import TimestampMixin
from oop.principles.inheritance.person import Person


class Student(Person, TimestampMixin):
    def __init__(self, semester, faculty_number, *args, **kwargs):
        self.pens = {}
        super().__init__(*args)
        if not kwargs.get("create_student"):
            return
        if self.age < 18 and kwargs["validate_age"]:
            raise Exception("Student can't be under 18")

        self.semester = semester
        self.faculty_number = faculty_number
        self.scholarship = kwargs.pop("scholarship", 0)

    def __repr__(self):
        return f"<Student {self.name}, semester: {self.semester}>"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.semester == other.semester

    def __le__(self, other):
        return self.age <= other.age

    # def __del__(self):
    #     raise TypeError("You can't delete a Student instance")

    # def __lt__(self, other):
    #     return self.semester == other.semester
    #
    # def __ge__(self, other):
    #     return self.semester == other.semester
    #
    # def __gt__(self, other):
    #     return self.semester == other.semester

    def __delete__(self, instance):
        # Inspect what this can be used for
        pass

    def __new__(cls, *args, **kwargs):
        if args[3] < 18:
            print("Student can't be under 18 years old")
            return
        return super().__new__(cls)

    def save_pen(self, pen):
        self.pens[pen.id] = pen

    def write(self, pen_id, text):
        if not self.pens.get(pen_id):
            print("You don't have such Pen. Choose again")
            return
        pen = self.pens[pen_id]
        pen.write(text)

    def study(self, discipline):
        print(f"{self.name} is studying {discipline}")

    def read_books(self):
        return self.semester * 10

    @classmethod
    def create_students(cls, students_data):
        return [
            cls(
                semester,
                faculty_number,
                name,
                age,
                gender,
                height,
            )
            for semester, faculty_number, name, age, gender, height in students_data
        ]

    @staticmethod
    def student_static_method():
        pass


student_gosho = Student(8, 9988855, "Gosho", 33, "Male", 185, scholarship=1000)
yellow_pen = Pen("Mont Blanc", 77, "yellow", 1011)
student_gosho.save_pen(yellow_pen)
student_gosho.write(yellow_pen.id, "CodeAcademy group is so strong!")


# print(student_gosho, student_misho)

# student.study("Astro physics")
# print(f"Student {student.name} read {student.read_books()}")

# student_one, student_two = Student.create_students([
#         [8, 9988855, "Pesho", 32, "Male", 185],
#         [7, 9988857, "Gosho", 27, "Male", 180]
#     ]
# )
# print(student_one.semester)
# student_one.student_static_method()
# Student.student_static_method()
#
# # Not good practice
# student_three = student_one.create_students([[10, 9988860, "Maria", 25, "Female", 150]])[0]
# print(student_three.name)
