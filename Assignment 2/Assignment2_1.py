
import Arithematic

def main():

    print("Enter First Value : ")
    iNo1 = int(input())

    print("Enter Second Value : ")
    iNo2 = int(input())

    iAdd = Arithematic.Add(iNo1,iNo2)
    print("Addition is : ",iAdd)

    iSub = Arithematic.Sub(iNo1,iNo2)
    print("Substraction is : ",iSub)

    iMult = Arithematic.Mult(iNo1,iNo2)
    print("Multiplication is : ",iMult)

    iDiv = Arithematic.Div(iNo1,iNo2)
    print("Division is : ",iDiv)

if __name__ == '__main__':
    main()