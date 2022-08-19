# MOR

# Q) write down classes father and mother each initialized with the features of height and colour
#   Demonstarte MRO by giving the dominant set of features for the child

# class Father:
#     def method(self, height=180, colour="white"):
#         self.height = height
#         self.colour = colour
#         print("Father Dominant\n height: ",
#               self.height, ", Colour: ", self.colour)


# class Mother:
#     def method(self, height=170, colour="black"):
#         self.height = height
#         self.colour = colour
#         print("Mother Dominant\n height: ",
#               self.height, ", Colour: ", self.colour)


# class paternal(Father, Mother):
#     pass


# class maternal(Mother, Father):
#     pass


# p = paternal()
# m = maternal()
# pref = int(input("Which side if more dominant: 1.Father 2.Mother\n"))
# if(pref == 1):
#     p.method()
# else:
#     m.method()
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return "({0},{1})".format(self.x, self.y)

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1+p2)

# Q) Demonstarte operator overloading by writing two classes ramayana and Mahabharata .
# Take the page no. of the book in the constructor and print the book with the highest page no.

# -------------METHOD OVERLOAD----------------

class Example:
    def sum(self, a=0, b=0, c=0):
        print(a+b+c)


e = Example()
e.sum(1, 2)
