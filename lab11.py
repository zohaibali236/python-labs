# # """q1"""
# familyTree = {
#     "father": "Jonathan",
#     "mother": "Betty",
#     "brother": "Harry",
#     "sister": "Mary"
# }
# for i,j in familyTree.items():
#     print("%s: %s" %(i,j))
# print()
# familyTree.update({"paternal":{
#     "grandfather": "Dominic",
#     "grandmother": "Daisy",
#     "uncle": "Terry",
#     "aunt": "Gina"
# }})
# familyTree.update({"maternal":{
#     "grandfather": "Larry",
#     "grandmother": "Alison",
#     "uncle": "Bob",
#     "aunt": "Sophia"
# }})
# for i,j in familyTree.items():
#     if(i == "paternal" or i == "maternal"):
#         print("%s:\n" %(i), end="\t\b\b\b")
#         for k,l in familyTree["%s" %(i)].items():
#             print("%s: %s" %(k, l), end="\n\t\b\b\b")
#         print(end="\b\b\b\b\b")
#     else: print("%s: %s" %(i, j))


# # """q2"""
# phone_directory = dict()
# def CreatePhoneDirectory(dict):
#     for _ in range(int(input("How many enteries you would like in the directory\n"))):
#         name = input("Enter name\n")
#         phone_number = input("enter phone number\n")
#         dict[name] = phone_number
# def DeletePhoneDirectoryEntries(dict):
#     while True:
#         name = input("Enter the name of person whose number you want to remove or enter stop to stop removing entries\n")
#         if(name.casefold() == "stop"): break
#         dict.pop(name)
# # CreatePhoneDirectory(phone_directory)
# # for i,j in phone_directory.items():
# #     print("%s: %s" %(i, j))
# # print()
# # print("total entries in phone directory is: %i" %(len(phone_directory)))
# # print()
# # print("Now deleting some entries")
# # DeletePhoneDirectoryEntries(phone_directory)
# # print()
# # for i,j in phone_directory.items():
# #     print("%s: %s" %(i, j)) 
# # print()
# # print("total entries in phone directory is: %i" %(len(phone_directory)))


# # """q3"""

# def hexASCII():
#     for i in range(ord("a"), ord("z")+1):
#         print(f"The ascii and hex code for alphabet \"{chr(i)}\" is {i} and {hex(i)}")

# hexASCII()

# # print()
# # print()
# # print()
# # print()
# # print()
# # print()


# # """q4"""
myDishes = {
    "day1": "Fried Chicken",
    "day2": "Chicken Tenders",
    "day3": "Chicken Nuggets",
    "day4": "Turkey",
    "day5": "Mashed Potatoes",
    "day6": "Meatballs",
    "day7": "Pasta",
}
dishesCooked = {
    "day1": "Fried Chicken",
    "day2": "Chicken Tenders",
    "day3": "Pizza",
    "day4": "Grilled Chicken",
    "day5": "Steak",
    "day6": "Fried Rice",
    "day7": "Pasta",
}
print("foods of my choice are:-", end=" ")
for i in myDishes.values():
    print(i, end=" ")
print()
print("foods cooked this week are:-", end=" ")
for i in dishesCooked.values():
    print(i, end=" ")
ListDishCoocked = list()
ListMyDishes = list()
for i in dishesCooked.values():
    ListDishCoocked.append(i)
for i in myDishes.values():
    ListMyDishes.append(i)
print()
print("food of my choices coocked this week are")
for i in range(len(ListMyDishes)):
    if(ListMyDishes[i] == ListDishCoocked[i]): print(ListMyDishes[i])

"""q5"""
def totalGuestsInvited(l1, l2):
    l1, l2 = set(l1), set(l2)

    return len(l1.union(l2))
def commonGuestsInvited(l1,l2):
    l1, l2 = set(l1), set(l2)

    commonGuests = l1.intersection(l2)
    return commonGuests, len(commonGuests)
myList = ["Charlie Ruiz", "Carson Ramos", "Reagan Campbell", "Tyler Butler", "Gwendolyn Lindsey", "Vera Lindsey"]
parentsList = ["Finn Thompson", "Carson Ramos", "Brianna Stewart", "Tyler Butler", 
 "Leon Allen", "Vera Lindsey", "London Martin", "Luca Morales", "Samantha Clark", 
 "Adonis Briggs", "Orion Newman", "Micah Gray"]
print("Guests invited by me are:", ", ".join(myList))
print()
print("guests invited by my parents are", ", ".join(parentsList))
print()
print(commonGuestsInvited(myList, parentsList)[1], "guests are common in our lists and their names are:", ", ".join(commonGuestsInvited(myList, parentsList)[0]))
print()
print("Total number of guests arrived are", totalGuestsInvited(myList, parentsList))