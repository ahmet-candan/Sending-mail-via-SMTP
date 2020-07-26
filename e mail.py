import smtplib

host = "smtp.gmail.com"
port = 587
username = "ahmetcandan1234@gmail.com"
password = "pass"
from_mail = username
to_mail = ["ahmetcandan1@outlook.com.tr"]

email_conn =smtplib.SMTP(host,port) 
print(email_conn.ehlo())
print(email_conn.starttls())
email_conn.login(username,password)
print(email_conn.sendmail(from_mail,to_mail, "Merhaba, Python ile mail gönderiyorum. Ahmet Candan"))
email_conn.quit()


