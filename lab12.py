import random

cities = [
    "Karachi","Lahore","Faisalabad",
    "Rawalpindi","Gujranwala","Peshawar","Multan",
    ]

print(cities)

random.shuffle(cities)
print("After shuffling")
print(cities)



students = [
    "Ali",
    "Arham",
    "Bilal",
    "Sanaullah"
]
print(students)

for _ in range(3):
    print(".")

newList = list()
for _ in range(len(students)):
    newList.append(students.pop())

print(newList)
for _ in range(3):
    print(".")

scholarship = random.sample(newList, 2)
print(f"Congratulation {scholarship[0]} and {scholarship[1]} got the scholarship")




dice1 = [_ for _ in range(1,7)]
dice2 = [_ for _ in range(1,7)]

print("Rolling the dice")
print(f"dice for player 1 rolled the number: {random.choice(dice1)}\ndice for player 2 rolled the number: {random.choice(dice2)}")
print()

while True:
    str = input("Enter reroll to roll the dices again or enter stop to stop ").casefold()
    if(str == "reroll".casefold()):
        print("Rolling the dice")
        print(f"dice player 1 rolled the number: {random.choice(dice1)}\ndice player 2 rolled the number: {random.choice(dice2)}")
        print()
    else: break