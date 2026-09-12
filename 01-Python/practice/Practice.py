a = int(input ("enter your number: "))
b = int(input ("enter your number: "))
print("True") if (a > b) else print("False")


name = input("User name : ")
print(len(name))

str = input("type your string:")
print(str.count("@"))


num = int(input("enter you number : "))
if(num % 2 == 0):
    print("it is even")
else:
    print("it is odd")


a = int(input("enter your number: "))
b = int(input("enter your number: "))
c = int(input("enter your number: "))
if(a>=b or a>=c):
    print(" a is the greatest")
elif(b>=c):
    print("b is the greatest")
else:
    print("c is the greatest")


a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
d = int(input("enter fourth number :"))
if a >= b and a >= c and a >= d:
    print("first number is the largest", a)
elif b >= c and b >= d:
    print("second number is the largest", b)
elif c >= d:
    print("third number is the largest", c)
else:
    print("fourth number is largest", d)


num = int(input("your number :"))
if num % 7 == 0:
    print("it is a multiple of seven")
else:
    print("not a multiple")


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


mov1 = input("enter your movie name :")
mov2 = input("enter your movie name :")
mov3 = input("enter your movie name :")
list = [mov1, mov2, mov3]
print(list)


movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))
print(movies)


list1 = ["m", "a", "a", "m", "p"]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")
