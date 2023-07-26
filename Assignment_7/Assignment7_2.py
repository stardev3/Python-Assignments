import threading

def EvnFact(No):
    iSum = 0
    for i in range(1,No):
        if (No % i == 0):
            if(i % 2 == 0):
                iSum = iSum + i
    print("Addition of Even Factors : ",iSum)

def OddFact(No):
    iSum = 0
    for i in range(1,No):
        if (No % i == 0):
            if(i % 2 != 0):
                iSum = iSum + i
    print("Addition of Odd Factors : ",iSum)

def main():

    print("Enter Number : ")
    iValue = int(input())

    EvenFactors = threading.Thread(target = EvnFact,args = (iValue,))
    OddFactors = threading.Thread(target = OddFact,args = (iValue,))

    EvenFactors.start()
    OddFactors.start()

    EvenFactors.join()
    OddFactors.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()