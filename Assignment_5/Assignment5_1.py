
class Demo:

    Value = 0
    
    def __init__(self,A,B):
        self.iValue1 = A
        self.iValue2 = B

    def Fun(self):
        print("Displaying Values from Fun : ")
        print("Value1 : ",self.iValue1)
        print("Value2 : ",self.iValue2)

    def Gun(self):
        print("Displaying Values from Gun : ")
        print("Value1 : ",self.iValue1)
        print("Value2 : ",self.iValue2)

def main():

    print("Enter First Number : ")
    iNo1 = int(input())

    print("Enter Second Number : ")
    iNo2 = int(input())

    obj = Demo(iNo1,iNo2)
    obj.Fun()
    obj.Gun()

    obj1 = Demo(11,21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()

    