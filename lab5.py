# odd no
i = 1
while(i<100):
    if(i == 1):
        i+=2
        continue
    print(i, end = " ")
    i += 2
print("\n")
#factorial

# def calculteFactorial(n):
#     r = 1
#     for i in range(1,n+1):
#         r *= i
#     return r

# k = 1

# while(k <= 10):
#     print("factorial of", k, "is", calculteFactorial(k))
#     k+=1
# print("\n")
#shapes
i = 0
while(i < 8):
    j = 0
    if(i >= 4): print("\t\t", end="")
    while(j < 14):
        print("*", end="")
        j += 1
    print()
    i += 1
    
print()
# i = 0
# while(i < 4):
#     j = 0
#     # if(i == 0): print("  ", end="")
#     # # if(i == 1): print("  ", end="")
#     # if(i == 2): print(" ", end="")
   
#     while(j < 14):
#         print("*", end="")
#         j += 1
#     print()
#     i += 1
# print("\n")
i = 0
while(i < 8):
    j = 0
    while(j <= i):
        print("*", end="")
        j += 1
    print()
    i += 1
    
print()
i = 8
while(i >= 0):
    j = 0
    while(j < i):
        print("*", end="")
        j += 1
    print()
    i -= 1
