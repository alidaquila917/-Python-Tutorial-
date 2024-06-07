class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Test the Student class
student1 = Student("John", 20)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(95)

student2 = Student("Emma", 22)
student2.add_grade(75)
student2.add_grade(80)
student2.add_grade(85)

student1.display_info()
print("Average Grade:", student1.calculate_average_grade())

student2.display_info()
print("Average Grade:", student2.calculate_average_grade())
