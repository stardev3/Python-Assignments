
MultFunc = lambda iNo1,iNo2 : iNo1 * iNo2

def main():

    print("Enter First Number : ")
    iValue1 = int(input())

    print("Enter Second Number : ")
    iValue2 = int(input())

    iRet = MultFunc(iValue1,iValue2)
    print("Multiplication : ",iRet)

if __name__== "__main__":
    main()