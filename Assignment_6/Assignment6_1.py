
class BookStore:

    NoOfBooks = 0

    def __init__(self):
        self.Name = ""
        self.Author = ""
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Accept(self):
        print("Enter Name of a Book : ")
        self.Name = input()
        print("Enter its Author : ")
        self.Author = input()

    def Display(self):
        print("{} by {}.No of Books : {}".format(self.Name,self.Author,BookStore.NoOfBooks))


def main():

    Obj1 = BookStore()
    Obj1.Accept()
    Obj1.Display()

    Obj2 = BookStore()
    Obj2.Accept()
    Obj2.Display()


if __name__ == "__main__":
    main()