import os
from sys import *

def DirFileSearch(Directory,Extension):
    for Cnt in os.listdir(Directory):
        if Cnt.endswith(Extension):
            print(Cnt)

def main():
    print("-----Directory File Search Application-----")

    if(argv[1] == "-h"):
        print("Display all files with particular extension")
        exit()

    if(argv[1] == '-u'):
        print("Usage : Application_Name Directory_Name Extension")
        exit()

    DirFileSearch(argv[1],argv[2])

if __name__ == "__main__":
    main()