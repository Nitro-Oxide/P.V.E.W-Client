from email.message import EmailMessage
import smtplib
def Send_Alert(subject, target):
    sender = "PVEWOffical@outlook.com"
    recipient = target
    message = "This is a demonstration of our powers of communication"

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=465)
    smtp.starttls()
    smtp.login(sender, "Burner.Lord123")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit() 

