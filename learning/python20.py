# 发送电子邮件
import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
print(smtpObj.ehlo())
print(smtpObj.starttls())

print("input your pass:")
myPass = input()
print(smtpObj.login('chengshuozhang666@gmail.com', myPass))

print(smtpObj.sendmail('chengshuozhang666@gmail.com', 'testchengshuo@163.com',
                       'Subject: So long.'
                       '\n\n Dear , so long and thanks for all the fish. Sincerely,shuo'))
print(smtpObj.quit())
