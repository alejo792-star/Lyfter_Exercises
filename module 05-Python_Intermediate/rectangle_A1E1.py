def get_information(text):
        while True:
            try:
                number = float(input(text))
                
                if number>= 0:
                    return number
                else:
                    print("no negative numbers")
            except ValueError as f:
                print(F"ValueError: {f}")
class Rectangle:
    def __init__(self,width,height):
        if width <0 or height <0:
            raise ValueError("can't be negative ")
        self.width = width
        self.heigth = height
                
            

    def get_area(self):
        area = self.width * self.heigth
        return area

    def get_perimeter(self):
        perimeter = 2 *(self.width + self.heigth)
        return perimeter


def main ():
    width = get_information("Give a width: ")
    heigth = get_information("Give a Heigth")
    rectangle= Rectangle(width,heigth)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    
if __name__ == "__main__":
    main()
