import os,hashlib
from sys import *
import time

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

def PrintDuplicate(dict1,log_dir):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    separator = "-" * 80
    log_path = os.path.join(log_dir,"DuplicatesLogFile.log")
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Directory Duplicate Files Logger : " + time.ctime() + "\n")
    f.write(separator + "\n")

    if len(results) > 0:
        f.write("Duplicates Found : \n")
        f.write("The following files are identical : \n")

        iCnt = 0;
        for result in results:
            for subresult in result:
                iCnt += 1
                if iCnt >= 2:
                    f.write(subresult)
                    f.write("\n")

    else:
        f.write("No Duplicates found")

def main():
    print("-----Directory Duplicate Files Application-----")

    if(argv[1] == "-h"):
        print("Creates log file of all duplicate files in a directory duplicates all files in a Directory")
        exit()

    if(argv[1] == '-u'):
        print("Usage : Application_Name Directory_Name")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr,argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if __name__ == "__main__":
    main()