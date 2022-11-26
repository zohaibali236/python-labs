class Person():
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    def print(self):
        print(self.__firstName + " " + self.__lastName + "\n")


class PersonalInformation(Person):
    def __init__(self, firstName, lastName, age, bday):
        super().__init__(firstName, lastName)
        self.__age = age
        self.__bday = bday

    def print(self):
        super().print()
        print(self.__age + " " + self.__bday)


test = Person("First", "Last")
test.print()

test1 = PersonalInformation("First", "Last", "10", "18 aug 2000")

test1.print()


print(test.__firstName)