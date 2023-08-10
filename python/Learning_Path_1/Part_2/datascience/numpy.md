=========================================================================
Numpy basics
=========================================================================

Sure! **NumPy** (Numerical Python) is a powerful library for numerical computations in Python. It provides support for arrays (including matrices), and mathematical functions to operate on these arrays.

### Basics

#### 1. Arrays

NumPy's main object is the homogeneous multidimensional array. All elements must be of the same type.

```python
import numpy as np

# Create a one-dimensional array
a = np.array([1, 2, 3])

# Create a two-dimensional array
b = np.array([
   [1, 2, 3], 
   [4, 5, 6]])
```

#### 2. Array Attributes

```python
# Shape of the array (rows, columns)
print(b.shape)  # Output: (2, 3)

# Number of dimensions
print(b.ndim)  # Output: 2

# Data type of the elements
print(b.dtype)  # Output: int64
```

#### 3. Array Creation

```python
# Create an array filled with zeros
zeros = np.zeros((3, 4))

# Create an array filled with ones
ones = np.ones((2, 3))

# Create an identity matrix
identity = np.eye(3)
```

#### 4. Arithmetic Operations

Arithmetic operators apply element-wise.

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
print(x + y)  # Output: [5, 7, 9]

# Multiplication
print(x * y)  # Output: [4, 10, 18]

# Division
print(y / x)  # Output: [4., 2.5, 2.]
```

#### 5. Broadcasting

NumPy allows operations on arrays of different shapes.

```python
x = np.array([
      [1], 
      [2], 
      [3]])
y = np.array([4, 5, 6])

# The smaller array is "broadcast" across the larger array
print(x + y)  # Output: [[5, 6, 7], [6, 7, 8], [7, 8, 9]]
```

#### 6. Mathematical Functions

```python
# Exponential
print(np.exp(x))

# Square root
print(np.sqrt(x))

# Logarithm
print(np.log(x))
```

#### 7. Indexing and Slicing

```python
# Accessing elements
print(b[1, 2])  # Output: 6

# Slicing
print(b[0, :])  # Output: [1, 2, 3]
```

#### 8. Linear Algebra

```python
# Matrix multiplication
print(np.dot(b, x))

