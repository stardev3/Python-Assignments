
def Maximum(Arr):
    iMax = Arr[0]
    for no in Arr:
        if(no > iMax):
            iMax = no
    return iMax

def main():

    print("Enter no of Elements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")

    for i in range(0,iValue):
        Elm = int(input())
        Values.append(Elm)

    Ret = Maximum(Values)
    print("Maximum Number : ",Ret)

if __name__ == "__main__":
    main()