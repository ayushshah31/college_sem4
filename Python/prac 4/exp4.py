# Q1) WAP to Reverse a Number
# num1 = int(input("Enter a number: "))
# rev = 0
# while(num1 > 0):
#     rev = rev*10 + (num1 % 10)
#     num1 = int(num1/10)

# print("Reverse Number: ", rev)

# Q2)WAP to read number N and print natural numbers summation pattern
# n = int(input("Enter N: "))
# sum = 0

# for i in range(1, n+1):
#     sum += i
#     for j in range(1, i+1):
#         if(j != i):
#             print(j, " + ", end=" ")
#         else:
#             print(j, " = ", end=" ")
#     print(sum)

# Q3) WAP to determine all Pythagorean triplets
# def pythagorean_triplets(limits):
#     c, m = 0, 2
#     while c < limits:
#         for n in range(1, m):
#             a = m * m - n * n
#             b = 2 * m * n
#             c = m * m + n * n
#             if c > limits:
#                 break
#             print(a, b, c)
#         m = m + 1


# limit = int(input("Enter limit: "))
# print("The Pythagorean triplets are :")
# pythagorean_triplets(limit)

# Q4) WAP, You are given a number A which contains only digits 0's and 1's.
# Your task is to make all digits same by just flipping one digit(i.e. 0 to 1 or 1 to 0) only.
# If it is possible to make all the digits same by just flipping one digit then print 'YES' else print 'NO'.

# inp_num = input("Enter binary numbr: ")
# num = list(inp_num)
# num_copy = num.copy()
# ans = False
# for i in range(len(inp_num)):
#     if(num[i] == "0"):
#         num[i] = "1"
#     else:
#         num[i] = "0"
#     # print("i=", i, " num=", num)
#     for j in range(len(inp_num)-1):
#         if(num[j] != num[j+1]):
#             ans = False
#             break
#         else:
#             ans = True
#     if(ans):
#         print("YES")
#         break
#     num = num_copy.copy()

# if(ans == False):
#     print("NO")

# Q5) WAP, Given a list A of N distinct integer numbers, you can sort the list by moving an element
# to the end of the list. Find the minimum number of moves required to sort the list using this method
# in ascending order

list1 = [177, 4, 9, 24, 50, 20, 1]
sortedList = list1.copy()
sortedList.sort()
i = len(list1)
moves = 0
while(i > 0 and sortedList != list1):
    x = max(list1[:i])
    list1.remove(x)
    i -= 1
    list1.insert(i, x)
    moves += 1
print("Sorted List: ", list1)
print("Moves required: ", moves)
