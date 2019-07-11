import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

class email:
   
    def sendEmail(self,fromaddr,toaddr,filepath):   
        fromaddr = fromaddr
        toaddr = toaddr
        msg = MIMEMultipart() 
        msg['From'] = fromaddr 
        msg['To'] = toaddr 
        msg['Subject'] = "Automation Sanity Results"
        body = "please find the attached file."
        msg.attach(MIMEText(body, 'plain')) 
        filename = "Demo automation"
        attachment = open(filepath, "rb") 
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
        s = smtplib.SMTP('smtp.live.com', 587) 
        s.starttls() 
        s.login(fromaddr, "Welcome12$") 
        text = msg.as_string() 
        s.sendmail(fromaddr, toaddr, text) 
        s.quit() 

#sendmail = email() 
#sendmail.sendEmail("ganesh.kumar1986@hotmail.com", "ganesh.kumar1986@hotmail.com","testme.txt")  
#print("email hase been send to user,please check the email")  
