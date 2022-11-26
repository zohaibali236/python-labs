# # # # n = int(input("enter no of terms "))
# # # # a = int(input("enter first term "))
# # # # d = int(input("enter common difference "))

# # # # sum = (n/2*(2*a + (n-1)*d))
# # # # print(int(sum))

# # # age_of_sara=23
# # # age_of_mark=19
# # # age_of_fatima=31

# # # avg_age=((age_of_sara + age_of_mark + age_of_fatima)/3)

# # # print(avg_age)

# # # print("The number of times 73 goes into 403 is", int(403/73))

# # # print("the remainder when 403 is divided by 73 is", 403%73)

# # # print(pow(2,10))

# # # height_sara=54
# # # height_mark=57
# # # difference=(height_sara-height_mark)

# # # print(difference, abs(difference))


# # # print(min(34.99,29.95,31.50))

# # # print(2+2 < 4)
# # # print(7//3 == 1+1)
# # # print(pow(3,2)+pow(4,2) == 25)
# # # print(2+4+6 > 12)
# # # print(1387%19 == 0)
# # # print("31 is even?", (31%2==0))
# # # print(min(34.99,29.95,31.50) <30.00)

# # s1='ant'
# # s2='bat'
# # s3='cod'

# # print(s1+' '+s2+' '+s3)
# # print((s1+' ')+(s2+' ')*2+(s3+' ')*3)
# # print(s1+s2+s1+s2+s1+s2+s1+s2+s1+s2+s1+s2+s1+s2+s1+s2+s1+s2+s1+s2)
# # n=int(input())
# # fac = 1
# # for i in range(1, n+1):
# #     fac = fac*i

# # print(fac)

# # def factorialCalculator(n):
# #     x = n
# #     for i in range(n,1,-1):
# #         if i == n:
# #             continue
# #         x=x*i
# #     print(x)

# # factorialCalculator(4)

# def x(n):
    
#     if(n == 1):
#         return n
#     if(n != 1):
#         n = n*x(n-1)
#         # print(n)
#         return n

# print(x(3))

i=0
while(i<5):
    print(i)
    i += 1
    if(i == 3):
        break
else:
    print(0)

    
a = [[96], [69]]

print(list(map(str, a)))
