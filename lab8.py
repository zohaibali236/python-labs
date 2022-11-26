from datetime import datetime

time = datetime(2018, 7, 13, 21, 40)

print(time.strftime("%A, %B %d %Y"))
print(time.strftime("%I:%M %p Central Daylight Time on %m/%d/%Y"))
print(time.strftime("I will meet you on %a %B %d at %I:%M %p"))


print()
#q 2

forecast = "It will be a sunny day today"

count = forecast.count("day")
print("The word \"day\" occurred", count, "times")

weather = forecast.index("sunny")
print("The word sunny starts at index", weather)

change = forecast.replace("sunny", "cloudy")
print(change)

print()
#q 3
def even(n):
    for i in range(2, n+1):
        if((i % 2 == 0) or (i % 3 == 0)):
            print(i, end = " ")

even(17)

print()
print()


#q 4

first = "John"
last = "Doe"
street = "Main Street"
number = 123
city = "AnyCity"
state = "AS"
zipcode = "09876"


print(f"{first} {last}\n{number} {street}\n{city}, {state} {zipcode}")


#q 5
message = "The secret of this message is that it is secret"

length = len(message)
print("The length of message is", length)

count = message.count("secret")
print("The number of times the word \"secret\" occured is", count)

censored = message.replace("secret", "xxxxxx")
print("The censored message is:", censored)

#q6
def month(n):
    return (("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())[n-1])

print(month(7))

print()
# q 7
def cheer(string):

    string_spaced = " ".join(list(string.upper()))

    print(f"How do you spell winner?\nI know, I know!\n{string_spaced} !\nAnd that's how you spell winner!\nGo {string.title()}!")

cheer("nedians")