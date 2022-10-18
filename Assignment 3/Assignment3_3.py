
def Minimum(Arr):
    iMin = Arr[0]
    for no in Arr:
        if(no < iMin):
            iMin = no
    return iMin

def main():

    print("Enter no of Elements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")

    for i in range(0,iValue):
        Elm = int(input())
        Values.append(Elm)

    Ret = Minimum(Values)
    print("Minimum Number : ",Ret)

if __name__ == "__main__":
    main()