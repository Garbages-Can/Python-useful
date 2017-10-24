import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')  # 这里是你的信件中的内容
msg['From'] = 'ltoddy@163.com'  # 这里是发送人的邮箱.
msg['To'] = 'ltoddy@qq.com'  # 这里是接收信件人的邮箱
msg['Subject'] = 'an email'  # 这里是信件的标题

server = smtplib.SMTP('smtp.163.com') # 163 SMTP 服务器地址
server.login(user='ltoddy@163.com', password='lt19970516')
# user 是发送人的邮箱, password 是你的授权码!授权码!授权码!(这不是我生日.)
server.send_message(msg=msg)

server.close()
 