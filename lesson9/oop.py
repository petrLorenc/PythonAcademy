class Animal:
    encapsulated_variable = "Animal"
    position_X = 0.
    position_Y = 0.

    def __init__(self, name):
        self.name = name


    def make_sound(self):
        pass

    def go_up(self):
        print("Moving")
        self.position_Y += 1.

    def __str__(self):
        return f"I am {self.name} and my position is {self.position_X}:{self.position_Y}"

class Dog(Animal):
    encapsulated_variable = "Animal"

    def __init__(self, name=None):
        super(Dog, self).__init__(name=name or "Dog")

    def make_sound(self):
        print(f"{self.name} is making: Haf")

    def go_up(self):
        super(Dog, self).go_up()
        super(Dog, self).go_up()


class Cat(Animal):
    encapsulated_variable = "Cat"

    def __init__(self, name="Cat"):
        super(Cat, self).__init__(name)

    def make_sound(self):
        print(f"{self.name} is making: Mnau")

    def go_up(self):
        self.position_Y += 1.5


class Tiger(Animal):
    pass

pets = [Dog("Alik"), Cat("Linda"), Cat("Tapka"), Tiger("Tiger")]

for pet in pets:
    print(type(pet) is Cat)

    # print(pet is Dog("Alik"))
    # print(pet.encapsulated_variable)
    # pet.go_up()
    # pet.make_sound()
    # print(pet)
    # print()