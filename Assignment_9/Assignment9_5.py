import os
from collections import Counter

def Data_Freq(File_Name):
    Cnt = 0
    if(os.path.exists(File_Name)):
        fd = open(File_Name,"r")
        Data =  Counter(fd.read().split())
        for i,j in Data.items():
            if(i == "marvellous"):
                print(i,j)
                
    else:
        print("File does not exist")
    

def main():
    print("Enter File Name")
    fname = input()

    Data_Freq(fname)

if __name__ == "__main__":
    main()