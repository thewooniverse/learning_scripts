In Python, the `return` statement is used to end the execution of a function and gives back the result to the caller. Here are various ways to use it:

**1. Simple Return**
A function can simply return a value. In the function below, we return the result of adding two numbers:

```python
def add(a, b):
    return a + b

print(add(3, 2))  # Outputs: 5
```

**2. Return Multiple Values**
You can also return multiple values from a function using tuples. 

```python
def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([1, 2, 3, 4, 5]))  # Outputs: (1, 5)
```
When calling this function, you can use multiple variables to capture the results:

```python
min_val, max_val = min_max([1, 2, 3, 4, 5])
print(min_val)  # Outputs: 1
print(max_val)  # Outputs: 5
```

**3. Return a Boolean**
It's common to return a Boolean value from a function. This is often used to check conditions:

```python
def is_even(n):
    return n % 2 == 0

print(is_even(5))  # Outputs: False
print(is_even(6))  # Outputs: True
```

**4. Return None**
If no return statement is given, or a function ends without hitting a return statement, Python functions will return `None`:

```python
def no_return(n):
    n + 2
    # no return statement

print(no_return(2))  # Outputs: None
```

Remember, when the `return` statement is executed inside a function, it ends the function execution and sends the result back to the caller. If you have code after the return statement in a function, it will not be executed.