from sys import *
import os
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def ProcInfoLog(log_dir,mailid):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"ProcessInfo.log")
    LFile = open(log_path,'w')
    LFile.write(separator + "\n")
    LFile.write("Current Running Process Information Log : \n")
    LFile.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            LFile.write(str(pinfo))
            LFile.write("\n")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    SMail = "inglevaibhavi03@gmail.com"
    SPass = "****************" #Gmail App Pass(Not Google Acc Pass)
    RMail = mailid
    mail_content = "Process Information Log File"

    Msg = MIMEMultipart()
    Msg['From'] = SMail
    Msg['To'] = RMail

    Msg.attach(MIMEText(mail_content,'plain'))
    AFile = open(log_path,"rb")
    payload = MIMEBase('application','octate-stream')
    payload.set_payload((AFile).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition',"attachment; AFile= %s" % AFile)
    Msg.attach(payload)

    Session = smtplib.SMTP('smtp.gmail.com',587)
    Session.starttls()
    Session.login(SMail,SPass)
    Txt = Msg.as_string()
    Session.sendmail(SMail,RMail,Txt)
    Session.quit
    print("Mail Sent")


def main():
    print("----------Process Monitor Automation Application----------")
    print("Process Monitor")

    ProcInfoLog(argv[1],argv[2])

if __name__ == "__main__":
    main()