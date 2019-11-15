# Animal class

class Animal:
    
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def what_species_are_you(self):

        if self.species == "Cat":
            print("MEOW! I'm a cat!")
        elif self.species == "Dog":
            print("WOOF! I'm a doggy!")
        else:
            print("I'm not a cat or a dog!")


# make objects for class animals

cat = Animal("Pipa", 9, "Cat")
dog = Animal("Poppy", 5, "Dog")

print(cat.name)
cat.what_species_are_you()

print(dog.name)
dog.what_species_are_you()


