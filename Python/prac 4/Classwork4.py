# ----------------- DECOR -----------------
from student import *


def decor(fun):
    def inner():
        value = fun()
        return value + 2
    return inner()

# def num():
#     return 10

# result_fun = decor(num)
# print(result_fun)


@decor
def num():
    return 10


print(num)

# ----------------- Generator --------------------


def mygen(x, y):
    while x <= y:
        yield x
        x += 1


g = mygen(5, 10)

for i in g:
    print(i)

# ******************************************** CLASS **************************************************


class Classname(object):

    name = "Ayush"

    def __init__(self):
        print(self.name)


c = Classname()


class Student:
    def __init__(self):
        self.name = "Ayush"

    def talk(self):
        print("Hi i am ", self.name)


s = Student()
s.talk()

# ------- Instance method --------


class Student:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def avg(self):
        return (self.a + self.b)/2


s1 = Student(10, 20)
print(s1.avg())

# CLASSMETHOD


class Student:
    name = "Ayush"

    def __init__(self) -> None:
        pass

    @classmethod
    def info(cls):
        return cls.name


s1 = Student()
print(s1.info())

# # STATIC METHOD


class Fact:
    def __init__(self, fact) -> None:
        self.fact = fact

    @staticmethod
    def findFact(fact):
        prod = 1
        for i in range(1, fact+1):
            prod = prod*i
        return prod


# fact1 = Fact(10)
# print(fact1.fact)
# print(Fact.findFact(5))

# SUPER
class EndSemMarks():
    def __init__(self, m1, m2, m3, m4, m5, m6) -> None:
        print("End Sem marks: ", (m1+m2+m3+m4+m5+m6))


class Marks(EndSemMarks, Fact):
    def __init__(self, m1, m2, m3, m4, m5, m6):
        super().__init__(75, 75, 75, 75, 75, 75)
        print("TT Marks: ", (m1+m2+m3+m4+m5+m6))


stud = Marks(25, 25, 25, 25, 25, 25)

# Q)Write a program to create a student class and store it in student.py module. WAP to use the student class to access the methods available in student.py.
# Methods: setID, getID , setName , getName , setAdd,getAdd , setMarks , getMarks


s1 = Student()
s1.setID(177)
print("ID: ", s1.getID())
s1.setName("Ayush")
print("Name: ", s1.getName())
s1.setMarks(100)
print("Marks: ", s1.getMarks())
s1.setAddr("SION")
print("Addr: ", s1.getAddr())

# Q)WAPP to convert decimal to binary using recursion
# Q)WAPP to multiply 2 matrices using numpy
# Q)WAPP to merge two dictionaries
