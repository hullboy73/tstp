class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

class Square(Shape):

    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, n):
        self.s1 += n

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name
        
jockey = Rider("Sam Twiston-Davies")
horse = Horse("Hitched", jockey)
print("The name of horse is: {}".format(horse.name))
print("The name of rider is: {}".format(horse.rider.name)) 

##a_rectangle = Rectangle(20,10)
##a_square = Square(10,10)
##print(a_rectangle.calculate_perimeter())
##print(a_square.calculate_perimeter())
##a_square.change_size(-3)
##print(a_square.calculate_perimeter())

a_square = Square(10)
a_rectangle = Rectangle(20,10)
a_square.what_am_i()
a_rectangle.what_am_i()
