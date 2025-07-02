import os 
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") 
django.setup()


from django.core.mail import send_mail

def send_email(email):
    subject = 'TESTE DE EMAIL COM PYTHON'
    message = 'ESSE É UM TESTE DE EMAIL ENVIADO COM PYTHON'
    from_email =email 
    to_email = ['pedrohenriquecosta.profissional@gmail.com']

    send_mail(
        subject,
        message,
        from_email,
        to_email,
        fail_silently=False
    )
