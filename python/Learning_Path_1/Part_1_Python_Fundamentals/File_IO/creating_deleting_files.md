You can use Python's built-in `os` module to create and delete files. Here's how you can do it:

**Creating a file:**

You can create a file in Python using the built-in `open()` function with the 'w' (write) mode. If the file does not exist, `open()` will create it.

```python
with open('newfile.txt', 'w') as file:
    pass
```

Here, the 'w' mode opens the file for writing. If the file already exists, it gets truncated (emptied). If it doesn't exist, a new one gets created. Using `with` is recommended as it automatically closes the file after use.

If you want to create a file without truncating it if it already exists, you can use the 'a' (append) mode.

```python
with open('existingfile.txt', 'a') as file:
    pass
```

**Deleting a file:**

You can delete a file using the `os.remove()` function:

```python
import os

os.remove('file_to_delete.txt')
```

Before you delete a file, you might want to check if it exists to prevent an error:

```python
import os

if os.path.exists('file_to_delete.txt'):
    os.remove('file_to_delete.txt')
else:
    print("The file does not exist")
```

The `os.path.exists()` function checks whether the specified path exists or not.

Remember to be careful while deleting files, as the operation cannot be undone.