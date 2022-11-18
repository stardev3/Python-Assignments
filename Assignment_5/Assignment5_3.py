
class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):

        print("Enter First Number : ")
        self.Value1 = int(input())

        print("Enter Second Number : ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 // self.Value2

def main():

    obj = Arithematic()

    obj.Accept()

    Ret = obj.Addition()
    print("Addition is : ",Ret)

    Ret = obj.Subtraction()
    print("Addition is : ",Ret)

    Ret = obj.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj.Division()
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()