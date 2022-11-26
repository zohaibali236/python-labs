# # # quadratic equation solve
# # from cmath import sqrt

# # a = int(input("Enter value of a "))
# # b = int(input("Enter value of b "))
# # c = int(input("Enter value of c "))

# # if(a == 0): print("The roots cannot be calculated because of divison with 0")
# # else:
# #     x1 = (-b + sqrt((pow(b, 2)) - 4*a*c))/(2*a)
# #     x2 = (-b - sqrt((pow(b, 2)) - 4*a*c))/(2*a)
# #     print(f"The roots of the given quadratic eqation are {x1} and {x2}")

# # def arithmetic_sequnce_calculator(a, n, d):
# #     print((a + (n-1)*d))
# #     ask = int(input("Enter the next term you want to find or enter '-1' to end\n"))
# #     if(ask != -1): arithmetic_sequnce_calculator(a, ask, d)
# #     else: return

# # a = int(input("Enter the value of first term\n"))
# # d = int(input("Enter the common difference\n"))
# # n = int(input("Enter the no of term you want to find\n"))

# # arithmetic_sequnce_calculator(a,n,d)

# # input = input("Enter the phrase to be checked if it is palindrome or not\n")

# # if(input == input[::-1]): print("The given input is palindrome")
# # else: print("Sorry the given input is not palindrome")


# # matrix addition
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# b = [
#     [10,11,12],
#     [13,14,15],
#     [16,17,18]
# ]

# r = [[0 for _ in range(len(a))] for _ in range(len(b))]

# for i in range(len(a)):
#     for j in range(len(b)):
#         r[i][j] += a[i][j] + b[i][j]

# for x in r:
#     print(x)

# matrix multiply
a = []
b = []
r = int(input("rows and columns for both matrices "))

result = [[0 for _ in range(r)]for _ in range(r)]

print()
print("for first matrix\n")
for i in range(r):
    print("for row number", i+1)
    temp = []
    for j in range(r):
        print("Enter values for column number", j+1)
        temp.append(int(input()))
    a.append(temp)

for x in a: print(x)

print("now for second matrix\n")
for i in range(r):
    print("for row number", i+1)
    temp = []
    for j in range(r):
        print("Enter values for column number", j+1)
        temp.append(int(input()))
    b.append(temp)

for x in b: print(x)

print("multiplying a and b\n")
for i in range(r):
    for j in range(r):
        for k in range(r):
            result[i][j] += a[i][k] * b[k][j]

for x in result: print(x)

# # data
# name = input("Enter your name\n")
# father_name = input("Enter your father's name\n")
# roll_no = int(input("Enter your roll no\n"))

# sub_name_marks = []
# for _ in range(5):
#     temp = []
#     for _ in range(1):
#         name = input("Enter subject name\n")
#         marks = int(input("Enter subject marks\n"))
#         temp.append(name)
#         temp.append(marks)
#     sub_name_marks.append(temp)
# print()
# print(f"Name: {name}\nFather's Name: {father_name}\nRoll Number: {roll_no}\n\nSubjects(Marks)")
# for i in sub_name_marks:
#     for j in i:
#         if(isinstance(j, str)): print(j, end="")
#         if(isinstance(j, int)): print(f"({j})")
# print()
# total_marks_obtained = 0
# for i in sub_name_marks:
#     for j in i:
#         if(isinstance(j, int)):
#             total_marks_obtained += j
# percentage = (total_marks_obtained/500)*100

# print("Total marks obtained:", total_marks_obtained)
# print(f"Percentage: {percentage}%")

# if(percentage <= 100 and percentage >= 80): print("Grade: A+")
# elif(percentage <= 79 and percentage >= 70): print("Grade: A")
# elif(percentage <= 69 and percentage >= 50): print("Grade: B")
# elif(percentage <= 49 and percentage >= 40): print("Grade: C")
# elif(percentage <= 69): print("Grade: D")

# table
# m = int(input("Enter initial value\n"))
# n = int(input("Enter final value\n"))

# for i in range(m,n+1):
#     for j in range(1,n+1):
#         print(i*j, end=" ")
#     print() 