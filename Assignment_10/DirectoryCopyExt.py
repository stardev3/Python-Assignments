import os
import shutil
from sys import *

def DirCopy(FDirectory,SDirectory,Extension):
    os.mkdir(SDirectory)
    for FCnt in os.listdir(FDirectory):
        if FCnt.endswith(Extension):
            shutil.copy(os.path.join(FDirectory,FCnt),SDirectory)
            

def main():
    print("-----Directory Copy Extension Application-----")

    if(argv[1] == "-h"):
        print("Copies file with specific extension from one directory to another")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_Name First_Directory_Name Second_Directory_Name Extension")
        exit()

    DirCopy(argv[1] ,argv[2], argv[3])

if __name__ == "__main__":
    main()