import numpy as np
import matplotlib.pyplot as plt


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
# print(array_a)



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

print("The value is:")
# print(B[1,1]) #indexing, (row, column)


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
# print(R)

# 2. Extract the first 3 rows and 3 columns as a new array.
RS = R[0:3, 0:3] #0, 1, 2 columns
# print(RS)

# 3. Reshape the array into a shape of (9, 4) without changing its data.
RR = R.reshape(9,4)
# print(RR)



### Exercise 4: Statistical Functions
# 1. Create a one-dimensional array of 100 random numbers.
r100 = np.random.randint(1, 10, size=(1, 100))

# 2. Compute and print the mean, median, standard deviation, mode, and sum of the array.
r100_mean = np.mean(r100)
r100_std_dev = np.std(r100)
r100_median = np.median(r100)
r100_sum = np.sum(r100)

# print(r100_mean, r100_std_dev, r100_median, r100_sum)



### Exercise 5: Boolean Indexing
# 1. Create a 5x5 matrix with random integers between 1 and 100.
r_5x5 = np.random.randint(1, 100, size=(5, 5))
# print(r_5x5)

# 2. Use boolean indexing to replace all the values greater than 50 with 50.
condition = r_5x5 > 50
print(condition)
r_5x5[r_5x5 > 50] = 50
# print(r_5x5)


### Exercise 6: Working with Diagonals and Transpose
# 1. Create a 4x4 matrix.
r_4x4 = np.random.randint(1, 10, size=(4, 4))
# print(r_4x4)

# 2. Print the main diagonal of the matrix.
diagonal = np.diag(r_4x4)
# print(diagonal)
# or, print(np.diag(r_4x4))

# 3. Print the transpose of the matrix.
transposed_r_4x4 = r_4x4.T
# print(transposed_r_4x4)



### Exercise 7: Broadcasting
# 1. Create a 3x3 array filled with random numbers.
r_3x3 = np.random.randint(1, 10, size=(3,3))
print(r_3x3)

# 2. Add the one-dimensional array `[1, 2, 3]` to each row of the 3x3 array.
array_123 = np.array([1, 2, 3])
array_sum = r_3x3 + array_123

# 3. Print the result.
print(array_sum)





### Exercise 8: Solving Linear Equations
# 1. Create a 3x3 matrix `A` and a one-dimensional array `b` of length 3.
A = np.eye(3)
print(A)
print(np.eye(5))
b = np.array([1,2,3])


# 2. Use NumPy's functions to solve the linear equation system `Ax = b`.
x = np.linalg.solve(A, b)

# 3. Print the solution.
# print(x)


# plt.plot(b)
# plt.title('My NumPy Series')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.show()
