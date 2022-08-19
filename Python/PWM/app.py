# # 2 Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.
# import math
# import random
# import matplotlib.pyplot as plt
# # create random data
# no_of_balls = 25
# x = [random.triangular() for i in range(no_of_balls)]
# y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
# # draw the plot
# plt.figure()
# plt.scatter(x, y, alpha=0.85)
# plt.axis([0.0, 1.0, 0.0, 1.0])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # 3 Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students. Sample data: math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# import matplotlib.pyplot as plt
# import pandas as pd
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# plt.scatter(marks_range, math_marks, label='Math marks', color='r')
# plt.scatter(marks_range, science_marks, label='Science marks', color='g')
# plt.title('Scatter Plot')
# plt.xlabel('Marks Range')
# plt.ylabel('Marks Scored')
# plt.legend()
# plt.show()

# 4 Write a Python script to concatenate following dictionaries to create a new one. Sample Dictionary:
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dict4 = {}

# for x in (dic1, dic2, dic3):
#     print(x)
#     dict4.update(x)
#     print(dict4)

# print(dict4)

# # 5 Write a Python script to check whether a given key already exists in a dictionary.
# dict1 = {1: 10, 2: 20, 3: 30, 4: 40}
# x = int(input('Enter key: '))
# try:
#     if(dict1[x]):
#         print("Key exists")
# except:
#     print("Key does not exist")

# 6 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).Sample Dictionary ( n = 5) : Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n = int(input("Enter no: "))
# dict1 = {}
# for i in range(1, n+1):
#     dict1[i] = i*i
# print(dict1)

# 7 Remove key from dictionary:
# n = int(input("Enter key: "))
# dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# dict1.pop(n)
# print(dict1)

# # 8 Write a Python program to map two lists into a dictionary.
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [10, 20, 30, 40, 50, 60]
# dict1 = {}
# for i in range(len(list1)):
#     x = {list1[i]: list2[i]}
#     dict1.update(x)
# print(dict1)

# # 9 Write a Python program to print all unique values in a dictionary
# # Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# l = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#      {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# values = []
# for i in l:
#     for y in i.values():
#         if(y not in values):
#             values.append(y)
# print(values)

# # 10 Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
# string = input("Enter: ")
# my_dict = {}
# for letter in string:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# # 11 Write a program that takes a sentence as an input parameter where each word in the sentence is separated by a space. Then replace each blank with a hyphen and then print the modified sentence.
# sentence = input("Enter sentence: ")
# sentence = sentence.replace(" ", "-")
# print(sentence)

# # 12 Write a program to randomly select 10 integer elements from range 100 to 200 and find the smallest among all.
# import random

# list1 = []
# for i in range(10):
#     list1.append(random.randint(100, 200))
# print(list1)
# print(min(list1))

# # 13 Create a dictionary of 5 countries with their currency details and display them.
# # Print as below
# # First line
# # Second line
# # Third Line

# countries = {
#     'India': 'Rupee',
#     'USA': 'Dollar',
#     'UK': 'Euro',
#     'Australia': 'Australian Dollar',
#     'Dubai': 'Dinar'
# }
# for i, j in countries.items():
#     print(i, j)

# # 14 Declare complex number, find data type, real part, imaginary part, complex conjugate, absolute value of a number
# from math import sqrt


# x = 2
# y = 3
# z = complex(x, y)
# print(z)
# print("Real", z.real)
# print("Imaginary", z.imag)
# print("Type:", type(z))
# z1 = complex(x, -y)
# print("Complex congugate: ", z1)
# print("Absolue value: ", sqrt(x**2 + y**2))

# 15 Change string hello to help  ,remove white spaces before word if  s=”   hello ”
# sent = input("Enter: ")
# words = sent.split()
# print(words)
# final_sent = ""
# for word in words:
#     if(word.lower() == 'hello'):
#         final_sent += 'help '
#     else:
#         final_sent += word + " "
# print(final_sent)

# 16 Write a program to randomly select 10 integer elements from range 100 to 200 and find the smallest among all.
# # same as 12

# # 17 Swap first & last letter of a string
# sent = "Aakad Bakkad bombay boo"
# end = sent[-1]
# start = sent[0]
# new_sent = end + sent[1:-1] + start
# print(new_sent)

# 18 Find if substring is present in string or not
# sent = input("Enter string: ")
# sub_sent = input("Enter sub string: ")
# if(sub_sent in sent):
#     print("Present")
# else:
#     print("Not present")

# 19 Write a program that takes a sentence as an input parameter where each word in the sentence is separated by a space. Then replace each blank with a hyphen and then print the modified sentence.
# #  Same as 11

