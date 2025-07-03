import os 
import sys
from dotenv import load_dotenv
from django.core.mail import send_mail

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") 

load_dotenv()
class Email():
    def __init__(self,subject:str,message:str, from_email:str,to_emails:list):

        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.to_emails = to_emails

    def send_email(self):

        send_mail(
                self.subject,
                self.message,
                self.from_email,
                self.to_emails,
                fail_silently=False
            )