In Python, you can import all variables, functions, classes etc from another module using the `from module import *` statement.

For example, if you have a module named `my_module` and you want to import all its contents, you would do:

```python
from my_module import *
```

This will import all "public" items, i.e., those not beginning with an underscore. After this, you can use the variables and functions directly as if they were defined in the same file.

However, this is generally discouraged for a couple of reasons:

1. It can lead to confusion about where certain variables or functions are defined, especially in larger projects.

2. If the imported module has variables or functions with the same names as those in your current module, they will be overwritten by the imports.

Instead, it's recommended to import only the specific items you need:

```python
from my_module import specific_variable, specific_function
```

Or import the module under an alias and access the variables or functions with dot notation:

```python
import my_module as mm

print(mm.specific_variable)
mm.specific_function()
```

This will make your code easier to understand and maintain.