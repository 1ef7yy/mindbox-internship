from math import pi, sqrt

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Define the shape!")
    


class Circle(Shape): # класс круга
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2
    

class Triangle(Shape): # класс треугольника
    def __init__(self, sides:list[float]):
        self.sides = sorted(sides)
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

        if self.a + self.b < self.c:
            raise ValueError("Such triangle does not exist")
        

    def calculate_area(self) -> float:
        p = self.sides / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    def is_right(self) -> bool:
        return self.c**2 == self.b**2 + self.a**2
    


class Rectangle(Shape): # класс прямоугольника
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height
    


def calculate_area_all(*args):
    if len(args) == 1:
        return Circle(*args).calculate_area()
    
    elif len(args) == 2:
        return Rectangle(*args).calculate_area()
    
    elif len(args) == 3:
        return Triangle([*args]).calculate_area()
    
    return ValueError("No such shape!")


