import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


title = 'This is Title'
title2 = 'This is another title'
header = '<html><head><meta http-equiv="Content-Type" content="text/html" /></head>'
th = '<body><table width="80%" border="0" cellspacing="0" cellpadding="0" align="center">' + \
'<tr ><td align="center" height="60"><b><font size="5">' + title + \
'</font></b></td></tr>' + \
'<tr ><td align="center" height="40" ><b><font color="red" size="2">' + title2 + \
'</font></b></td></tr>' + \
'</table>' + \
'<br />' + \
'<table border="1" cellspacing="0" cellpadding="0" bordercolor="#E0E0E0" width="80%" align="center" >' + \
'<tr bgcolor="#3399FF" align="center" height="40" ><th>xxx</th><th>xxx</th><th>xxx</th><th>xxx</th></tr>'
body = ''
tds = ''
trs = ''
red = 'style=\"background-color:#FF0000\"'
green = 'style=\"background-color:#33FF00\"'
yellow = 'style=\"background-color:#FF9900\"'
rowColor = ['style=\"background-color:#FFFFFF\"', 'style=\"background-color:#CCFFFF\"']


COMMASPACE = ', '
msg = MIMEMultipart()
msg['Subject'] = 'This is Subject'
msg['From'] = your_mail_addr
msg['To'] = COMMASPACE.join(self.mail_list)
msg['Cc'] = COMMASPACE.join(Cclist)

trs = trs + sum
body = body + trs + '</table><br />'

cov_title = '<table width="80%" border="0" cellspacing="0" cellpadding="0" align="center">' + \
'<tr ><td align="center" height="60"><b><font size="5">' + 'xxxx' + \
'</font></b></td></tr></table>'
tail = '</body></html>'
mail = header + th + body + cov_title  + tail
# mail body
msg.attach(MIMEText(mail, 'html'))

# mail attachment
att1 = MIMEText(open(self.mail_textPath, 'rb').read())
att1["Content-Disposition"] = 'attachement; filename=\"' + 'xxx.csv\"'

# Use Application to avoid End of Line Issue
att2 = MIMEBase('application', 'octet-stream')
att2.set_payload(open(rename_cov, 'rb').read())
encoders.encode_base64(att2)
att2.add_header('Content-Disposition', 'attachement; filename=\"' + rename_cov.split('\\')[-1] + '\"')
msg.attach(att1)
msg.attach(att2)
server = smtplib.SMTP('HostAddr')
server.starttls()
server.login(self.me, 'password')
server.sendmail(self.me, self.mail_list, msg.as_string())
server.quit()