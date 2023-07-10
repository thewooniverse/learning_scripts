Python's built-in `random` module is commonly used for generating random numbers. The module has several functions for generating numbers, but the most common ones are `randint()`, `random()`, and `uniform()`.

1. `random.randint(a, b)`: This function returns a random integer between the two numbers `a` and `b` inclusive.

   Example:

   ```python
   import random
   print(random.randint(1, 10))  # Generates a random integer between 1 and 10
   ```

2. `random.random()`: This function returns a random floating-point number in the range [0.0, 1.0).

   Example:

   ```python
   import random
   print(random.random())  # Generates a random float between 0.0 and 1.0
   ```

3. `random.uniform(a, b)`: This function returns a random floating-point number between the two numbers `a` and `b` (which can be either integer or float).

   Example:

   ```python
   import random
   print(random.uniform(1.0, 10.0))  # Generates a random float between 1.0 and 10.0
   ```

Remember to `import random` at the start of your program to use these functions.