
def Display(iNo):

    for i in range(1,iNo+1):
        for j in range(1,iNo+1):
            print(" ",j," ",end="")
        print()

def main():

    print("Enter a Number : ")
    iValue = input()

    Display(int(iValue))

if __name__ == '__main__':
    main()