# # 20 WAPP to test whether string is palindrome or not
# sent = input("Enter string: ")
# if(sent == sent[::-1]):
#     print("Palindrome")
# else:
#     print("Not palindrome")

# # 21 WAP to capitalize the first character of each words from a given sentence(example: all the best All The Best)
# sent = "all the best"
# sent = sent.title()
# print(sent)

# # 22 WAP to count the frequency of occurrence of a given character in a given line of text
# sent = input("Enter: ")
# dict1 = {}
# for letter in sent:
#     dict1[letter] = dict1.get(letter, 0) + 1
# print(dict1)

# # 23 Create a dictionary of 4 states with their capital details & add one more pair to the same
# states = {
#     'Maharashtra': 'Mumbai',
#     'abc': 'def'
# }
# states.update({'state': 'capital'})
# print(states)

# # 24 To count number digits, special symbols from the given sentence. Also count number of vowels and consonants
# from curses.ascii import isalnum


# sent = input("Enter: ")
# vowels = ['a', 'e', 'i', 'o', 'u']
# vn = 0
# cn = 0
# number = 0
# special = 0
# for letter in sent:
#     if(letter.isdigit()):
#         number += 1
#     if(not isalnum(letter) and letter != " "):
#         special += 1
#     if(letter in vowels):
#         vn += 1
#     elif(letter != " "):
#         cn += 1
# print(sent)
# print("VN:", vn)
# print("CN:", cn)
# print("Number:", number)
# print("Special", special)

# # 25 Write a program to accept any string up to 15 characters. Display the elements of string with their element nos
# while(True):
#     try:
#         sent = input("Enter upto 15: ")
#         if(len(sent) > 15):
#             raise(TypeError)
#         break
#     except TypeError:
#         print("String rejected. Enter string only<=15")

# for i in range(len(sent)):
#     print(i, sent[i])

# # 26 Create a Numpy array filled with all ones
# import numpy as np

# n = int(input("Enter n:"))
# arr = np.ones(n, dtype=int)
# print(arr)

# 27 Check whether a Numpy array contains a specified row
# import numpy as np
# num = np.arange(20)
# print(num)
# arr1 = np.reshape(num, [4, 5])
# print("Original array:")
# print(arr1)
# print([0, 1, 2, 3, 4] in arr1.tolist())
# print([0, 1, 2, 3, 5] in arr1.tolist())
# print([15, 16, 17, 18, 19] in arr1.tolist())

# # 28 Compute mathematical operations on Array, Add & Multiply two matrices
# import numpy as np
# arr1 = np.array([[1, 2], [3, 4], [5, 6]])
# arr2 = np.array([[5, 6, 7], [8, 9, 10]])
# # multily
# arr3 = np.dot(arr1, arr2)
# print(arr3)
# # add
# # arr4 = np.add(arr1, arr2)
# # print(arr4)

# # 29 Find the most frequent value in a NumPy array
# import numpy as np
# x = np.random.randint(0, 10, 40)
# print("Original array:")
# print(x)
# print("Most frequent value in the above array:")
# print(np.bincount(x).argmax())

# 30 Flatten a 2d numpy array into 1d array
# import numpy as np


# arr1 = np.array([[1, 2], [3, 4]])
# newarr = arr1.flatten()
# # newarr = arr1.reshape(-1)
# print(newarr)

# 31 Calculate the sum of all columns in a 2D NumPy array
# import numpy as np
# arr1 = np.array([[1, 2], [3, 4]])
# print(np.sum(arr1, axis=0))

# # 32 Calculate the average, variance and standard deviation in Python using NumPy
# import numpy as np
# arr1 = np.arange(10).reshape(2, 5)
# print(np.average(arr1))
# print(np.var(arr1))
# print(np.std(arr1))

# # 33 Insert a space between characters of all the elements of a given NumPy array['Python' 'is' 'easy']['P y t h o n' 'i s' 'e a s y']
# import numpy as np
# arr1 = np.array(['Python', 'is', 'easy'])
# arr2 = np.array([])
# print(arr1)
# for i in arr1:
#     msg = ""
#     for letter in i:
#         msg += letter + " "
#     arr2 = np.append(arr2, msg)
#     print(msg)
# print(arr2)

# # 34 Plot line graph from NumPy array
# from matplotlib import pyplot as plt
# import numpy as np
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# plt.plot(x, y, "o")
# plt.show()

# # 35 WAP to Reverse a Number
# n = input("Enter no: ")
# n1 = int(n[::-1])
# print(n1)

