
def Add(Arr):
    iSum = 0
    for no in Arr:
        iSum = iSum + no

    return iSum

def main():

    print("Enter no of ELements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")
    
    for i in range(0,iValue):
        Elm = int(input())
        Values.append(Elm)

    Ret = Add(Values)
    print("Addition of all Elements is : ",Ret)

if __name__ == "__main__":
    main()