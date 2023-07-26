import threading

def EvenSum(Data):
    iSum = 0
    for No in Data:
        if(No % 2 == 0):
            iSum = iSum + No
    print("Addition of Even Elements in List : ",iSum)

def OddSum(Data):
    iSum = 0
    for No in Data:
        if (No % 2 != 0):
            iSum = iSum + No
    print("Addition of Odd Elements in List : ",iSum)

def main():
    print("Enter no of ELements to store : ")
    iValue = int(input())

    Values = []

    print("Enter Elements : ")

    for i in range(0, iValue):
        Elm = int(input())
        Values.append(Elm)

    EvenList = threading.Thread(target = EvenSum,args = (Values,))
    OddList = threading.Thread(target = OddSum,args = (Values,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()