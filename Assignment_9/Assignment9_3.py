import os
from sys import *

def Copy_File(File_Name):
    if(os.path.exists(File_Name)):
        fd = open(File_Name, "r")
        Data = fd.read()

        New_File = open("Demo.txt","a")
        New_File.write(Data)

    else:
        print("File does not exist")

def main():
    if(len(argv) < 2):
        print("Invalid number of Arguments")

    Copy_File(argv[1])

if __name__ == "__main__":
    main()