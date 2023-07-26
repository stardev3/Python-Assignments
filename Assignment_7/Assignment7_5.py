import threading

def Ascending():
    No = 50
    for i in range(1,No+1):
        print(i,end = " ")

def Descending():
    No = 50
    for i in range(No,0,-1):
        print(i, end=" ")

def main():

    thread1 = threading.Thread(target = Ascending)
    thread2 = threading.Thread(target = Descending)

    print("Displaying from Thread 1")
    thread1.start()
    thread1.join()
    print("\n")
    print("Displaying from Thread 2")
    thread2.start()

if __name__ == "__main__":
    main()