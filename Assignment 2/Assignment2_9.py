
def CntDigits(iNo):

    iCnt = 0;

    while iNo != 0:
        iCnt = iCnt + 1
        iNo = iNo//10

    return iCnt

def main():

    print("Enter a Number : ")
    iValue = input()

    iRet = CntDigits(int(iValue))
    print("Number of digits in given number is : ",iRet)

if __name__ == '__main__':
    main()