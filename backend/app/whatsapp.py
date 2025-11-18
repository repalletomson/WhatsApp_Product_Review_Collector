from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppService:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.client = Client(self.account_sid, self.auth_token) if self.account_sid and self.auth_token else None
    
    def send_message(self, to_number: str, message: str):
        if not self.client:
            print(f"Would send to {to_number}: {message}")
            return
        
        try:
            # Ensure proper phone number format
            if not to_number.startswith('+'):
                to_number = f'+{to_number}'
            
            message = self.client.messages.create(
                body=message,
                from_='whatsapp:+14155238886',  # Twilio Sandbox number
                to=f'whatsapp:{to_number}'
            )
            print(f"Message sent successfully to {to_number}: {message.sid}")
            return message.sid
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
            return None