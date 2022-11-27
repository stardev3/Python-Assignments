
class Numbers:
    def __init__(self):
        self.No = 0

    def Accept(self):
        print("Enter a Value : ")
        self.No = int(input())

    def ChkPrime(self):
        i = 0
        Flag = True
        for i in range(2, int(self.No / 2) + 1):
            if (self.No % i == 0):
                Flag = False
                break
        return Flag

    def ChkPerfect(self):
        Ans = self.SumFactors()
        if (self.No == Ans):
            return True
        else:
            return False

    def Factors(self):
        print("Factors of given Value are : ")
        for i in range(1, int((self.No / 2) + 1)):
            if (self.No % i == 0):
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1, int((self.No / 2) + 1)):
            if (self.No % i == 0):
                Sum = Sum + i
        return Sum

def main():

    Obj1 = Numbers()
    Obj1.Accept()

    if(Obj1.ChkPrime() == True):
        print("Given Value is a Prime Number")
    else:
        print("Given Value is not a Prime Number")

    if (Obj1.ChkPerfect() == True):
        print("Given Value is a Perfect Number")
    else:
        print("Given Value is not a Perfect Number")

    Obj1.Factors()

    iRet = Obj1.SumFactors()
    print("Summation of all factors of given Value is : ",iRet)
######################################################
    Obj2 = Numbers()
    Obj2.Accept()

    if (Obj2.ChkPrime() == True):
        print("Given Value is a Prime Number")
    else:
        print("Given Value is not a Prime Number")

    if (Obj2.ChkPerfect() == True):
        print("Given Value is a Perfect Number")
    else:
        print("Given Value is not a Perfect Number")

    Obj2.Factors()

    iRet = Obj2.SumFactors()
    print("Summation of all factors of given Value is : ", iRet)

if __name__ == "__main__":
    main()