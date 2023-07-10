1. **Classes and Objects**: In Python, a class is a blueprint for creating objects. Objects have member variables and behavior associated with them. In Python, a class is created by the keyword `class`.

   Here's an example:

   ```python
   class Dog:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def bark(self):
           print(f"{self.name} says woof!")

   # Creating objects
   fido = Dog("Fido", 4)
   buddy = Dog("Buddy", 9)

   # Accessing object information
   print(fido.name)
   print(buddy.age)
   buddy.bark()
   ```

2. **Inheritance**: Inheritance is a way of creating a new class using details of an existing class without modifying it. The newly formed class is a derived class (or child class). The existing class is a base class (or parent class).

   Here's an example:

   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           raise NotImplementedError("Subclass must implement this method")

   class Dog(Animal):
       def speak(self):
           return f"{self.name} says woof!"

   fido = Dog("Fido")
   print(fido.speak())
   ```

3. **Polymorphism**: Polymorphism allows us to use a single interface with different underlying forms. In Python, Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

   Here's an example:

   ```python
   class Cat(Animal):
       def speak(self):
           return f"{self.name} says meow!"

   class Cow(Animal):
       def speak(self):
           return f"{self.name} says moo!"

   animals = [Dog("Fido"), Cat("Whiskers"), Cow("Bessie")]
   for animal in animals:
       print(animal.speak())
   ```

These concepts are the foundation of OOP in Python. By understanding them, you'll be able to write more organized, efficient, and practical code.

======================================================
The `__init__()` method in Python is a special method that gets called when an object is instantiated. This method is also known as a constructor in Object Oriented Concepts. It is used to initialize the attributes of an object.

The first argument of `__init__()` is always `self`, which is a reference to the instance of the class. The `self` keyword is used to access variables that belongs to the instance, allowing you to assign values to instance variables.

Here's an example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Person class
p1 = Person("Alice", 25)

# Accessing object information
print(p1.name)
print(p1.age)
```

In this example, `__init__()` takes `name` and `age` as arguments (in addition to the mandatory `self`), and assigns them to the `name` and `age` attributes of the instance. So when we create a new `Person` instance with `p1 = Person("Alice", 25)`, we're calling the `__init__()` method and passing "Alice" and 25 as the name and age, respectively. These values are then accessible as attributes of the `p1` object.

======================================================
In Python, `raise` is a keyword used to generate an exception. An exception is a signal that an error or unusual condition has occurred. 

`NotImplementedError` is a built-in exception in Python. It's a special error that you can raise when you're writing a class or function that is supposed to be overridden or subclassed, but you want to ensure that any method that needs to be overridden in the subclass gives a clear error message if it's not.

For instance, when you have a method in your base class which is meant to be implemented in any subclass you create, and you want to make sure that any subclass must override this method, you can use `raise NotImplementedError()` in the base class method. This will raise an error when a subclass tries to use this method without overriding it.

Here's an example:

```python
class AbstractClass:
    def do_something(self):
        raise NotImplementedError()

class SubClass(AbstractClass):
    pass

obj = SubClass()
obj.do_something()  # Raises NotImplementedError
```

In the above code, `do_something` is meant to be implemented by any class that inherits from `AbstractClass`. We haven't defined `do_something` in `SubClass`, so calling `obj.do_something()` will raise a `NotImplementedError`. This clearly signals to the user of the class that they need to provide an implementation for this method in their subclass. 

Note that `NotImplementedError` and `NotImplemented` are different in Python. The former is an exception used for abstract methods that can't be called, while the latter is a special value returned by binary special methods (e.g., `__eq__`, `__lt__`, `__add__`, etc.) to indicate that the operation is not implemented with respect to the other type.




================================
**Exercises**
Absolutely, practicing coding exercises is a great way to reinforce your understanding of the concepts. Here are some exercises related to Object-Oriented Programming in Python:

**Exercise 1:**

Create a Python class named `Person` with two attributes: `name` and `age`. Add a method called `introduce_yourself` which prints a message introducing the person.

Example:

```python
p = Person("Alice", 25)
p.introduce_yourself()  # Should print "Hello, my name is Alice and I'm 25 years old."
```

**Exercise 2:**

Create a Python class named `Student` which inherits from the `Person` class. Add an additional attribute: `grades` (a list). Also add methods to add a grade and to calculate the student's GPA.

Example:

```python
s = Student("Bob", 20)
s.add_grade(90)
s.add_grade(80)
s.calculate_gpa()  # Should return 85.0
```

**Exercise 3:**

Demonstrate polymorphism by creating a `Teacher` class that also inherits from `Person`, but has a different `introduce_yourself` method that includes the subjects they teach.

Example:

```python
t = Teacher("Charlie", 30, ["Math", "Physics"])
t.introduce_yourself()  # Should print "Hello, my name is Charlie and I'm 30 years old. I teach Math and Physics."
```

When you're done with the exercises, you can share your code and I will provide feedback.









====================
**Optional parameters / attributes**

In Python, you can specify optional parameters for a method (including the `__init__` method for a class) by providing default values for the parameters. If an argument is given in the method call, it's used as the parameter's value. If no argument is given, the parameter's default value is used.

Here's an example where the `Student` class has an optional `gpa` attribute:

```python
class Student:
    def __init__(self, name, student_id, gpa=None):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa  # This attribute is optional
```

Now you can create `Student` objects with or without a `gpa`:

```python
# Create a Student object with a gpa
student_with_gpa = Student("Alice", "S123", 3.9)
print(student_with_gpa.gpa)  # Output: 3.9

# Create a Student object without a gpa
student_without_gpa = Student("Bob", "S456")
print(student_without_gpa.gpa)  # Output: None
```

In the `__init__` method of the `Student` class, `gpa=None` makes the `gpa` parameter optional. If you don't provide a value for `gpa` when creating a `Student` object, it will default to `None`.



============================================================
**Adding a new attribute to a subclass** in Python is quite straightforward. Here's how you can do it:

1. Define your base class (also known as the parent or superclass).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

2. Define your subclass (also known as the child class) and add a new attribute.

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the __init__ of the superclass
        self.student_id = student_id  # Add new attribute
```

Here's how you can use the subclass:

```python
student = Student("Alice", 20, "S123")
print(student.name)  # Output: Alice
print(student.age)  # Output: 20
print(student.student_id)  # Output: S123
```

In this example, the `Student` class is a subclass of the `Person` class and adds a new attribute `student_id`. The `super().__init__(name, age)` line is calling the initializer of the `Person` class to handle setting up the name and age attributes, allowing `Student` to add its own initialization (i.e., setting up the `student_id`).