# Transposition
print(b.T)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(b)
```

### Most Common Use Cases

- **Mathematics**: NumPy provides an abundance of useful features for operations on n-arrays and matrices in Python.
- **Signal Processing**: Used in image and signal processing tasks.
- **Data Analysis**: Data manipulation using Pandas often uses NumPy under the hood.
- **Machine Learning**: Libraries like Scikit-Learn, TensorFlow, and PyTorch use NumPy arrays for inputs and outputs.

### Summary

NumPy provides a fast, efficient way to perform numerical operations in Python. Its powerful set of features and ease of use make it an essential library for anyone working in scientific or data-driven fields.








=========================================================================
Indexing and locating items
=========================================================================
In NumPy, you can index and locate items in an array through various methods. Here's an overview, including how to find the index of the maximum value:

1. **Standard Indexing**: Like Python lists, you can access an element by its index.
   ```python
   value = array[3]
   ```

2. **Slicing**: You can slice an array to get a specific portion.
   ```python
   subset = array[2:5]
   ```

3. **Boolean Indexing**: Using a condition, you can get elements that meet specific criteria.
   ```python
   filtered_values = array[array > 5]
   ```

4. **Fancy Indexing**: You can access multiple non-continuous indices at once.
   ```python
   specific_values = array[[1, 4, 7]]
   ```

5. **Multi-Dimensional Indexing**: In a 2D array, you can specify row and column indices.
   ```python
   value = array2d[1, 2]
   ```

6. **Finding the Index of a Specific Value**: If you want to find the index of a specific value (e.g., the maximum temperature), you can use `np.argmax()`.
   ```python
   temperatures = np.array([30, 35, 32, 40, 33])
   max_temperature = np.max(temperatures)
   index_of_max_temperature = np.argmax(temperatures)
   print(index_of_max_temperature)  # Output: 3
   ```

Here, `np.argmax(temperatures)` will give you the index of the maximum value in the `temperatures` array. If the array is multidimensional, you can use `np.unravel_index` along with `np.argmax` to get the multidimensional index.

```python
temperatures_2d = np.array([[30, 35], [32, 40]])
index_of_max_temperature = np.unravel_index(np.argmax(temperatures_2d), temperatures_2d.shape)
print(index_of_max_temperature)  # Output: (1, 1)
```

This diverse set of indexing methods makes NumPy very powerful and flexible for data manipulation and analysis.










=========================================================================
Dividing and grouping data into smaller ones
=========================================================================
Dividing a year's worth of temperature data into months can be done in several ways, depending on the data's format and the tools you're using. Below are some common approaches:

1. **Using NumPy Alone**:
   If the data is in a NumPy array, and you know the number of days in each month, you can use slicing to manually divide the data.
   ```python
   january = temperatures[0:31]
   february = temperatures[31:59]
   # ... and so on
   ```

2. **Using Pandas with DateTime Index**:
   If you're using Pandas, you can create a DataFrame and set a DateTime index. This way, you can leverage Pandas' time series functionality to resample the data by month.

   ```python
   import pandas as pd

   # Create a DateTime index
   date_rng = pd.date_range(start='1/1/2020', end='12/31/2020', freq='D')

   # Create a DataFrame with the temperatures and DateTime index
   df = pd.DataFrame(date_rng, columns=['date'])
   df['temperature'] = temperatures  # Assuming temperatures is a 1D array of the data
   df.set_index('date', inplace=True)

   # Resample by month
   monthly_temperatures = df.resample('M').mean()
   ```

3. **Using GroupBy with Pandas**:
   You can also use Pandas' `groupby` method with a function that extracts the month from each date to group the data by month.

   ```python
   # Assuming df is a DataFrame with a 'date' column
   df['month'] = pd.to_datetime(df['date']).dt.month
   monthly_temperatures = df.groupby('month').mean()
   ```

4. **Manual Parsing with Custom Logic**:
   If the data is not in a standard format, you may need to write custom parsing logic to divide it into months. This can involve parsing date strings, handling missing data, and more, depending on the dataset's specifics.

The best approach depends on your specific needs and the data's structure. If you're working with time series data frequently, using Pandas with a DateTime index can provide powerful and flexible tools for handling dates and times.







=========================================================================
Broadcasting
=========================================================================
Certainly! The code you've posted is a demonstration of broadcasting in NumPy. Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations. Here's a breakdown of how it works in your example:

1. `x` is a 3x1 array:
   ```
   [[1],
    [2],
    [3]]
   ```

2. `y` is a 1x3 array (when treated as a one-dimensional array, it can be thought of as a row vector):
   ```
   [4, 5, 6]
   ```

3. When you try to add these two arrays, their shapes don't match. But NumPy applies broadcasting rules to make the shapes compatible. In this case, it "broadcasts" the smaller array (`y`) across the larger one (`x`) by replicating the row vector across all the rows of `x`.

4. After broadcasting, `y` effectively becomes:
   ```
   [[4, 5, 6],
    [4, 5, 6],
    [4, 5, 6]]
   ```

5. Now, `x` and the broadcasted `y` are of the same shape, and NumPy adds them element-wise:
   ```
   [[1 + 4, 1 + 5, 1 + 6],
    [2 + 4, 2 + 5, 2 + 6],
    [3 + 4, 3 + 5, 3 + 6]]
   = [[5, 6, 7], [6, 7, 8], [7, 8, 9]]
   ```

The resulting array is the output you see. Broadcasting can be quite handy, as it allows you to perform these operations without needing to manually reshape or replicate the arrays to make their shapes match.






=========================================================================
N-Arrays - N-Dimensional Arrays
=========================================================================
An n-array in the context of NumPy refers to an n-dimensional array. Essentially, an array can have one or more dimensions, and the "n" here is just a placeholder for the number of dimensions the array has.

Here's a breakdown of what n-arrays look like for various values of n:

- **1D array (n=1)**: A one-dimensional array is like a simple list of values. It's a straight line of elements. Example: `[1, 2, 3]`.

- **2D array (n=2)**: A two-dimensional array can be thought of as a matrix or a grid of values. It has rows and columns. Example:
  ```
  [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]
  ```

- **3D array (n=3)**: A three-dimensional array adds another layer of depth, like a cube of values. It can be visualized as a stack of matrices.
  ```
  [[[1, 2], [3, 4]],
   [[5, 6], [7, 8]]]
  ```

- **nD array (n>3)**: You can continue to add dimensions, creating 4D, 5D, etc., arrays. These become harder to visualize but can be very useful in mathematical computations, particularly in fields like physics, engineering, and machine learning.

NumPy is designed to work efficiently with these n-dimensional arrays, providing a host of mathematical operations and manipulations that you can perform on them. This includes things like basic arithmetic, statistical analysis, linear algebra, and more. The library is optimized for performance and allows for expressing complex mathematical tasks succinctly.












=========================================================================
Numpy Random
=========================================================================
Yes, NumPy provides a module called `numpy.random` that contains functions to generate random numbers from different probability distributions. This module is very useful in data science and statistical applications, where random sampling and data shuffling are common tasks.

Here are a few examples of using `numpy.random`:

### Generating Random Floats
You can generate random floats uniformly distributed over the interval `[0, 1)` using the `random` function:

```python
import numpy as np

