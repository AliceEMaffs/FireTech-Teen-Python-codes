# Class Heirachy : Base classes and sub classes

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

    def speak(self):
        print("Nothing useful here!")
        
