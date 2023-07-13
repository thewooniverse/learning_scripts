SQLite is a library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Python includes a built-in SQLite connector, `sqlite3`.

Here's a basic usage:

1. **Importing the module**

```python
import sqlite3
```

2. **Creating a connection**

```python
# This will create a new file named 'my_database.db' if it doesn't exist. Otherwise, it will connect to it.
conn = sqlite3.connect('my_database.db')
```

3. **Creating a cursor object**

```python
cursor = conn.cursor()
```

4. **Executing SQL commands**

You can execute any SQL command using the `execute` method of the cursor object.

```python
# Creating a new table named 'users'
cursor.execute('''
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT unique,
    password TEXT)
''')
```

5. **Committing changes and closing the connection**

After executing all your commands, you should commit those changes and close the connection.

```python
conn.commit()
conn.close()
```

When it comes to storing Python objects in SQLite, we typically need to serialize the objects before storing them. Here's an example using `pickle` for serialization:

```python
import sqlite3
import pickle

class MyClass:
    def __init__(self, val):
        self.val = val

# Create a new object
my_obj = MyClass(10)

# Serialize the object
my_obj_pickled = pickle.dumps(my_obj)

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a new table named 'objects'
cursor.execute('''
CREATE TABLE objects(
    id INTEGER PRIMARY KEY,
    obj BLOB)
''')

# Insert the serialized object into the 'objects' table
cursor.execute("INSERT INTO objects (obj) VALUES (?)", (my_obj_pickled,))

# Commit the changes and close the connection
conn.commit()
conn.close()
```

To retrieve this object later:

```python
# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Retrieve the serialized object from the 'objects' table
cursor.execute("SELECT obj FROM objects WHERE id=?", (1,))  # Assuming the id of the object is 1
my_obj_pickled = cursor.fetchone()[0]

# Deserialize the object
my_obj = pickle.loads(my_obj_pickled)

print(my_obj.val)  # This should print: 10

# Close the connection
conn.close()
```

Remember that `pickle` is not safe or reliable for transmitting data between untrusted parties.