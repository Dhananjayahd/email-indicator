import serial
import time
import email                                                                 
import imaplib
import ctypes
import getpass

x = serial.Serial('com3',9600)
mail = imaplib.IMAP4_SSL('imap.gmail.com','993')
user = 'your email address'
pwd = 'your email password'
mail.login(user,pwd)
mail.select("INBOX")
if __name__ == '__main__':
    try:
        while True:
            mail.select("INBOX")
            n=0
            (retcode,messages)= mail.search(None,'(UNSEEN)')
            if retcode == 'OK':
                for num in messages[0].split():
                    n=n+1
                    x.write(n)
                    print (n)
                   
    finally:
        print ("thanks")

