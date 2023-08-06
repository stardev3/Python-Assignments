from sys import *
import os
import psutil

def ProcInfoLog(log_dir):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"ProcessInfo.log")
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Current Running Process Information Log : \n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            f.write(str(pinfo))
            f.write("\n")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

def main():
    print("----------Process Monitor Automation Application----------")
    print("Process Monitor")

    ProcInfoLog(argv[1])

if __name__ == "__main__":
    main()