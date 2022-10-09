
def AddDigits(iNo):

    iSum = 0

    while iNo != 0:
        iSum = iSum + (iNo % 10)
        iNo = iNo//10

    return iSum

def main():

    print("Enter a Number : ")
    iValue = input()

    iRet = AddDigits(int(iValue))
    print("Addition of Digits is : ",iRet)

if __name__ == '__main__':
    main()