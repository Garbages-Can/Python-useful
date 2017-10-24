<small>sendemail.py</small>
```python
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
```

借用SMTP(简单邮件传输协议)和163邮箱来发送邮件.

使用方法:

> python3 sendemail.py

这个程序我已经运行过了,没有问题,163邮箱是我随便注册的,随便任何人使用.
不过目前这个程序的接受人是我,所以你运行的话,希望更换一下接收人.


#### 网易163免费邮箱相关服务器信息

|服务器名称|服务器地址|SSL协议du端口号|非SSL协议端口号|
|----|----|---|---|
|IMAP|imap.163.com|993|143|
|SMTP|smtp.163.com|465/994|25|
|POP3|pop.163.com|995|110