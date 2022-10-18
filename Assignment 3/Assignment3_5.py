import MarvellousNum

def ListPrime(Arr):
    iSum = 0
    for no in Arr:
        if(MarvellousNum.ChkPrime(no) == True):
            iSum = iSum + no
    return iSum

def main():

    print("Enter no of Elements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")

    for i in range(0,iValue):
        Elm = int(input())
        Values.append(Elm)

    Ret = ListPrime(Values)
    print("Addition of all Prime Numbers is : ",Ret)

if __name__ == "__main__":
    main()