random_floats = np.random.random((3, 3))
print(random_floats)
```

### Generating Random Integers
You can generate random integers within a specific range using the `randint` function:

```python
random_integers = np.random.randint(1, 10, size=(5, 5))
print(random_integers)
```

### Generating Random Samples from a Normal Distribution
You can generate random samples from a normal (Gaussian) distribution using the `normal` function:

```python
mean = 0
std_dev = 1
samples = np.random.normal(mean, std_dev, 1000)
```

### Shuffling an Array
You can shuffle an array using the `shuffle` function:

```python
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
```

### Setting a Random Seed
To ensure that the random numbers generated are reproducible, you can set a seed using the `seed` function:

```python
np.random.seed(42)
```

The `numpy.random` module provides many other functions to generate random numbers from various distributions, and to perform other randomization tasks. It's a powerful tool for anyone working with stochastic simulations or random sampling.









=========================================================================
Slicing in NumPy
=========================================================================
Slicing in NumPy works similarly to regular list slicing in Python, but it's more powerful since it allows you to slice multidimensional arrays. Here's a breakdown of how slicing works in NumPy:

1. **Basic Slicing**: If you have a one-dimensional array, you can slice it just like a regular Python list.

   ```python
   import numpy as np
   a = np.array([0, 1, 2, 3, 4])
   print(a[1:4]) # Output: [1 2 3]
   ```

   Here, `1:4` is slicing the array from index 1 (inclusive) to index 4 (exclusive).

2. **Multidimensional Slicing**: NumPy allows you to slice multidimensional arrays using commas to separate each dimension's slice.

   ```python
   b = np.array(
       [
           [0, 1, 2], 
           [3, 4, 5], 
           [6, 7, 8]])
   print(b[0:2, 1:3]) # Output: [[1 2]
                     #          [4 5]]
   ```

   Here, `0:2` slices rows 0 and 1, and `1:3` slices columns 1 and 2. So the resulting slice includes those specific rows and columns.

3. **Step Slicing**: You can include a step value to take elements with a certain interval.

   ```python
   print(a[0:5:2]) # Output: [0 2 4]
   ```

   Here, `0:5:2` starts at index 0, stops at index 5, and takes every 2nd element.

4. **Using Ellipsis (`...`)**: When dealing with arrays that have many dimensions, you can use ellipsis to indicate multiple colons in a row.

   ```python
   c = np.random.rand(3, 3, 3, 3) # A 4D array
   print(c[..., 0]) # Will slice the last dimension, selecting only the first element along the last axis
   ```

5. **Boolean Masking**: You can also use boolean arrays to select specific elements that satisfy a condition.

   ```python
   mask = a > 2
   print(a[mask]) # Output: [3 4]
   ```

Slicing in NumPy is very powerful, allowing you to easily manipulate and access parts of large and potentially multidimensional arrays. It's one of the features that make NumPy so valuable for scientific computing and data analysis in Python.












=========================================================================
Reshaping in NumPy
=========================================================================
You can reshape a NumPy array without changing its data by using the `reshape` method. This method returns a new view of the array with the specified shape. The new shape must be compatible with the original shape, meaning that the total number of elements must remain the same.

Here's an example:

```python
import numpy as np

# Create a one-dimensional array of 12 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape it into a 3x4 matrix
reshaped_arr = arr.reshape(3, 4)

