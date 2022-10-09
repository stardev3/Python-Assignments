
def Display(iNo):

    for i in range(iNo,0,-1):
        for j in range(0,i):
            print(" * ",end="")

        print()

def main():

    print("Enter a Number : ")
    iValue = input()

    Display(int(iValue))

if __name__ == '__main__':
    main()