



In Python, the `__main__` module is the entry point to your program. When you run a script, Python sets the special variable `__name__` to `"__main__"` for that script. This allows you to check whether a script is being run directly or being imported as a module into another script.

### Basic Usage
Here's the basic usage of `if __name__ == "__main__":`:

```python
# some_module.py
print("This will always run.")

def function_one():
    print("Function one.")

def function_two():
    print("Function two.")

if __name__ == "__main__":
    print("This will only run if the script is the entry point.")
    function_one()
    function_two()
```

If you run `some_module.py` directly, it will print:

```
This will always run.
This will only run if the script is the entry point.
Function one.
Function two.
```

However, if you import `some_module.py` into another script, only the "This will always run." line will execute. The code inside the `if __name__ == "__main__":` block won't run because the `__name__` attribute for `some_module.py` will be set to its module name (`"some_module"`) instead of `"__main__"`.

### Why it's Useful

1. **Code Organization**: It allows you to separate the code in your script that's usable as a module from the code that should only run when the script itself is run.

2. **Performance**: When you're importing a module, you may not want to run all the computations or initializations that are in the global scope. This makes sure only the necessary bits run.

3. **Testing**: It allows you to import the module's classes and functions into other scripts for testing without running the whole script.

### Attributes
The `__main__` module doesn't have specific attributes. However, Python sets a couple of attributes when a script is run:

- `__name__`: The name of the current module. When a script is run, its `__name__` is set to `"__main__"`.
  
- `__file__`: The path of the script being run. This is useful for finding resources relative to the script location.

### Other Usages
Apart from the most common use-case (`if __name__ == "__main__":`), you can also do other checks or initializations in `__main__`:

```python
if __name__ == "__main__":
    # Parse command-line arguments
    # Perform initial setup
    # Run a function or class defined in the script
    pass
```

### Example with Command-line Arguments
```python
import sys

def main(arg1, arg2):
    print(f"Argument 1: {arg1}, Argument 2: {arg2}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
```

By using `__main__`, you can make your Python files more modular and reusable.