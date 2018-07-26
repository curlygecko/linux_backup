class Dog:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print("Woof!  says", self.name)

    def dog(self):
        print("Name: {}\nAge: {}\nWeight: {}".format(self.name, self.age, self.weight))

my_dog = Dog()
my_dog2 = Dog()

my_dog.name = "Lion"
my_dog.age = 3
my_dog.weight = "15 KG"

my_dog2.name = "Lazy"
my_dog2.age = 1
my_dog2.weight = "11 KG"


my_dog.bark()
my_dog2.bark()