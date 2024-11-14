
import sys
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase



#creating a message  A message can be considered as python dictionary
message = MIMEMultipart()  # Create a message object
message["From"] = 'Priyath Perera'  # Set the sender email address
message["To"] = 'dirunthaperera123@gmail.com'  # Set the recipient email address
message["Subject"] = "Test Email"  # Set the email subject

html_content = """
<html>
  <body>
    <p>This is an example of <strong>rich text formatting</strong> in an email.</p>
    <p>Here is an inline image: <img src="image.jpg" alt="Inline Image"></p>
  </body>
</html>


 """

#extracting the message from the file
with open('Message.txt', 'r') as f:
    message_body = f.read()
# message.attach(MIMEText(message_body, 'plain'))  # Attach the message body to the email   
message.attach(MIMEText(html_content, 'html'))  # Attach the message body to the email   

#Trying to add an image to the email
filename = "image.jpg"  # Set the file name
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename = {filename}")
    message.attach(part)


# Connect to the server
try:
    with open('password.txt', 'r') as f:
        password = f.read()
        
except:
    print("Password file not found")
    sys.exit()

try:    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # server.ehlo()
        server.starttls()  # Start the server
        server.login("priyathperera13@gmail.com",password)
        text=message.as_string() #convert the message to a string
        server.sendmail("priyathperera13@gmail.com","dirunthaperera123@gmail.com",text)#send the email
except Exception as e:
    print("Something went wrong",e)  
    sys.exit()       


print("Email sent successfully!")  # Print a success message after sending the email



