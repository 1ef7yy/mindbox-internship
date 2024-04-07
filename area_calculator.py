import math

class AreaCalculator:
    def calculate_circle_area(self, radius: float) -> float:
        return math.pi * radius ** 2
    
    def calculate_triangle_area(self, sides: list[float]) -> float:
        p = sum(sides) / 2
        return math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))
    