# # 36 WAP to read number N and print natural numbers summation pattern
# n = int(input("Enter no: "))
# for i in range(1, n+1):
#     arr = []
#     sum = 0
#     msg = ""
#     for j in range(1, i+1):
#         sum += j
#         arr.append(j)
#     for j in range(len(arr)):
#         if(len(arr) != 1 and j < len(arr)-1):
#             msg += str(arr[j]) + " + "
#         else:
#             msg += str(arr[j])
#     print(msg + " = " + str(sum))

# # 37 WAP to determine all Pythagorean triplets
# a = int(input("Enter range:"))

# for i in range(1, a):
#     for j in range(i, a):
#         for k in range(j, a):
#             if(i**2 == j**2 + k ** 2 or j**2 == k**2 + i**2 or k**2 == i**2 + j**2):
#                 print("Pythagorean triplet: ", i, j, k)

# # 38 WAP, You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit(i.e. 0 to 1 or 1 to 0) only. If it is possible to make all the digits same by just flipping one digit then print 'YES' else print 'NO'.

# import numpy as np


# a = input("Enter no: ")
# arr = []
# for i in range(len(a)):
#     arr.append(int(a[i]))
# zero_array = list(np.zeros(len(a), dtype=int))
# one_array = list(np.ones(len(a), dtype=int))
# for i in range(len(a)):
#     if(arr[i] == 0):
#         arr[i] = 1
#     else:
#         arr[i] = 0
#     if(arr == zero_array or arr == one_array):
#         flag = 1
#         break
#     else:
#         flag = 0
#     if(arr[i] == 0):
#         arr[i] = 1
#     else:
#         arr[i] = 0
# if(flag == 1):
#     print("YES")
# else:
#     print("NO")

# # 39 Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order

# list1 = [1, 2, 6, 4, 3, 5]
# sortedList = list1.copy()
# sortedList.sort()
# i = len(list1)
# moves = 0
# while(i > 0 and sortedList != list1):
#     x = max(list1[:i])
#     list1.remove(x)
#     i -= 1
#     list1.insert(i, x)
#     moves += 1
# print("Sorted List: ", list1)
# print("Moves required: ", moves)

# 40 WAP to print following pattern
# 1\n
# 22\n
# 333\n
# 4444\n
# 55555\n
# 666666
# rows_req = 6
# for i in range(1, rows_req+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# 41 Convert two lists into a dictionary
# # SAME as 8

# 42 Check how many times a given number can be divided by 6 before it is less than or equal to 10.
# n = int(input("Enter no: "))
# div_times = 0
# while(n > 10):
#     n = n//6
#     if(n > 10):
#         div_times += 1
# print(div_times)

# 43 Python program to read a file and Capitalize the first letter of every word in the file

# f = open('test.txt')
# for line in f:
#     print(line.title())

# 44 Python program that reads a text file and counts number of times certain letter appears in the text file

# f = open('test.txt')
# for line in f:
#     for letter in line:
#         if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
#             print(letter, end=" ")

# 45 Write a program to write content to file &  append data to file

# f = open('test.txt', 'w')
# f.write("Hello World")
# f.close()

# f = open('test.txt', 'a')
# f.write("\nHello World")

# 46 Python program to read the contents of a file

# f = open('test.txt')
# f.read()

# 47 Copy the contents from one file to another file

# f = open('test.txt')
# k = open('test1.txt', 'w')
# k.write(f.read())

# 48 WAP to accept name and roll number of students and store it in file. Read and display the stored data. Also check if file exists or not

# try:
#     f = open('student.txt', 'r')
# except:
#     print("file does not exist")
#     exit()
# print(f.read())
# f.close()

# f = open('student.txt', 'w')
# n = int(input('Enter no. of students: '))
# for i in range(n):
#     name = input("Enter name: ")
#     roll = int(input("Enter roll no: "))
#     f.write(f"{i+1}. Name: {name} Roll No: {roll}\n")
# f.close()

# f = open('student.txt', 'r')
# print(f.read())
# f.close()

# 49 WAP to copy contents of 1 file to another Let user specify name of source and destination files
#  # SAME AS 47. Just add a prompt to ask user to enter source and destination file names

# 50 Python program to read file word by word
# f = open('test.txt')
# for line in f:
#     for word in line.split():
#         print("Word: ", word)


# 51 Python program to read character by character from a file
# f = open('test.txt')
# for line in f:
#     for character in line:
#         print("Character: ", character)

# 52 Python – Get number of characters, words, spaces and lines in a file
# EASY

# 53 Make your exception class “InvalidMarks” which is thrown when marks obtained by student exceeds 100

# class InvalidMarks(Exception):
#     def __init__(self, message):
#         self.message = message


