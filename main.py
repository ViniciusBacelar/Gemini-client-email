import smtplib
from email.message import EmailMessage
import google.generativeai as genai

def send_email(sender, password, recipient, message):
    # Set up email message
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Test Email"
    email.set_content(message)

    # Establish SMTP connection
    smtp = smtplib.SMTP("smtp-mail.outlook.com",port=587)
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()

def main():
    # Get user input
    sender_input = input("Type your email address: ")
    password = input("Type your password: ")
    recipient_input = input("Type the recipient: ")
    message = input("Type your message: ")

    # Validate user input
    if not sender_input or not password or not recipient_input or not message:
        print("Invalid input. Please try again.")
        return

    # Send email
    try:
        send_email(sender_input, password, recipient_input, message)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

if __name__ == "__main__":
    main()
