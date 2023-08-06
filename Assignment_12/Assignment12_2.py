from sys import *
import psutil

def ProcInfo(PName):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            if(PName == pinfo['name']):
                print(pinfo)
            else:
                print("There is no such process currently running")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

def main():
    print("----------Process Monitor Automation Application----------")
    print("Process Monitor")

    if(len(argv) != 2):
        print("Invalid Number of Arguments")

    ProcInfo(argv[1])

if __name__ == "__main__":
    main()