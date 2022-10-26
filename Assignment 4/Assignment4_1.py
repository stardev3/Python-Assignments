
PwrFunc = lambda iNo : iNo * iNo

def main():

    print("Enter Number : ")
    iValue = int(input())

    iRet = PwrFunc(iValue)
    print("Power of two of given no is : ",iRet)

if __name__ == "__main__":
    main()