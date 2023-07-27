import os

def Display_File(File_Name):
    if(os.path.exists(File_Name)):
        fd = open(File_Name,"r")
        Data = fd.read()
        print("Displaying data from file : ")
        print(Data)
        fd.close()

    else:
        print("Such file does not exist")


def main():
    print("Enter File Name")
    fname = input()

    Display_File(fname)

if __name__ == "__main__":
    main()