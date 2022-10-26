
ChkEven = lambda iNo : (iNo % 2 == 0)
Square = lambda iNo : iNo * iNo
Sum = lambda iNo1,iNo2 : iNo1 + iNo2

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
    iSum = 0
    for No in Data:
        iSum = Helper_Function(iSum,No)
    return iSum

def main():

    print("Enter no of Elements to store in list : ")
    iValue = int(input())

    Data_Input = []

    print("Enter Elemnets : ")

    for i in range(0,iValue):
        Elm = int(input())
        Data_Input.append(Elm)

    print("Original Data : ",Data_Input)

    Data_Filter = list(FilterX(ChkEven,Data_Input))
    print("Data after Filter : ",Data_Filter)

    Data_Map = list(MapX(Square,Data_Filter))
    print("Data after Map : ",Data_Map)

    iRet = ReduceX(Sum,Data_Map)
    print("Output of Reduce : ",iRet)

if __name__ == "__main__":
    main()