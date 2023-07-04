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