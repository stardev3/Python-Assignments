
def Summation(No):
    if(No < 10):
        return No
    else:
        return (No % 10) + Summation(No//10)

def main():
    print("Enter a Number : ")
    Value = int(input())

    Ret = Summation(Value)
    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()