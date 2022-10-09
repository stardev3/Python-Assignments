def ChkNum(iValue):

    if iValue == 0:
        print("Zero")
    elif iValue > 0:
        print("Positive Number")
    else:
        print("Negative Number")
        
def main():

    print("Enter a Value : ")
    iNo = input()

    ChkNum(int(iNo))

if __name__ == '__main__':
    main()