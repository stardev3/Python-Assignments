import threading

def DEven(No):
    i = 1
    while i <= No:
        print("Even Number : ",2 * i)
        i = i + 1

def DOdd(No):
    i = 1
    while i <= No:
        print("Odd Number",2 * i - 1)
        i = i + 1


def main():
    Rnge = 10

    DisplayEven = threading.Thread(target = DEven,args = (Rnge,))
    DisplayOdd = threading.Thread(target = DOdd,args = (Rnge,))

    DisplayEven.start()
    DisplayOdd.start()

    DisplayEven.join()
    DisplayOdd.join()


if __name__ == "__main__":
    main()