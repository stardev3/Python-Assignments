
def Display(iValue):

    i = 0

    while i < iValue:
        print("Marvellous")
        i = i + 1

def main():

    print("Enter Number : ")
    iNo = input()

    Display(int(iNo))

if __name__ == '__main__':
    main()