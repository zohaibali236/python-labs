"""TASK NO 1"""

l = [2, 1, 3, 5, 4, 3, 8]

l.sort()
print(l)

l.insert(0,0)
print(l)

print(l.pop())
print(l)

l.pop(1)
print(l)

print(l.count(3))

print(l.index(2))

l.append(23)
l.append([1,2,3])
print(l)

l.remove(23)
print(l)

l1 = [99,88,55]
l.extend(l1)
print(l)


"""TASK NO 2"""
from math import pi
from math import sin

angles = (75, 0, 45, 80)
lengths = (16, 20, 24, 24)

for i in range(len(angles)):

    angle_in_radian = (pi*angles[i])/180
    height = lengths[i]*sin(angle_in_radian)

    print(f"The height reached by ladder will be {height:.03f} when angle is {angle_in_radian:.03f} and length of ladder is {lengths[i]}")


"""TASK NO 2"""

# from math import pi
# from math import sin

# length = int(input("Enter the length of ladder(in feets)\n"))
# angle = int(input("Enter angle formed between ladder and wall(in degrees)\n"))

# if(angle == 90): print("The ladder will fall over if the angle is 90°")
# else:
#     angle = (pi*angle)/180
#     height = length * sin(angle)
    
#     print(f"The height reached by ladder will be {height:.03f} when angle is {angle:.03f} and length of ladder is {length}")

"""TASK NO 3"""
from math import ceil

lst = [i for i in range(1,12)]
print(lst)

if(len(lst) % 2 == 0):
    middle_term_1 = ((len(lst)//2) -1)
    middle_term_2 = (((len(lst) + 2)//2) -1)

    print(f"index of first middle term: {middle_term_1}\nindex second middle term: {middle_term_2}")
   
    print(f"element of first middle term: {lst[middle_term_1]}\nelement of second middle term: {lst[middle_term_2]}")
else:
    middle_term = (ceil(len(lst)/2) -1)
    print(f"index of middle term: {middle_term}")
   
    print(f"element of middle term: {lst[middle_term]}")

lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

for _ in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        if(lst[i] < lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)


"""TASK NO 4"""
monthsL = ["Jan", "Feb", "Mar", "May"]
print(monthsL)

monthsL.insert(3, "Apr")
print(monthsL)

monthsL.append("Jun")
print(monthsL)

monthsL.reverse()
print(monthsL)

monthsL.sort()
print(monthsL)

monthsL.pop()
print(monthsL)

monthsL.remove("Feb")
print(monthsL)

# """TUPLE"""
# monthsT = ("Jan", "Feb", "Mar", "May")
# print(monthsT)

# monthsT.insert(3, "Apr")
# print(monthsT)

# monthsT.append("Jun")
# print(monthsT)

# monthsT.reverse()
# print(monthsT)

# monthsT.sort()
# print(monthsT)

# monthsT.pop()
# print(monthsL)

# monthsT.remove("Feb")
# print(monthsL)


"""TASK NO 5"""
a, b = 6, 7
print("a =", a, "b =", b)

c = (a+b)/2
print("avg of a and b =", c)

inventory = ['paper', 'staples', 'pencils']
print(inventory)

first, middle, john = 'Jonh', 'Fitzgerald', 'Kennedy'
print(first, middle, john)

fullname = first + " " + middle + " " + john
print(fullname)

