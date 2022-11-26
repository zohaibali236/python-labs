def isleap(y):
    return ( y % 4==0 and (y % 100 != 0 or y % 400 == 0))

month = input("Enter the name of month\n")
date = int(input("Enter the date\n"))

if(date <= 0): print("Invalid date")

year = int(input("Enter the year\n"))

month == month.casefold()

if(date <= 0): print("Invalid date")

if(month in "january"):
    if(date > 31): print("Invalid date for month \"January\"")
    else:
        print("The season is \"Winter\"")
    
elif(month in "february"):
    if(isleap(year)):
        if(date > 29): print("Invalid date for month \"February\"")
        else: print("The season is \"Winter\"")
    else:
        if(date > 28): print("The year is not a leap year so date cannot be above than 28")
        else: print("The season is \"Winter\"")

elif(month in "march" or month in "may"):
    if(date > 31): print(f"Invalid date for month \"{month}\"")
    else: print("The season is \"Spring\"")

elif(month in "april"):
    if(date > 30): print("Invalid date for month \"April\"")
    else: print("The season is \"Spring\"")

elif(month in "june"):
    if(date > 30): print("Invalid date for month \"June\"")
    else: print("The season is \"Summer\"")

elif(month in "july"):
    if(date > 31): print("Invalid date for month \"July\"")
    else: print("The season is \"Summer\"")

elif(month in "August"):
    if(date > 31): print("Invalid date for month \"July\"")
    else: print("The season is \"Summer\"")

elif(month in "september"):
    if(date > 30): print("Invalid date for month \"September\"")
    else: print("The season is \"Autumn\"")

elif(month in "october"):
    if(date > 31): print("Invalid date for month \"October\"")
    else: print("The season is \"Autumn\"")

elif(month in "november"):
    if(date > 30): print("Invalid date for month \"November\"")
    else: print("The season is \"Autumn\"") 

elif(month in "december"):
    if(date > 31): print("Invalid date for month \"December\"")
    else: print("The season is \"Winter\"")

else: print("Error")


def digitSplitter(a):
    firstDigit = (a//1000)
    secondDigit = (a//100 - (firstDigit)*10)
    thirdDigit = (a//10 - (a//100)*10)
    fourthDigit = (a - (a//10)*10)

    print(f"{firstDigit}\n{secondDigit}\n{thirdDigit}\n{fourthDigit}")

numbers = input("Enter Four digit number (e.g 1234) ")
if(len(numbers) != 4 or numbers[0] == '0'): print("Error")
else: digitSplitter(int(numbers))

students_list = (input("Enter the names of students separated by spaces\n").title()).split()

print("The names of students that starts with \"A\" through \"M\" are")
for i in students_list:
    for j in i[0]:
        if(ord(j) >=65 and ord(j) <= 77):
            print(i)



# for i in range(11, 42, 5):
#     print(i, end=" ")

# print()

# for j in range(3, 34, 5):
#     print(j, end=" ")
# print()

# for i in range (20, 10, -3):
#     for j in range(2):
#         if(j==1 and i == 11): break
#         print(i, end = " ")

# def xmult(a, b):
#     c = []
#     for i in a:
#         for j in b:
#             c.append(i*j)
#     return c
# print(xmult([2,3], [3,4]))

# for i in range(9):
#     for j in range(i+1):
#         print(i+1, end="")
#     print(end="\n")
# print()

# for i in range (3,0,-1):
#     for j in range(i):
#         print(j+1, end="")
#     print(end="\n")




# def increment(salary, grade):
#     if(grade >= 1 and grade <= 14):
#         increment_percent = 20/100
#         print(f"The increase in salary will be {salary*increment_percent:0.2f} and the new salary will be \
# {(salary + salary*increment_percent):0.2f}")

#     elif(grade >= 15 and grade <= 19):
#         increment_percent= 10/100
#         print(f"The increase in salary will be {salary*increment_percent:0.2f} and the new salary will be \
# {(salary + salary*increment_percent):0.2f}")

#     elif(grade >= 20 and grade <= 22):
#         increment_percent= 5/100
#         print(f"The increase in salary will be {salary*increment_percent:0.2f} and the new salary will be \
# {(salary + salary*increment_percent):0.2f}")
    
#     else: print("Invalid grade")

# salary = float(input("Enter the salary of employee\n"))

# grade = int(input("Enter the grade of employee\n"))

# increment(salary, grade)