# try:
#     marks = int(input("Enter marks: "))
#     if(marks > 100):
#         raise InvalidMarks("Error: Marks cannot be greater than 100")
# except InvalidMarks as e:
#     print(e.message)

# 54 WAP that accepts the values of a, b, c and d. Calculate and display ((a+d) + (b*c))/ (b*d). create user defined exception to display proper message when value of (b*d) is zero

# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))

# try:
#     if(b*d == 0):
#         raise MyException("Error: b*d cannot be zero")
#     else:
#         print(((a+d) + (b*c)) / (b*d))
# except MyException as e:
#     print(e.message)

# 55 Ask user to input an age. Raise an exception for age less than 18 , print message “ age is not valid ” & “age is valid ” if age entered is more than 18
# SAME AS 54

# 56 Handle the FileNotFoundError exception
# try:
#     f = open('abc.txt', 'r')
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")

# 57 Raise a TypeError if x is not a string
# x = 5
# try:
#     raise TypeError("x is not a string")
# except TypeError as e:
#     print(e)

# 58 Create class Complex , define two methods init to take real & imaginary number & method add to add real & imaginary part of complex number . print addition of real part & addition of imaginary part.

# class Complex:
#     def __init__(self, real=0, imag=0):
#         self.real = real
#         self.imag = imag

#     def add(self, other):
#         return self.real + other.real, self.imag + other.imag


# c1 = Complex(3, 4)
# c2 = Complex(5, 6)
# c3 = Complex()
# c3.real, c3.imag = c1.add(c2)
# print(c3.real, c3.imag)


# 59 Create class Triangle, Create object from it . The objects will have 3 attributes named a,b,c  that represent sides of triangle .Triangle class will have two methods init method to initialize the sides & method to calculate perimeter of triangle from its sides . Perimeter of triangle should be printed from outside the class

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def calPerimeter(self):
#         return self.a + self.b + self.c


# t1 = Triangle(10, 20, 30)
# print(t1.calPerimeter())

# 60 Python program to append ,delete and display elements of a list using classe
# class list_class():
#    def __init__(self):
#       self.n = []

#    def add_val(self, a):
#       return self.n.append(a)

#    def remove_val(self, b):
#       self.n.remove(b)

#    def display_val(self):
#       return (self.n)


# my_instance = list_class()
# choice_val = 1
# while choice_val != 0:
#    print("0. Exit")
#    print("1. Add elements")
#    print("2. Delete element")
#    print("3. Display list")
#    choice_val = int(input("Enter your choice: "))
#    if choice_val == 1:
#       n = int(input("Enter element to add to the list... "))
#       my_instance.add_val(n)
#       print("List: ", my_instance.display_val())
#    elif choice_val == 2:
#       n = int(input("Enter number to delete.."))
#       my_instance.remove_val(n)
#       print("List: ", my_instance.display_val())
#    elif choice_val == 3:
#       print("List: ", my_instance.display_val())
#    elif choice_val == 0:
#       print("Exit")
#    else:
#       print("Invalid choice!")
# print()

# 61 Write a program  to create a class which performs basic calculator operations
# class Calculator:
#     def __init__(self) -> None:
#         pass

#     def add(self, a, b):
#         return a + b

#     def sub(self, a, b):
#         return a-b

#     def mul(self, a, b):
#         return a*b

#     def div(self, a, b):
#         return a/b


# calc = Calculator()
# print(calc.add(1, 2))
# print(calc.sub(20, 3))
# print(calc.mul(4, 17))
# print(calc.div(50, 13))

# # 62 Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.

# class Student:
#     def __init__(self, student_id, student_name):
#         self.student_id = student_id
#         self.student_name = student_name

#     def display(self):
#         print("Student ID: ", self.student_id)
#         print("Student Name: ", self.student_name)
#         try:
#             print("Student Class: ", self.student_class)
#         except:
#             print("Student class not defined")


# s1 = Student(177, 'Ayush')
# s1.display()
# s2 = Student(120, 'Mihika')
# s2.student_class = 'B4'
# s2.display()

# 63 Write a Python class to reverse a string word by word.
# class Reverse:
#     def __init__(self, sent) -> None:
#         self.sent = sent

#     def reverse(self):
#         return self.sent.split()[::-1]


# r1 = Reverse("Hello!, This is Ayush")
# print(r1.reverse())

# 64 Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

# class String_Class:
#     def get_string(self):
#         self.string = input("Enter a string: ")

#     def print_string(self):
#         print(self.string.upper())


# s1 = String_Class()
# s1.get_string()
# s1.print_string()

