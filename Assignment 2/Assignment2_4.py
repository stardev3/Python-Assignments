
def AddFactors(iNo):

    iSum = 0
    
    for i in range(1,iNo):
        if(iNo % i == 0):
            iSum = iSum + i

    return iSum

def main():

    print("Enter a Number : ")
    iValue = input()

    iRet = AddFactors(int(iValue))
    print("Addition of Factors is : ",iRet)

if __name__ == '__main__':
    main()