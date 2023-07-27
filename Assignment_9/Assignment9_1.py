import os

def Chk_File(File_Name):
    if(os.path.exists(File_Name)):
        print("File already exists")
        return 
    else:
        print("File does not exist")

def main():
    print("Enter file name to check whether it exists or not : ")
    fname = input()

    Chk_File(fname)

if __name__ == "__main__":
    main()