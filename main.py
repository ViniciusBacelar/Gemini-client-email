"""
This script sends an email using a generated message from a pre-trained AI model.
"""

import smtplib
from email.message import EmailMessage
import google.generativeai as genai

"""
Set API key for Gemini model
"""
GOOGLE_GEMINI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"

"""
Configure Gemini model with API key
"""
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

"""
Load GenerativeModel for text generation
"""
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

"""
Function to send an email
"""


def send_email(sender, password, recipient, message):
    """
    Send an email using the provided sender, password, recipient, and message.

    Args:
        sender (str): The sender's email address.
        password (str): The sender's email password.
        recipient (str): The recipient's email address.
        message (str): The message to be sent.
    """
    try:
        # Set up email message
        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = "Test Email"
        email.set_content(message)

        # Establish SMTP connection
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))


"""
Main function
"""


def main():
    """
    Get user input, generate a more formal message using the pre-trained model, and send the email.
    """
    # Get user input
    sender_input = input("Type your email address: ")
    password = input("Type your password: ")
    recipient_input = input("Type the recipient: ")
    message = input("Type your message: ")
    enhancer = f'Improve this email message with business formality: {message}'
    print("Improving your message!")

    try:
        # Generate a more formal message using the pre-trained model
        response = model.generate_content(enhancer)
        improved_message = response.text
        print(improved_message)
    except Exception as e:
        print("Error improving email:", str(e))
        return

    # Validate user input
    if not sender_input or not password or not recipient_input or not message:
        print("Invalid input. Please try again.")
        return

    # Send email
    send_email(sender_input, password, recipient_input, improved_message)


if __name__ == "__main__":
    main()