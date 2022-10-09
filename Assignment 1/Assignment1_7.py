def ChkNum(iValue):

    if (iValue % 5 == 0):
        return 1
    else:
        return 0


def main():

    print("Enter a Value : ")
    iNo = input()

    bRet = ChkNum(int(iNo))

    if bRet == 1:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()