# ************************************************* LOOPS ***********************************************

# 1.---------- If ELse loop -------------
# Q) Check if the user has entered character c
from functools import reduce
charInput = input("Enter char: ")
charInput = charInput.lower()
if(charInput == "a" or charInput == "b" or charInput == "c"):
    print("YES")
else:
    print("NO")

# ------------ 2.While --------------
# Q) Write a python a progtam to display the elements of the list using while loop

list1 = [10, 2, 5, 31, 39, 177, 179, 0]
index = len(list1)-1
while(index >= 0):
    print(list1[index])
    index = index-1

# ------------- 3.FOR -----------------
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
charInput = input("Enter string: ")
nonVowelStr = ""
vowelStr = ""
for letter in charInput:
    if(letter in vowel):
        vowelStr = vowelStr + letter
        continue
    nonVowelStr = nonVowelStr + letter
print("Vowel String: " + vowelStr)
print("Non vowel String: " + nonVowelStr)
print(str(vowel))

# # PASS & Continue
for i in range(5):
    if(i < 3):
        pass
    print(i)
print("_")
for i in range(5):
    if(i < 3):
        continue
    print(i)


# ************************************************* FUNCTION *************************************************
def my_function():
    print("This is a function")


my_function()

# Variable parameters:


def my_function(*kids):
    print("the youngest kid is " + kids[2])


my_function("Shlok", "Kuber", "Gaurav")

# # Q)Write a function to greet


def greet(name):
    print("Hello "+name)
    return name


def health():
    print(greet("Ayush")+" ,How are you?")


health()

# Q) Write a program to pass a list to a function and modify it
list1 = [1, 3, 5, 7, 9]


def modify(x):
    x.append(0)
    print(x, id(x))


modify(list1)
print(list1, id(list1))
# __________________Arguments that can be passed in a function: __________________
# Arbitrary arguments
# Formal arg: defined in the function like def my_function(a,b)
# Actual arg: arguments passed in the function call like my_function(a,b)
# Positional argument: named arguments
# Default Arg: value defined for arg while the function definition like below:


def grocery(item, price=40):
    print("Item: "+item)
    print("Price: " + str(price))


grocery(item="Mango")


def add(farg, *args):
    sum = 0
    for i in args:
        sum = sum + i
    print("Sum: ", sum+farg)


add(1)

# Factorial using recursion function


def fact(n):
    if(n > 1):
        return n * fact(n-1)
    else:
        return 1


print(fact(5))

# Lambda fns
# Write a reduce function to find product of the elements of the list

x = reduce(lambda x, y: x*y, [1, 2, 3])
print(x)
# Write a program to find the squares of a list and store thwe squares in a different list altogether using map
x = map(lambda x: x*x, [1, 2, 3])
print(list(x))
