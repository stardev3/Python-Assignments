
def ChkPrime(iNo):
    for i in range(2,int(iNo/2)+1):
        if (iNo % i == 0):
            return False
            break;
    else:
        return True

Doubles = lambda iNo : iNo * 2

def Maximum(iNo1,iNo2):
     if(iNo1 > iNo2):
         return iNo1
     else:
         return iNo2

def FilterX(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    return Result

def MapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result

def ReduceX(Helper_Function,Data):
    iMax = Data[0]
    for No in Data:
        iMax = Maximum(iMax,No)
    return iMax

def main():

    print("Enter no of Elements to store in list : ")
    iValue = int(input())

    Data_Input = []

    print("Enter Elemnets : ")

    for i in range(0,iValue):
        Elm = int(input())
        Data_Input.append(Elm)

    print("Original Data : ",Data_Input)

    Data_Filter = list(FilterX(ChkPrime,Data_Input))
    print("Data after Filter : ",Data_Filter)

    Data_Map = list(MapX(Doubles,Data_Filter))
    print("Data after Map : ",Data_Map)

    iRet = ReduceX(Maximum,Data_Map)
    print("Output of Reduce : ",iRet)

if __name__ == "__main__":
    main()