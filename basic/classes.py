class Point:
    def hold(self):
        print('move')

    def draw(self):
        print('draw')


std = Point()
std.hold() # ans: move
std.draw() # ans: draw

# add attribute to class
std.up = 'up'
std.down = 'down'
print(std.up)
print(std.down)
# this up and down attribute is set for std variable. if we want to 
# get this attribute by different variable, it will give error
# std2 = Point()
# print(std2.up)

                        # Constructors
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y


chair = Room(10, 20)
print(chair.x)

                        # Inheritance
class Mammal:
    def sound(self):
        print("hey")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


dog = Dog()
dog.sound()
dog.bark()

