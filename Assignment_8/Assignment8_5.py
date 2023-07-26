
def Fact(No):
    if (No <= 0):
        return 1
    else:
        return (No * Fact(No - 1))


def main():

    Value = int(input("Enter a Number : "))
    Ret = Fact(Value)
    print("Factorial of given Number is : ",Ret)

if __name__ == "__main__":
    main()