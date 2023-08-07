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
b = np.array([[1, 2, 3], [4, 5, 6]])
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
x = np.array([[1], [2], [3]])
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