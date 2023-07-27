import os
from sys import *
import filecmp

def Compare_Files(File_Name1,File_Name2):
    if((os.path.exists(File_Name1)) and (os.path.exists(File_Name2))):
        Result = filecmp.cmp(File_Name1,File_Name2)
        if(Result == True):
            print("Success")
        else:
            print("Failure")
    else:
        print("Files does not exist")

def main():
    if(len(argv) < 3):
        print("Invalid number of Arguments")

    Compare_Files(argv[1],argv[2])

if __name__ == "__main__":
    main()