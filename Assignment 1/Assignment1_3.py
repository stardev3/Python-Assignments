def Add(iValue1,iValue2):

    iAdd = iValue1 + iValue2
    return iAdd


def main():

    print("Enter First Number : ")
    iNo1 = input()

    print("Enter Second number : ")
    iNo2 = input()

    iRet = Add(int(iNo1),int(iNo2))
    print("Addition is : ",iRet)

if __name__ == '__main__':
    main()
