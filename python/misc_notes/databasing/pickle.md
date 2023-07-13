Python's built-in module `pickle` is used for serializing (pickling) and deserializing (unpickling) Python object structures. Pickling converts Python objects into a byte stream, and unpickling converts the byte stream back into Python objects. Here's a simple example:

```python
import pickle

class Dog:
    def __init__(self, name):
        self.name = name

# Create an instance of Dog
my_dog = Dog("Fido")

# Pickle the Dog object (serialization)
with open("dog.pickle", "wb") as file:
    pickle.dump(my_dog, file)

# Later on, we can load the Dog object back (deserialization)
with open("dog.pickle", "rb") as file:
    loaded_dog = pickle.load(file)

print(loaded_dog.name)  # Outputs: Fido
```

In this example, we first create a `Dog` object with the name "Fido". We then open a new file `dog.pickle` in write-binary mode, and use `pickle.dump()` to serialize the `Dog` object into the file.

Later, we open `dog.pickle` in read-binary mode and use `pickle.load()` to deserialize the `Dog` object from the file. We can then use this object just like any other Python object.

Remember, while pickle is very convenient for storing Python objects, it should not be used for long-term storage or for communicating between different systems because the protocol can change over time or vary between Python versions. It's also not secure against erroneous or maliciously constructed data, so never unpickle data that came from an untrusted source.

Also, other more robust and versatile options for storing Python objects include databases (like SQLite) and ORMs (like SQLAlchemy), but these come with more complexity and require more setup.
