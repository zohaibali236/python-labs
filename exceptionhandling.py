# l1 = [1,2,3,4,5]
# l2 = [1,2,0,4,0]

# for i in range(len(l1)):
#     try:
#         print(l1[i]/l2[i])
#     except ArithmeticError as e:
#         print(e)

# l = [1,2]
# try:
#     print(l[2])
# except IndexError as e:
#     print(e)

# try:
#     n=input()
#     print(n)
# except EOFError as e:
#     print(e)
# else:
#     print(1)

try:
    fopen = open("file.txt")
except IOError as e:
    print(e)
else:
    print("no error")