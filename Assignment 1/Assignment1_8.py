
def Display(iValue):

    i = 0;

    for i in range(0,iValue):
        print(" * ",end="")


def main():

    print("Enter a Value : ")
    iNo = input()

    Display(int(iNo))

if __name__ == '__main__':
    main()