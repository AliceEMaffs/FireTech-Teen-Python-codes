# OOP and Classes
# Day 4

# Create a class 'Character'
class Character:
    # These are our 'attributes'
    def __init__(self, name, position, health):
        self.name = name
        self.position = position
        self.health = health
        self.age = 21

    # Using 'def' - we create our 'methods' 
    def how_do_you_feel(self):
        if self.health > 10:
            print("I'm fine thanks!")
        else:
            print("Not so good, I'm afraid.")

    def where_are_you(self):
        print("I'm at {}".format(self.position))

    def how_old_are_you(self):
        print("I am {} year old".format(self.age))

# Instantiate the object 'me'
#me = Character()
# This is creating an instance of the character class,
# which is assigned to the variable (or object) 'me'
# At the moment, there is not any actual information
# about the object 'me', we have just assigned 'memory'
# for the object

# Instantiate = allocating memory to an object of a class
# Initialise = giving 'information' about the object of a class

#me.name = "Alice Matthews"
alice = Character("Alice", (3,4), 50)
# alice is instantiated as the 'self' using __init__ and then when we access the class
# we pass the information to the attricbutes (name and position)
morgan = Character("Name", (5,4), 7)

# Print the object data for alice and morgan
print(alice)
print(alice.name)
print(alice.health)
print(alice.age)
print(alice.how_do_you_feel())
print(morgan)
print(morgan.name)
print(morgan.health)
print(morgan.age)
print(morgan.how_do_you_feel())
