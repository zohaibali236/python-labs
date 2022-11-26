grades = ['B', 'B' , 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B']

grades.sort()
x = []
y = []
for i in grades:
    if(i not in y):
        y.append(i)
        z = grades.count(i)
        x.append(int(z))

print(x)

for i in range(7):
    for j in range(3):
        if((i >= 1 or i <= 5) and (i != 3 and i != 0)):
            if(j == 1):
                print( end="   ")
            else: print("*", end="")
        elif(i == 3): print("***", end="\b\b")
        else: print("*", end=" ")
    print(end="\n")

for i in range(9):
    for j in range(3):
        if(i == 0):
            if(j == 0):
                print("   * ", end="")
            else: print("* * *", end="\b")
        elif((i >= 1 or i <= 5) and (i != 4 and i != 0)):
            if(j == 1):
                print(end="\t")
            else: print("*", end="\t")
        elif(i == 4): print("* * * ", end="")
        else: print("*", end="\t")
    print(end="\n")

for i in range(9):
    for j in range(i+1):
        print(i+1, end="")
    print(end="\n")

for i in range (3,0,-1):
    for j in range(i):
        print(j+1, end="")
    print(end="\n")


for i in range(10):
    for j in range(i):
        print("*", end="")
    print(end="\n")



for i in range (20, 10, -3):
    for j in range(2):
        if(j==1 and i == 11): break
        print(i, end = " ")

def xmult(a, b):
    c = []
    for i in a:
        for j in b:
            c.append(i*j)
    return c

print(xmult([2,3], [3,4]))


list_1 = []
list_2 = []

input_1 = input("Enter the first list(use space as separator) ")
input_2 = input("Enter second list(use space as separator) ")

list_1 = input_1.split()
list_2 = input_2.split()

for i in range(len(list_1)):
    list_1[i] = int(list_1[i])

for i in range(len(list_2)):
    list_2[i] = int(list_2[i])

def digitSplitter(a):
    firstDigit = (a//1000)
    secondDigit = (a//100 - (firstDigit)*10)
    thirdDigit = (a//10 - (a//100)*10)
    fourthDigit = (a - (a//10)*10)

    print(f"{firstDigit}\n{secondDigit}\n{thirdDigit}\n{fourthDigit}")

numbers = input("Enter Four digit number (e.g 1234) ")

if(len(numbers) != 4 or numbers[0] == '0'): print("Error")
else: digitSplitter(int(numbers))

print(1234//1000)
print(1234//100 - (1234//1000)*10)
print(1234//10 - (1234//100)*10)
print(1234-(1234//10)*10)


for i in range(11, 42, 5):
    print(i, end=" ")

print()

for j in range(3, 34, 5):
    print(j, end=" ")

print()

for k in range(20, 10, -3):
    if(k >= 12):
        print(k, k, end=" ")
    else: print(k)

print()

def acronym(phrase):
    phrase = phrase.title()
    for i in phrase:
        if(i.isupper()):
            print(i, end="")

input_phrase = input("Enter the phrase you want to get acronym of ")

acronym(input_phrase)

students_list = (input("Enter the names of students separated by spaces")).split()

for i in students_list:
    for j in i[0]:
        if(ord(j) >=97 and ord(j) <= 109):
            print(i)


month = int(input("Enter the month "))
date = int(input("Enter the date of month"))


if(month == 1 or month == 2 or month == 12):
    print("season is Winter")
elif(month == 3 or month == 4 or month == 5):
    print()


#quadratic equation roots calculator

from cmath import sqrt

a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))

if(a == 0): print("The roots cannot be calculated because of divison with 0")
else:
    x1 = (-b + sqrt((pow(b, 2)) - 4*a*c))/(2*a)
    x2 = (-b - sqrt((pow(b, 2)) - 4*a*c))/(2*a)
    print(f"The roots of the given quadratic eqation are {x1} and {x2}")


for i in range (1,6):
    if(i == 1):
        print("\t", end="")
    elif(i == 2):
        print("       *", end="")
    elif(i == 3):
        print("      **", end="")
    elif(i == 4):
        print("     ***", end="")
    elif(i == 5):
        print("    ****", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range (1,6):
    if(i == 1):
        print("\t", end="")
    else: print("\t"+("\b"*(i-1))+("*"*(i-1)),end="")
    for j in range(i):
        print("*", end="")
    print()


x = [9,2,4,1,5,6]

for _ in range(len(x)-1):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i] , x[i+1] = x[i+1], x[i]
print(x)


n = 4
x = 1
for i in range(4,0,-1):
    if(i == 4): continue
    x = x*i

print(x)

print(round(1.2312312, 3))
print(1//2)

print(isinstance(123, int))


print("ß".lower())

x="AbC"

x.lower()
print(x)

print("as\"asd\"da")

a = 1
print(a, id(a))
a = 2
print(a, id(a))


a = [1,2,3]

print(a*3)

words = ['bat', 'ball', 'barn', 'basket', 'badminton']

for _ in range(len(words) - 1):
    for i in range(len(words)-1):
        if(words[i] > words[i+1]):
            words[i] , words[i+1] = words[i+1], words[i]
        
print(words)

words = ['bat', 'ball', 'barn', 'basket', 'badminton']
words.sort()

print(words)


l1 = [22,33,44,55,66,77,88,99,11,12,23]
print(l1[-1:5:-3])

print(max(l1))

a=3
b=4

print(a*a+b*b)


a = "sd"
b = 23
c = 2.0

print("%s %i %0.1f" %(a,b,c))

print(list("123 123 123"))

for i in range(20,0,-1):
    print(i)

a = 9
b = 11
while True:
    if a == 0: break
    print(b, end=" ")
    if(b != 11): a -= 1
    b = a+b


a = [11,22,33,44,55,66,77,88,99,100]
print(a[-1:1:-3])
x = 11
print(x, end=" ")

for i in range(9,0,-1):
    x += i
    print(x, end=' ')



print(3//2)

print()

import datetime
print(datetime._is_leap(2000))

print(-10>>1)
