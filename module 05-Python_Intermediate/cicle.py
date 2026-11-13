# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.
import math
class Circle:
    def __init__(self,radius):
        if radius < 0:
            raise ValueError("the radius can't be negative")
        self.radius = radius

    
    def get_area(self):
        area =  math.pi*self.radius**2
        return area

def main():
    try:
        radius = float(input("Enter a radius: "))
        circle = Circle(radius)
        circle_2 = Circle(2)
        circle_3 = Circle(5)
        print(f"the area is : {circle.get_area()}")
        print(f"the area is : {circle_2.get_area()}")
        print(f"the area is : {circle_3.get_area()}")
        
    except ValueError as f:
        print(f"We can't calculate: {f}")

if __name__ == "__main__":
    main()


