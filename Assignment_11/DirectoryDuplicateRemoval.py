import os
from sys import *
import hashlib
import time

def DeleteFiles(dict1,log_dir):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    separator = "-" * 80
    log_path = os.path.join(log_dir, "DuplicatesRmvLogFile.log")
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Directory Duplicate Files Removal Logger : " + time.ctime() + "\n")
    f.write(separator + "\n")

    iCnt = 0

    if len(results) > 0:
        f.write("Duplicates Files Removed : \n")
        f.write("The following files were found identical : \n")
        for result in results:
            for subresult in result:
                iCnt += 1
                if iCnt >= 2:
                    f.write(subresult)
                    f.write("\n")
                    os.remove(subresult)
            iCnt = 0
    else:
        f.write("No duplicate files found")

def hashfile(path,blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subDirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")


def main():
    print("-----------Directory Duplicate File Removal Application-----------")
    print("Application Name : " + argv[0])

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script will delete all the duplicate files in a directory")
        exit()

    if ((argv[1] == "-u") or (argv[1]) == "-U"):
        print("Usage : Application_name Direcory_Name")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        DeleteFiles(arr,argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if (__name__ == "__main__"):
    main()