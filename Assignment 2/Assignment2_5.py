
def ChkPrime(iNo):

    for i in range(2,iNo):
        if(iNo % i == 0):
            print("It is not a Prime Number!")
            break;
    else:
        print("It is a Prime Number!")

def main():

    print("Enter a Number : ")
    iValue = input()

    ChkPrime(int(iValue))

if __name__ == '__main__':
    main()