
def Frequency(Arr,iNo):
    iCnt = 0
    for no in Arr:
        if(no == iNo):
            iCnt = iCnt + 1
    return iCnt

def main():

    print("Enter no of Elements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")

    for i in range(0,iValue):
        Elm = int(input())
        Values.append(Elm)

    print("Enter Element to search : ")
    iSearch = int(input())

    Ret = Frequency(Values,iSearch)
    print("Frequency of given Element : ",Ret)

if __name__ == "__main__":
    main()