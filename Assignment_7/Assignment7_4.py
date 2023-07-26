import  threading

def SmallCnt(Str):
    Cnt = 0
    for s in Str:
        if(s >= 'a' and s <= 'z'):
            Cnt = Cnt + 1
    print("Small Characters : ",Cnt)

def CapitalCnt(Str):
    Cnt = 0
    for s in Str:
        if (s >= 'A' and s <= 'Z'):
            Cnt = Cnt + 1
    print("Capital Characters : ",Cnt)

def DigitsCnt(Str):
    Cnt = 0
    for s in Str:
        if (s >= '0' and s <= '9'):
            Cnt = Cnt + 1
    print("Digits : ",Cnt)

def main():
    print("Enter String : ")
    Data = input()

    Small = threading.Thread(target = SmallCnt,args = (Data,))
    Capital = threading.Thread(target = CapitalCnt,args = (Data,))
    Digits = threading.Thread(target = DigitsCnt,args = (Data,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("ID of Thread(Small) is : ",id(t1))
    print("ID of Thread(Capital) is : ",id(t2))
    print("ID of Thread(Digits) is : ",id(t3))

if __name__ == "__main__":
    main()