# 65 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
# from scipy import constants


# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def area(self):
#         print(constants.pi*self.radius**2)

#     def perimeter(self):
#         print(constants.pi*2*self.radius)


# c1 = Circle(5)
# c1.area()
# c1.perimeter()

# 66 Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def display(self):
#         print("Max Speed: ", self.max_speed)
#         print("Mileage: ", self.mileage)


# class Bus(Vehicle):
#     def __init__(self, max_speed, mileage, bus_type):
#         super().__init__(max_speed, mileage)
#         self.bus_type = bus_type

#     def display(self):
#         super().display()
#         print("Bus Type: ", self.bus_type)


# b1 = Bus(100, 10, "AC")
# b1.display()

# 67 Load a dataset using pandas : perform basic operations , data visualization using matplotlib ,seaborn etc

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('student.csv')
# print(df)
# plt.plot(df['id'], df['mark'])
# plt.xlabel('id')
# plt.ylabel('Marks')
# plt.show()

# # 68 WAPP to push all zeros to the end of a given list. The order of elements should not change:
# # Input: 0 2 3 4 6 7 9 0
# # Output:2 3 4 6 7 9 0 0

# # list1 = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0]
# n = int(input("Enter list length: "))
# print("Enter no: \n")
# list1 = []
# for i in range(n):
#     list1.append(int(input()))
# for i in range(len(list1)):
#     if list1[i] == 0:
#         list1.pop(i)
#         list1.append(0)
# print(list1)

# 69
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma separated sequence after sorting them alphabetically.
# Input: without, hello,bag, world
# Output: bag,hello,without,world

# sent = input("Enter a sentence: ").split(',')
# final_str = []
# for word in sent:
#     final_str.append(word.strip())
# final_str.sort()
# for word in final_str:
# print(word, end=',')


# 70
# WAP that calculates & prints value accoridng to given formula:
# Q=Square root of [(2*C*D)/H]
# C is 50 , H is 30. D is variable whose values should be input to program in comma separated sequence.
# Input: 100,150,180
# Output:18,22,24


# 71
# With given list L of integers, write a program that prints this L after removing duplicate values with original order preserved.
# Input: 12 24 35 24 88 120 155 88 120 155
# Output: 12 24 35 88 120 155
# list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# 72
# Given ab integer number n , define function named printDict(),which can print a dictionary where keys are numbers between 1 to n (both included) and values are square of keys . Function printDict(), does not take any arguments.
# n = 5
# def print_dict():
#     dict1 = {}
#     for i in range(1, n+1):
#         dict1[i] = i**2
#     print(dict1)
# print_dict()

# 73
# Python program to find the sum of the digits of an integer using while loop

# 74
# Python program to generate the prime numbers from 1 to N

# 75
# Python program to print the numbers from a given number n till 0 using recursion
# def rec(n):
#     if n == 0:
#         return
#     print(n)
#     rec(n-1)


# rec(5)

# 76
# Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
import numpy as np
import pandas as pd


def student_data(id, *args):
    print("Student ID: ", id)
    if args:
        try:
            print("Student Name: ", args[0])
        except:
            pass
        try:
            print("Student Class: ", args[1])
        except:
            pass


student_data('177', 'Ayush', 'B4')

# 77
# Write a Python class to convert a roman numeral to an integer

# 78
# Write a Python class to get all possible unique subsets from a set of distinct integers

# 79
# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number
# 80
# Write a Python class to implement pow(x, n).
# 81
# Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees and vice versa. Values are stored into a NumPy array. Sample Array [0, 12, 45.21, 34, 99.91]
# 82
# Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2
# 83
# Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. Go to the editor Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
# 84
# Write a Pandas program to get the first 3 rows of a given DataFrame
# 85
# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
# 86
# Write a Pandas program to select the specified columns and rows from a given data frame.
# 87
# Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
# 88
# Write a Pandas program to count the number of rows and columns of a DataFrame.
# 89
# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
# 90
# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15
# 91
# Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame
# 92
# Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# print("Orginal rows:")
# print(df)
# df.sort_values(by=['name', 'score'], ascending=[False, True])
# print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
# print(df)

# 93
# Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# print("Original rows:")
# print(df)
# print("\nReplace the 'qualify' column contains the values 'yes' and 'no'  with True and  False:")
# df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
# print(df)

# 94
# Write a Pandas program to set a given value for particular cell in DataFrame using index value.
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# df = pd.DataFrame(exam_data)
# print("Original DataFrame")
# print(df)
# print("\nSet a given value for particular cell in the DataFrame")
# df.set_value(8, 'score', 10.2)
# print(df)
