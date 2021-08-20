# Question: Define a class, which have a class parameter and have a same instance parameter.
class Human:
    name = "Darren"

    def __init__(self, name=None):
        self.name = name


itadori = Human("itadori")
print(Human.name, itadori.name)
