from twilio.rest import Client

# Import Twilio credentials from a separate config file
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER,TO_PHONE_NUMBER

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"Message sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage
to_number = TO_PHONE_NUMBER 
message = "Hello from Twilio!"
send_sms(to_number, message)
