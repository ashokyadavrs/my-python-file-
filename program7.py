#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("ashokmbl1999@gmail.com","ashokyadav123")
message="avikannana??"
s.sendmail("ashokmbl1999@gmail.com","avikannan13@gmail.com",message)
print("success")
s.quit()
