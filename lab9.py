# """q1"""
# best_students = set()

# print("Enter your 5 best students")

# for _ in range(5):
#     best_students.update([input()])

# print(best_students)

# """q2"""
# print("Enter the name of your friends who left NED")

# for _ in range(2):
#     best_students.discard(input())

# print(best_students)

# """q3"""
# best_dishes = set()

# print("Enter your favorite dishes one by one or enter stop to quit entering dishes")

# while True:
#     dish_name = input()
#     if(dish_name == "stop"): break
#     else: best_dishes.update([dish_name])

# print(best_dishes)

# print("After popping")
# for _ in range(len(best_dishes)):
#     best_dishes.pop()

# print(best_dishes)

"""q4"""
items = {"apples", "mangoes", "grapes"}
items_Prices = dict()
for _ in range(len(items)):
    poppedItem = items.pop()
    items_Prices[poppedItem] = int(input("Enter price for %s\n" %(poppedItem)))

print(items_Prices)

print("total price of items =", sum(items_Prices.values()))
print(f"maximum and minimum prices are {max(items_Prices.values())} and {min(items_Prices.values())}")


"""q5"""

U = {i for i in range(1,41)} #All
print(U)

A = {i for i in range(1,11)} #play both
print(A)

B = {i for i in range(1, 22)} #play hockey only
print(B)


C = B.difference(A)
print(C)
print((U.difference(C)).difference(A))


"""q6"""
dogProductOnly = 83
print("purchases for dog only are", dogProductOnly)

catProductOnly = 101
print("purchases for cat only are", catProductOnly)

dogOrFish = 83 + 22
print("purchases for dog or fish are", dogOrFish)


totalPurchases = 83+101+22+31+8+10+6+34
print("total purchases are", totalPurchases)

#q7

no_of_students = 110
pure_english = 25
eng_french = 17
eng_spanish = 20
eng_french_spanish = 13
pure_spanish = 10
spanish_french = 9
pure_french = 11

#a
eng_spanish_notFrench = 55
print("Students speaking english but not french:", eng_spanish_notFrench)
#b
neither = no_of_students - (pure_english+eng_french+eng_spanish+eng_french_spanish+pure_spanish+spanish_french+pure_french)
print("Students speaking neither of the languages:", neither)

#c
french_not_eng_spanish = 11
print("Students speaking french but not english and spanish:", french_not_eng_spanish)

#d
only_one_of_lang = pure_french + pure_english + pure_spanish
print("Students speaking only one language:", only_one_of_lang)

#e
two_lang = eng_french + spanish_french + eng_spanish
print("Students speaking only two languages:", two_lang)
