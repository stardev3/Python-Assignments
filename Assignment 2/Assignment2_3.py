
def Factorial(iNo):

    Ans = 1

    for i in range(1,iNo + 1):
        Ans = Ans * i

    return Ans

def main():

    print("Enter a Number : ")
    iValue = input()

    iRet = Factorial(int(iValue))
    print("Factorial is : ",iRet)

if __name__ == '__main__':
    main()