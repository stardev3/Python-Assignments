
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print(No+1)
        
def main():
    Display(5)

if __name__ == "__main__":
    main()