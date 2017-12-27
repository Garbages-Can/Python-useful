import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')
msg['From'] = 'ltoddy@163.com'
msg['Subject'] = 'an email'
server = smtplib.SMTP('smtp.163.com')
server.login(user='ltoddy@163.com', password='lt19970516')
to_addrs = ['ltoddy@qq.com', 'taoliu14@acm.org']
print('{} will send'.format(to_addrs))
server.sendmail(from_addr='ltoddy@163.com', to_addrs=to_addrs, msg=msg.as_string())
server.quit()
print('send mail ok')
