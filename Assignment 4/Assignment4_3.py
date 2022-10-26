
ChkRange = lambda iNo : iNo >= 70 and iNo <= 90
Incrmt = lambda iNo : iNo + 10
Mult = lambda iNo1,iNo2 : iNo1 * iNo2
   
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
    iMult = 1
    for No in Data:
        iMult = Helper_Function(iMult,No)
    return iMult

def main():

    print("Enter no of Elements to store in list : ")
    iValue = int(input())

    Data_Input = []

    print("Enter Elemnets : ")

    for i in range(0,iValue):
        Elm = int(input())
        Data_Input.append(Elm)

    print("Original Data : ",Data_Input)

    Data_Filter = list(FilterX(ChkRange,Data_Input))
    print("Data after Filter : ",Data_Filter)

    Data_Map = list(MapX(Incrmt,Data_Filter))
    print("Data after Map : ",Data_Map)

    iRet = ReduceX(Mult,Data_Map)
    print("Output of Reduce : ",iRet)

if __name__ == "__main__":
    main()