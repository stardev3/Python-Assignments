import os
from sys import *

def DirRename(Directory,FExtension,OExtension):
    for OFile in os.listdir(Directory):
        if OFile.endswith(FExtension):
            NFile = OFile.replace(FExtension,OExtension)
            os.rename(OFile,NFile)

def main():
    print("-----Directory Rename Application-----")
    
    if(argv[1] == "-h"):
        print("Renames all files with different extension")
        exit()
        
    if(argv[1] == "-u"):
        print("Usage : Application_Name Directory_Name First_Extension Second_Extenstion")
        exit()

    DirRename(argv[1],argv[2],argv[3])

if __name__ == "__main__":
    main()