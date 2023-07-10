Sure, debugging and logging are essential techniques in Python for identifying and fixing issues in code and for tracking the flow and state of the program over time.

1. **Python's Built-In Debugger (`pdb`):**

`pdb` is a built-in Python library used for interactive debugging. Its name is short for "Python Debugger".

Here's a simple example:

```python
import pdb

def add_numbers(a, b):
    sum = a + b
    pdb.set_trace()  # Debugger entry point
    return sum

print(add_numbers(1, 2))
```

When the program execution hits the `pdb.set_trace()` line, it'll start an interactive debugging session. In this session, you can inspect variables, step over lines, step into functions, and continue execution.

In the debugger, you could type `p sum` to print the value of the `sum` variable, `n` to go to the next line, or `c` to continue execution until the next breakpoint or the end of the program.

2. **Logging:**

Logging is used to record the flow of your program and its state. This is useful for understanding the program's behavior and for debugging.

Here's a simple logging example:

```python
import logging

# Configure logging to log to a file, level=DEBUG, and with a certain format
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def add_numbers(a, b):
    logging.debug(f'Adding {a} and {b}')  # Log a debug message
    sum = a + b
    logging.info(f'Sum of {a} and {b} is {sum}')  # Log an info message
    return sum

print(add_numbers(1, 2))
```

In this example, we're using two types of log messages - debug and info. The debug messages are used to give detailed information, typically of use only when diagnosing problems. The info messages confirm that things are working as expected.

This script will create a `app.log` file with the debug and info messages. The `logging.basicConfig()` function is used to configure the logging. There are many other configuration options, including logging to stdout, logging at different levels, and customizing the log message format.

Remember, using `print` statements for debugging and tracking the program flow is not a good practice. It's better to use `pdb` for interactive debugging and `logging` for non-interactive debugging and record keeping.


================================================================================
**LOGGING LEVELS**

Python's built-in logging module defines five standard levels indicating the severity of events. The levels, in increasing order of severity, are as follows:

1. **DEBUG**: Detailed information, typically of interest only when diagnosing problems. These logs provide the most granular and detailed logging information. You'd use this level when you are trying to diagnose a specific problem, and you need all available information about the application's state.

2. **INFO**: Confirmation that things are working as expected. It's used to confirm that things are working as expected. The program is working correctly, but it's still useful to record that events are taking place, like a particular function being entered or successfully exited, or any other operation that you'd want to know is happening.

3. **WARNING**: An indication that something unexpected happened, or may happen in the near future (e.g. 'disk space low'). The software is still working as expected, but something unusual and potentially harmful has occurred.

4. **ERROR**: Due to a more serious problem, the software has not been able to perform some function. It indicates a more serious problem that prevented the software from performing a function. Here, the function or some request failed to execute, and the issue is more severe than a warning.

5. **CRITICAL**: A very serious error, indicating that the program itself may be unable to continue running. It's the highest priority log message and indicates a possibly fatal error.

The logging level dictates what level of log messages will actually get logged. If you set the level to `INFO`, then it and all the levels more severe than it will be logged. This means an `INFO` level setting will log `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages, but not `DEBUG`. 

This allows you to control the granularity of your logging output as needed, and you can change the level as needed (such as increasing logging detail when diagnosing an issue, and reducing it afterward).