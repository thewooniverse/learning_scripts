
# exercise 1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# tests
p = Person("Alice", 25)
p.introduce_yourself()  # Should print "Hello, my name is Alice and I'm 25 years old."


# exercise 2:
class Student(Person):
    def __init__(self, name, age, grades=None):
            super().__init__(name, age)  # Call the __init__ of the superclass
            self.grades = []
    
    def add_grade(self, grade):
        return self.grades.append(grade)
    
    def calculate_gpa(self):
        return (sum(self.grades)/len(self.grades))

# tests
s = Student("Bob", 20)
s.add_grade(90)
s.add_grade(80)
print(s.calculate_gpa())  # Should return 85.0

# exercise 3

class Teacher(Person):
    def __init__(self, name, age, subjects=None):
            super().__init__(name, age)  # Call the __init__ of the superclass
            self.subjects = subjects
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old. I teach {self.parse_subjects()}.")


    def parse_subjects(self):
        if len(self.subjects) == 1:
            return self.subjects[0]
        elif len(self.subjects) == 2:
            return " and ".join(self.subjects)
        elif len(self.subjects) > 2:
            return ((", ".join(self.subjects[:-1])) + f" and {self.subjects[-1]}")
        


# test
t = Teacher("Charlie", 30, ["Math", "Physics"])
t.introduce_yourself()  # Should print "Hello, my name is Charlie and I'm 30 years old. I teach Math and Physics."

# test part 2, try for 3 subjects taught and 1 subject taught
t2 = Teacher("Becky", 30, ["Math", "Physics", "History"])
t2.introduce_yourself()

