class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):

        super().__init__(name)

        self.marks = marks


s = Student("Aashish", 95)

print(s.name)
print(s.marks)