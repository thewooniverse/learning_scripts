The main difference between using `elif` and using multiple `if` statements is how the conditions are evaluated after a true condition is found.

- `if`-`elif`-`else` statements: After a condition in an `if` or `elif` is found to be true, Python will execute the block of code associated with that condition and then skip the rest of the `if`-`elif`-`else` structure. `elif` is short for "else if", which means "if the previous conditions were not true, then try this condition".

- Multiple `if` statements: Each `if` statement is evaluated independently. This means that if a condition is found to be true, Python will execute the block of code associated with that condition and then move on to the next `if` statement (if any), even if its condition is also true.

Here's an example to illustrate:

```python
x = 10

# Using elif
if x > 5:
    print("x is greater than 5")
elif x > 0:
    print("x is greater than 0")

# Using multiple if statements
if x > 5:
    print("x is greater than 5")
if x > 0:
    print("x is greater than 0")
```

In the `elif` case, only "x is greater than 5" will be printed, because once the `if x > 5` condition is found to be true, the `elif` condition is skipped. In the multiple `if` statements case, both "x is greater than 5" and "x is greater than 0" will be printed, because both `if` conditions are true and evaluated independently.