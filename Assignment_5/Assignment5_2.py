
class Circle:

    PIValue = 3.14

    def __init__(self):
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0

    def Accept(self):
        print("Enter Radius of the Circle : ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PIValue * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PIValue * self.Radius
        
    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)

def main():

    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()