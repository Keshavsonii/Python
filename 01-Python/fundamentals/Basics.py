# Fundamentals of Python Programming
Name = "Keshav"
Age  = 25
Price  = 100.50
Age2 = Age
New = True
print("My name is :", Name)
print("My age is :", Age)
print("The price is :", Price)
print(type(Name))
print(type(Age))
print(type(Price))
print(type(New))


# Expresion Execution
a, b = 3, 4
txt = "#"
print(2 * 3 * txt)

c, d = "5", 4
e = "@"
print((c + e) * d)

f, g = 4, 5
i = 5
print(f + g * i)

j, k = 10, 0.6
l = j * k
print(l)

m, n = 2, 5
o = m / n
print(o)

p, q = 1.6, 5
r = p // q
print(r, p / q)

a,b,c = 3,4,"5"
Txt = "@"
print(a*(c+Txt))

from math import floor
a = 19.2
b = 2
c = a//b
d = a/b
e = floor(a/b)
print(c,d,e)


# Inputs
Name = input("enter your name: ")
Age   = int(input("enter your age: "))
Price = float(input("enter the price: "))

print("Name is :", Name)
print("Age is :", Age)
print("Price is :", Price)

name = input("name :")
age = int(input("age = :"))
price = float(input("price:"))
print("my name is", name, "and my age is", age, "i buy flowers that cost", price)

# Conditional Statements
light = input("light :")
if light == "red":
    print("stop")
elif light == "green":
    print("go")
elif light == "orange":
    print("look out")
else:
    print("light is broken and not working")


marks = int(input("enter your marks:"))
if(marks>=90 and marks<=100):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("grade b")
elif(marks>=70 and marks<80):
    print("grade c")
elif(marks>100):
    print("invalid")
else:
    print("grade d")


marks = int(input("marks : "))
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("fail")


A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")


# Single line if / ternary operator
# <var> = <val1> if <condition> else <val2>

food = input("Name of dessert :")
eat = "yes" if food == "cake" else "no"
print(eat)

# <stt1> if <condition> else <stt2>
food = input("food :")
print("i like it ") if food == "cake" or food == "burfi" else print ("i do not like it")

# Clever if

age = int(input("enter your age: "))
vote = ("yes", "no")[age <= 18]
print(vote)

age = int(input("age : "))
vote = ("no", "yes")[age >= 19]
print(vote)

# Operators
a = 50
b = 20
print(a == b, a != b, a <= b, a > b, a < b)

num = 20
num += 10
num -= 10
num *= 10
num /= 10
num %= 10
num **= 10
print(num)


a = 50
b = 10
print(not False)
print(not True)
print (not(a < b))

val1 = False
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)
print("OR operator:", (a==b) or (a > b))

# Strings

str = "this is a string \nthis is also a string \tit can be written like this too"
print(str)

a = "this is a string "
b  = "and it is joined"
print(a + b)
print(len(a))
print(len(str))
print(a[4])
print(b[5])
print(a[0:7])
print(b[:9])
print(b[0:])
print(b[0:5])
print(b[-5:])
print(b[-11: -2])

str = "this is a practice line by me"
print(str.endswith("me"))
print(str)
print(str.capitalize())
print(str.replace("line", "string"))
print(str.find("by"))
print(str.count("is"))


# lists
marks1 = 2
marks2 = 4
marks3 = 5
marks4 = 9

marks = [22, 12, 45, 66, 5, 100]
print(marks)
print(type(marks))
print(len(marks))
print(marks[4])
print(marks[0:3])

student = ["karan", 21, "delhi", "male", 92, "A"]
student[0] = "arjun"
print(student)
print(student[2])


slc = student[1:5]
slc2 = student[0:-1]
print(slc, slc2)


numbers = [23, 65, 345, 76, 34, 2, 3, 32, 322, 6543, 3, 666, 33]
numbers.append(1)
numbers.sort()
numbers.sort(reverse=True)
numbers.reverse()
numbers.insert(0, 21)
numbers.remove(3)
numbers.pop(9)

print(numbers)

# tuples
number = (21, 55, 91, 9, 66, 4, 9)
print(type(number))
print(number[2])

tup = ()
print(tup)
print(type(tup))

tuple = (5,)
print(type(tuple))

number.index(2)
number.count(9)


# dictionary
heredict = {
    "name": "keshav",
    "cgpa": "8",
    "university": "MRIIRS",
    "age": 21,
    "subject": {"dsa": "A", "os": "B", "cn": "A", "math": "C"},
    "place": "faridbad",
}
print(heredict["name"])
print(heredict["subject"])


heredict["name"] = "soni"
heredict["bollean"] = True
print(heredict)


print(heredict.keys())
print(heredict.values())
print(heredict.items())
print(heredict.get("bollean"))
print(heredict.update({"float": 13.34}))
heredict.update({"place": "delhi"})
print(heredict)

# sets
collection = {
    1,
    2,
    2,
    2,
    3,
    4,
    5,
    7,
    7,
    8,
    9,
}
print(len(collection))
print(type(collection))
print(collection)

emptyset = set()
print(emptyset)

emptyset = set()
emptyset.add(2)
emptyset.add(4)
emptyset.add("keshav")
emptyset.remove("keshav")
emptyset.add((1, 2, 3, 4, 5, 6, 7))
emptyset.clear()
emptyset.pop()
print(emptyset)


set1 = {
    1,
    3,
    5,
    7,
    9,
}
set2 = {1, 2, 3, 4, 6, 8}
print(set1.union(set2))
print(set1.intersection(set2))






# while
count = 1
while count <= 5:
    print("hello")
    count += 1

i = 1
while i <= 5:
    print(i, "keshav")
    i += 1
print("loop ended")


# for
str = "keshavsoni"
for val in str:
    if val == "v":
        print("v found")
        break
    print(val)
else:
    print("end")

# range
for i in range(1, 100, 2):
    print(i)


# functions
# function definition
def calsum(a, b):  # parameters
    return a * b


sum = calsum(3, 8)  # fxn calling,arguments
print(sum)
