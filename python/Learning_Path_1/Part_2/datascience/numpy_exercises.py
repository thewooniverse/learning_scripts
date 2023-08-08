import numpy as np

# basics practice
a = np.array([0, 1, 2])
b = np.array([
    [0, 1, 3], 
    [1, 3, 5]
    ])

c = np.zeros((1,10)) # one row, 10 columns
d = np.zeros((10,1)) # ten rows, 1 columns
# print(c)
# print(d)

# Shape of the array (rows, columns)
# print(b.shape)  # Output: (2, 3)
# print(c.shape)  # (1, 10)
# print(d.shape)  # (10, 1)
# print(b.ndim)  # Output: 2
# print(c.ndim)  # Output: 2
# print(d.ndim)  # Output: 2


###### exercises.md - part 1: #####

### Exercise 1: Create and Manipulate Arrays
# 1. Create a one-dimensional NumPy array containing 10 elements filled with zeros.
array_a = np.zeros((1, 10))
# 2. Change the 5th value to 10.
array_a[0,5] = 10
# 3. Print array
print(array_a)



# 1. Create two 3x3 matrices `A` and `B`.
A = np.array([
    [0, 1, 2],
    [1, 2, 3],
    [3, 4, 5]
])
B = np.array([
    [4, 1, 2],
    [1, 5, 3],
    [3, 4, 10]
])

### Exercise 2: Basic Array Operations
# 2. Perform and print the following operations: `A + B`, `A - B`, `A * B` (element-wise multiplication), 
# and the matrix multiplication of `A` and `B`.
AB_matrix_sum = A + B
AB_matrix_difference = A - B
AB_matrix_multiplied = A * B
AB_matrix_divided = A / B

# print(AB_matrix_sum)
# print(AB_matrix_difference)
# print(AB_matrix_multiplied)
# print(AB_matrix_divided)



### Exercise 3: Reshaping and Slicing
# 1. Create a NumPy array of shape (6, 6) filled with random numbers.
R = np.random.randint(1, 10, size=(6, 6))
print(R)
# 2. Extract the first 3 rows and 3 columns as a new array.
RS = R[0:3, 0:3]
print(RS)

# 3. Reshape the array into a shape of (9, 4) without changing its data.
RR = R.reshape(9,4)
print(RR)






### Exercise 4: Statistical Functions
# 1. Create a one-dimensional array of 100 random numbers.
r100 = np.random.randint(1, 10, size=(1, 100))

# 2. Compute and print the mean, median, standard deviation, mode, and sum of the array.




