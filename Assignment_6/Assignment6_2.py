
class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Accept(self):
        print("Enter Name : ")
        self.Name = input()
        print("Enter Initial Amount : ")
        self.Amount = int(input())

    def Display(self):
        print("Name of Account Holder : ",self.Name)
        print("Total Amount in Bank : ",self.Amount)
        print("Total Intrest on Bank Amount : ",self.TotalIntrest)

    def Deposit(self):
        print("Enter Amount you want to Deposit : ")
        self.Amount = self.Amount + int(input())

    def Withdraw(self):
        print("Enter Amount you want to Withdraw : ")
        self.Amount = self.Amount - int(input())

    def CalculateIntrest(self):
        self.TotalIntrest = ((self.Amount*BankAccount.ROI)/100)

def main():

    Obj1 = BankAccount()
    Obj1.Accept()
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.CalculateIntrest()
    Obj1.Display()

    Obj2 = BankAccount()
    Obj2.Accept()
    Obj2.Deposit()
    Obj2.Withdraw()
    Obj2.CalculateIntrest()
    Obj2.Display()

if __name__ == "__main__":
    main()