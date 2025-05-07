import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Only use dotenv locally
if os.getenv("GITHUB_ACTIONS") != "true":
    from dotenv import load_dotenv
    load_dotenv()



def send_error_email(subject, body):

    if isinstance(body, list):
        body = "\n\n".join([
            "\n".join([f"{k}: {v}" for k, v in item.items()])
            for item in body
        ])
    else:
        body = str(body)
        
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_HOST_USER")
    msg['To'] = os.getenv("EMAIL_RECEIVER")

    try:
        with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
            server.starttls()
            server.login(os.getenv("EMAIL_HOST_USER"), os.getenv("EMAIL_HOST_PASSWORD"))
            server.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
