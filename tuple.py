# t = [(2, 3), (4, 7), (8, 11), (3, 6)]

# for i in t:
#     print(f"max and min in {i} are {max(i)} and {min(i)}")


# a = "anachronistically"
# b = "counterintuitive"

# print(f"The number of characters in {a} is {len(a) - len(b)} more than the number of characters in {b}")
# print()


# words = ["misinterpretation", "misrepresentation"]
# if(words[0] < words[1]):
#     print(f"The word {words[0]} appears earlier in the dictionary than the word {words[1]}")

# if "e" not in "floccinaucinihilipilification":
#     print("The letter \"e\" does not appear in the word \"floccinaucinihilipilification\"")

# a = "counterrevolution"
# b = "counter"
# c = "resolution"

# if(len(a) == (len(b) + len(c))):
#     print("The number of characters in the word \"counterrevolution\" is equal to the sum of the number of characters in words \"counter\" and \"resolution\"") 


# def addProvinces(t):
#     t = list(t)
#     while True:
#         n = input("enter name of provinces or type stop to break loop\n")
#         if(n.casefold() == "stop"): break 
#         t.append(n)
#     return tuple(t)

# provinces = tuple()

# print(addProvinces(provinces))

# print()
# print()



# from math import sqrt
# points =[(0,0), (10,10), (6,6), (7,8)]

# centre = (0,0)
# radius = 10

# for i in points:
#     distance = sqrt(pow((i[0]-centre[0]), 2) + pow((i[1] - centre[1]), 2))
#     if(distance < radius):
#         print("the dart is within the board")
#     else:
#         print("the dart missed the board")


# # """TUPLE"""
monthsT = ("Jan", "Feb", "Mar", "May")
print(monthsT)

# monthsT.insert(3, "Apr")
# print(monthsT)

# monthsT.append("Jun")
# print(monthsT)

# monthsT.pop()
# print(monthsT)

# monthsT.remove("Feb")
# print(monthsT)

monthsT.reverse()
print(monthsT)

