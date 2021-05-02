import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SUBJECT = "VM test"
def sendgridmail(user,TEXT):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ritchie.vmware@gmail.com", "vmware@123")
    
    
    #mailtemptest
    conte="""
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>VM Customer Care Registration</center></h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <a href="http://localhost:8080/loginconfirmation/"""+user+""""><img src="http://assets.stickpng.com/images/59060d910cbeef0acff9a661.png" style="height: 300px;"></a>
                <div style="text-align:center;">
                    
                    <p>Ignore this message if you have not registered</p>
                    <a href="#">Read more</a>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    content1=Content("text/html",conte)




    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("ritchie.vmware@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "VM ware"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()
