class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
        
class Square(Shape):
    def __init__(self, s1):
        self.side = s1
    def calculate_perimeter(self):
        return 4 * self.side        


square = Square(5)
rectangle = Rectangle(2,4)

print(square.calculate_perimeter())
print(rectangle.calculate_perimeter())

square.what_am_i()
rectangle.what_am_i()

class Square2():
    square_list=[]
    def __init__(self, s1):
        self.side = s1
        self.square_list.append(self.side)
    def calculate_perimeter(self):
        return 4 * self.side