print(reshaped_arr)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
```

If you don't know the size of one of the dimensions, you can specify it as `-1`, and NumPy will automatically calculate it:

```python
reshaped_arr = arr.reshape(3, -1)  # Same result as above
```

It's important to note that the `reshape` method returns a new view of the original data whenever possible, so modifying the reshaped array can also modify the original array. If you want to ensure that the reshaped array is a copy, you can use the `np.copy` method:

```python
reshaped_copy = arr.reshape(3, 4).copy()
```

The `reshape` method is a versatile tool in NumPy, allowing you to adapt arrays to the shape you need for different operations and analyses without altering the underlying data.



===
PT 2 - Reshaping
===
Yes, you can reshape an array into a different shape with different dimensions, but it's not directly done using the `reshape` method. The `reshape` method requires that the total number of elements in the original and new shape must be the same. Therefore, you can't reshape a `(2,2)` array into a `(3,3)` array directly using `reshape`, as the total number of elements would change.

However, you can achieve this by combining other operations, such as creating a new array of zeros and then filling in the values from the original array. Here's how you could do that:

```python
import numpy as np

# Original (2,2) array
original_array = np.array([[1, 2], [3, 4]])

# Create a (3,3) array filled with zeros
new_shape = (3, 3)
reshaped_array = np.zeros(new_shape)

# Fill the new array with the values from the original array
reshaped_array[:original_array.shape[0], :original_array.shape[1]] = original_array

