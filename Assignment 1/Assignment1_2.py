def ChkNum(iValue):

    if(iValue % 2 == 0):
        print("Even Nummber")
    else:
        print("Odd Number")


def main():

    print("Enter a Value : ")
    iNo = int(input())

    ChkNum(iNo)

if __name__ == '__main__':
    main()