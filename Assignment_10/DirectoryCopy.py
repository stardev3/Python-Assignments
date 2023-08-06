import os
import shutil
from sys import *

def DirCopy(FDirectory,SDirectory):
    Files = os.listdir(FDirectory)
    shutil.copytree(FDirectory,SDirectory)


def main():
    print("-----Directory Copy Application-----")

    if(argv[1] == "-h"):
        print("Copies file from one directory to another")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_Name First_Directory_Name Second_Directory_Name")
        exit()

    DirCopy(argv[1] ,argv[2])

if __name__ == "__main__":
    main()