print(reshaped_array)
# Output:
# [[1. 2. 0.]
#  [3. 4. 0.]
#  [0. 0. 0.]]
```

This code first creates a new `(3,3)` array filled with zeros, then fills in the values from the original `(2,2)` array into the corresponding positions of the new array, leaving the "extra" elements as zeros.











=========================================================================
NUMPY Arithmetics
=========================================================================
Sure! NumPy provides a wide range of arithmetic operations that you can perform on arrays. Here's a rundown of some commonly used ones, complete with examples:

1. **Addition**: You can add arrays together using the `+` operator or the `np.add` function.

   ```python
   import numpy as np
   a = np.array([1, 2, 3])
   b = np.array([4, 5, 6])
   print(a + b) # Output: [5 7 9]
   print(np.add(a, b)) # Output: [5 7 9]
   ```

2. **Subtraction**: Use the `-` operator or `np.subtract` to subtract arrays.

   ```python
   print(a - b) # Output: [-3 -3 -3]
   print(np.subtract(a, b)) # Output: [-3 -3 -3]
   ```

3. **Multiplication**: Multiply arrays with the `*` operator or `np.multiply`.

   ```python
   print(a * b) # Output: [4 10 18]
   print(np.multiply(a, b)) # Output: [4 10 18]
   ```

4. **Division**: Divide arrays with the `/` operator or `np.divide`.

   ```python
   print(b / a) # Output: [4. 2.5 2.]
   print(np.divide(b, a)) # Output: [4. 2.5 2.]
   ```

5. **Modulus**: Get the remainder of division with the `%` operator or `np.mod`.

   ```python
   print(b % a) # Output: [0 1 0]
   print(np.mod(b, a)) # Output: [0 1 0]
   ```

6. **Exponentiation**: Raise elements to powers with the `**` operator or `np.power`.

   ```python
   print(a ** 2) # Output: [1 4 9]
   print(np.power(a, 2)) # Output: [1 4 9]
   ```

7. **Matrix Multiplication**: Use `np.dot` or the `@` operator for matrix multiplication.

   ```python
   c = np.array([[1,2],[3,4]])
   d = np.array([[5,6],[7,8]])
   print(c @ d)
   # Output:
   # [[19 22]
   #  [43 50]]
   print(np.dot(c, d))
   # Output:
   # [[19 22]
   #  [43 50]]
   ```

8. **Unary Operations**: These include operations like computing the sum of all elements using `np.sum`, or finding the minimum and maximum using `np.min` and `np.max`, respectively.

   ```python
   print(np.sum(a)) # Output: 6
   print(np.min(a)) # Output: 1
   print(np.max(a)) # Output: 3
   ```

These examples showcase basic element-wise arithmetic operations and some matrix operations. Remember that for these operations to be defined, the dimensions of the arrays must be compatible.








=========================================================================
Unary arithmetic operations
=========================================================================
Unary operations are operations that act on a single input (array or element). Here are some common unary operations available in NumPy:

### 1. Arithmetic Operations
- `np.negative(x)`: Numerical negative, element-wise.
- `np.positive(x)`: Numerical positive, element-wise.

### 2. Exponential and Logarithmic Functions
- `np.exp(x)`: Calculate the exponential of all elements in the input array.
- `np.log(x)`: Natural logarithm, element-wise.
- `np.sqrt(x)`: Return the non-negative square root of an array, element-wise.

### 3. Trigonometric Functions
- `np.sin(x)`: Trigonometric sine, element-wise.
- `np.cos(x)`: Cosine element-wise.
- `np.tan(x)`: Compute tangent element-wise.

### 4. Hyperbolic Functions
- `np.sinh(x)`: Hyperbolic sine, element-wise.
- `np.cosh(x)`: Hyperbolic cosine, element-wise.
- `np.tanh(x)`: Compute hyperbolic tangent element-wise.

### 5. Rounding
- `np.round(x)`: Round an array to the given number of decimals.
- `np.ceil(x)`: Return the ceiling of the input, element-wise.
- `np.floor(x)`: Return the floor of the input, element-wise.

### 6. Sum, Product, and Differences
- `np.sum(x)`: Sum of all the elements in the array.
- `np.prod(x)`: Return the product of all the elements in the array.
- `np.diff(x)`: Calculate the n-th discrete difference along the given axis.

### 7. Statistics
- `np.mean(x)`: Compute the arithmetic mean along the specified axis.
- `np.std(x)`: Compute the standard deviation along the specified axis.
- `np.var(x)`: Compute the variance along the specified axis.
- `np.median(x)`: Compute the median along the specified axis.

### 8. Other Mathematical Functions
- `np.abs(x)`: Calculate the absolute value element-wise.
- `np.sign(x)`: Returns an element-wise indication of the sign of a number.

These are some of the unary operations that you can use with NumPy arrays. Note that some of these can be used both as functions and as methods on NumPy arrays, depending on the needs of your code.








=========================================================================
Boolean Indexing
=========================================================================
Boolean indexing in NumPy refers to the practice of using an array of Boolean values to index or "filter" another array. This can be an extremely powerful tool for selecting or modifying parts of an array based on conditions.

Here's a basic example to illustrate how Boolean indexing works:

1. **Create a NumPy array**:

   ```python
   import numpy as np
   a = np.array([10, 20, 30, 40, 50])
   ```

2. **Create a Boolean condition**:

   You can create a Boolean condition using any of the comparison operators like `<`, `>`, `==`, etc. This will return a Boolean array with the same shape as the original array.

   ```python
   condition = a > 30
   print(condition)  # Output: [False False False  True  True]
   ```

3. **Use the Boolean array to index the original array**:

   You can use the Boolean array `condition` to index the original array `a`. This will return only the elements where the corresponding value in the Boolean array is `True`.

   ```python
   result = a[condition]
   print(result)  # Output: [40 50]
   ```

You can combine these steps into one line:

```python
result = a[a > 30]
```

Boolean indexing is often used for filtering data, replacing values under certain conditions, and other data manipulation tasks. It's a concise way to perform these operations without needing to use loops.

### Example: Replacing Values

You can also use Boolean indexing to modify parts of an array based on conditions. Here's an example that replaces all values greater than 30 with the value 999:

```python
a[a > 30] = 999
print(a)  # Output: [ 10  20  30 999 999]
```

Boolean indexing is a fundamental concept in NumPy and is widely used in data preprocessing, cleaning, and transformation tasks.




=========================================================================
Diagonal and Transposing
=========================================================================
Certainly! In NumPy, you can work with diagonals and transposes quite easily. Here's how you can do both:

### Getting the Diagonal of an Array

To get the diagonal of an array, you can use the `np.diag` method.

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

diagonal = np.diag(a)
print(diagonal)  # Output: [1 5 9]
```

### Transposing an Array

To transpose an array (swap its rows with columns), you can use the `np.transpose` method or simply the `.T` attribute of the array.

```python
transpose_a = np.transpose(a)
# or
transpose_a = a.T

print(transpose_a)
# Output:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
```

### Getting the Diagonal of the Transposed Array

You can combine these two to get the diagonal of the transposed array:

```python
diagonal_transpose_a = np.diag(a.T)
print(diagonal_transpose_a)  # Output: [1 5 9]
```

The diagonal of the transposed array is the same as the diagonal of the original array since transposing does not change the diagonal elements.

These methods make it easy to work with basic linear algebra concepts in NumPy.
