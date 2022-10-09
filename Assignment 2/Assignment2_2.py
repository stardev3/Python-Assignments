
def Display(iNo):

    for i in range(iNo):
        for j in range(iNo):
            print(" * ",end = "")
        print()

def main():

    print("Enter a Number : ")
    iValue = input()

    Display(int(iValue))

if __name__ == '__main__':
    main()