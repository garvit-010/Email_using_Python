import yagmail
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")

# Function to send an email
def send_email(to, subject, message, attachments=None, cc=None, bcc=None, is_html=False):
    
    yag = yagmail.SMTP(USER_EMAIL, USER_PASSWORD)

    if is_html:
        message = yagmail.inline(message)

    yag.send(
        to=to,
        subject=subject,
        contents=message,
        attachments=attachments,
        cc=cc,
        bcc=bcc
    )

message = "Type your message here"

# Send the email

send_email(
        to="receiver@example.com",
        subject="Test Email",
        message=message,
        attachments=["file1.pdf"], 
        cc=["cc@example.com"], 
        bcc=["bcc@example.com"],
        is_html=False 
    )
