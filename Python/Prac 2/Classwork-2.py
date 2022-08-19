# Practice:
from turtle import circle
import numpy

arr = numpy.array([10, 20, 30, 40])
print(arr)

# Q) Write a python program to create an array of odd integers using linspace
arr = numpy.linspace(1, 19, 10)
print(arr)
arr = numpy.logspace(1, 4, 5)
arr1 = numpy.linspace(1, 19, 10)
arr2 = numpy.arange(9, 0, -2)
print(arr)
print(arr1)
print(arr2)
arr3 = arr2.copy()
arr3[0] = 1
print(arr3)
arr4 = [10, 30, 2]
max = arr4[0]
for i in arr4:
    if(max < i):
        max = i
print(max)

# write a pyhton program to compare 2 arrays and display the resultant boolean type array
arr1 = []
arr2 = []
arr3 = []
print("Enter arr1 elements:")
for i in range(5):
    arr1.append(int(input()))

print("Enter arr1 elements:")
for i in range(5):
    arr2.append(int(input()))

for i in range(5):
    arr3.append(numpy.array_equal(arr1[i], arr2[i]))

print(arr3)

# WAPP to compare elements of two arrays and retrieve the biggest element
arr1 = []
arr2 = []
# arr3 = []
print("Enter arr1 elements:")
for i in range(5):
    arr1.append(int(input()))

print("Enter arr1 elements:")
for i in range(5):
    arr2.append(int(input()))

a = numpy.array([10, 20, 30, 40])
b = a.view()
b[0] = 99
print(a)

# creatr an array with elemets 10-15
# 1- retreive from to 1st to 6-1 elemets with step size of two
# 2- retrieve all elements
# 3- retrieve elements from 4 to 1 in decreasing step size
# 4- retrieve elemets from 0 to 1 prior to 4th elemet

arr = numpy.arange(10, 16, 1)
q1 = arr[1:6:2]
print(q1)
q2 = arr[:]
print(q2)
q3 = arr[4:1:-1]
print(q3)
q4 = arr[0:4]
print(q4)

arr = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

# create an array of 1-10 elements , use reshape method to change the shape of the array in nxm manner

arr = numpy.arange(1, 11, 1)
print(arr.reshape(circle))
