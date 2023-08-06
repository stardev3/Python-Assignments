import os
from sys import *
import hashlib
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

def SendMail(mailid):
    SMail = "inglevaibhavi03@gmail.com"
    SPass = "****************"  # Gmail App Pass(Not Google Acc Pass)
    RMail = mailid
    mail_content = "Duplicate File Removal Information Log File"

    Msg = MIMEMultipart()
    Msg['From'] = SMail
    Msg['To'] = RMail

    Msg.attach(MIMEText(mail_content, 'plain'))
    AFile = open(log_path, "rb")
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((AFile).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', "attachment; AFile= %s" % AFile)
    Msg.attach(payload)

    Session = smtplib.SMTP('smtp.gmail.com', 587)
    Session.starttls()
    Session.login(SMail, SPass)
    Txt = Msg.as_string()
    Session.sendmail(SMail, RMail, Txt)
    Session.quit
    print("Mail Sent")


def main():
    print("-----------Directory Duplicate File Removal Application-----------")
    print("Application Name : " + argv[0])


    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script will delete all the duplicate files in a directory")
        exit()

    if ((argv[1] == "-u") or (argv[1]) == "-U"):
        print("Usage : Application_name Direcory_Name")
        exit()


    try:
        arr = {}
        arr = schedule.every(int(argv[2])).minutes.do(FindDuplicate(argv[1]))
        DeleteFiles(arr,argv[1])
        SendMail(argv[3])

        while (True):
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if __name__ == "__main__":
    main()