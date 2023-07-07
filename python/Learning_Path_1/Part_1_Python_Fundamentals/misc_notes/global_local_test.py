
x = 1
def add_1(n):
    n += 1
    print(n, "value of n, this is inside the function")
    x = n
    print(x)

print(x)
add_1(x)
print(x)
# you may see that it doesn't change the global variable x





"""

**Global Variables**

In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

For example:

```python
x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)
```

Output:

```
x inside: global
x outside: global
```

In the above code, we created `x` as a global variable and defined a `foo()` function to print the global variable `x`. Finally, we call the `foo()` function and also print the value of `x` outside of the function.

**Local Variables**

A variable declared inside the function's body or in the local scope is known as a local variable. Local variables can only be accessed inside the function in which they are declared.

For example:

```python
def foo():
    y = "local"

foo()
print(y)
```

The above code will raise an error because we are trying to access a local variable `y` in a global scope.

However, if you print `y` inside the `foo()` function, you'll get "local" as output.

```python
def foo():
    y = "local"
    print(y)

foo()
```

**Using the `global` keyword**

In Python, when you want to use a global variable inside a function, you can use the `global` keyword.

```python
def foo():
    global x
    x = "local"

foo()
print(x)
```

Even though `x` is defined in the local scope of the `foo()` function, the `global` keyword makes it a global variable. So the last print statement will output "local".
"""