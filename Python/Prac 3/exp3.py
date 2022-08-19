# Q1) Create a Numpy array filled with all ones
# import numpy

# arr1 = numpy.array([1, 1, 1, 1, 1])
# print(arr1)

# Q2)  Check whether a Numpy array contains a specified row
# import numpy

# arr1 = numpy.array([[1, 2, 3, 4, 5],
#                    [6, 7, 8, 9, 10],
#                    [11, 12, 13, 14, 15],
#                    [16, 17, 18, 19, 20]
#                     ])

# print("Array: \n", arr1)

# # check for some lists
# print("[1, 2, 3, 4, 5] in arr1: ", [1, 2, 3, 4, 5] in arr1.tolist())
# print("[16, 17, 20, 19, 18] in arr1: ", [16, 17, 20, 19, 18] in arr1.tolist())

# Q3) Compute mathematical operations on Array, Add & Multiply two matrices

# import numpy

# arr1 = numpy.array([[2, -7, 5], [-6, 2, 0]])
# arr2 = numpy.array([[5, 8, -5], [3, 6, 9]])

# print("1st Array : \n", arr1)
# print("2nd Array : \n", arr2)

# addArr = numpy.add(arr1, arr2)
# mulArr = numpy.multiply(arr1, arr2)
# print("\nAddition of the two matrices: \n", addArr)
# print("\nMultiplication of the 2 matrices: \n", mulArr)

# Q4) Find the most frequent value in a NumPy array
# import numpy as np

# x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
# print("Array:\n", x)

# print("Most frequent value in above array")
# y = np.bincount(x)
# maximum = max(y)

# for i in range(len(y)):
#     if y[i] == maximum:
#         print(i)

# Q5)  Flatten a 2d numpy array into 1d array
# import numpy as np

# arr1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
# print("Array: \n", str(arr1))
# result = arr1.flatten()
# print("New resulting array: ", result)

# Q6) Calculate the sum of all columns in a 2D NumPy array
# import numpy

# arr = numpy.array([[1, 2, 3], [4, 5, 6],
#                    [7, 8, 9], [10, 11, 12]])
# print("Array:\n", arr)

# print("\nColumn-wise Sum:")
# print(numpy.sum(arr, axis=0))

# Q7) Calculate the average, variance and standard deviation in Python using NumPy
# import numpy

# arr = [2, 4, 4, 4, 5, 5, 7, 9]
# print("Array: ", arr)
# print("Average: ", numpy.average(arr))
# print("Variance: ", numpy.var(arr))
# print("Standard Deviation: ", numpy.std(arr))

# Q8) Insert a space between characters of all the elements of a given NumPy array

# import numpy as np

# arr = np.array(["Hello", "World"])
# print("Original Array:\n", arr)

# result = np.char.join(" ", arr)
# print("The Required Array: ", result)

# Q9) Plot line graph from NumPy array
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(1, 11)
# y = x * x

# plt.title("Line graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.plot(x, y, color="red")
# plt.show()

# Q10) Sort the values in a matrix
import numpy

mat = numpy.matrix('[4, 1, 7; 12, 3, 8]')
print("Matrix:\n", mat)
mat.sort()
print("\nSorted Matrix:\n", mat)
