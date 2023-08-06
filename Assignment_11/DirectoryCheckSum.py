import os,hashlib
from sys import *

def DirChkSum(Directory):
    Files = os.scandir(Directory)
    for File in Files:
        with open(File,"rb") as f:
            ChkSum = hashlib.md5(f.read()).hexdigest()
            print("File Name : ",File)
            print("ChkeckSum = ",ChkSum)

def main():
    print("-----Directory CheckSum Application-----")

    if(argv[1] == "-h"):
        print("Display checksum all files in a Directory")
        exit()

    if(argv[1] == '-u'):
        print("Usage : Application_Name Directory_Name")
        exit()

    DirChkSum(argv[1])

if __name__ == "__main__":
    main()