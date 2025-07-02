from django.shortcuts import render
from user.forms import UserFormLogin
from user.models import User
from user.emails.base import send_email

def login(request):
    form_login = UserFormLogin()
    context = {
        'form_login': form_login
    }
    return render(request, 'login.html', context)

def recover_password(request):
    if request.method == "GET":
        context = {
            'user_exist': None 
        }
        return render(request, 'forgot_password.html', context)

    email_user_input = request.POST.get('email_user_input')
    user_exist = User.objects.filter(email=email_user_input).first()

    if user_exist:
        context = {
            'user_exist': user_exist,
            'mensege': 'verifique sua caixa de email'
        }
        send_email(f'{user_exist.email}')
    else:
        context = {
            'user_exist': False,  
            'mensege': 'email não existe'
        }

    return render(request, 'forgot_password.html', context)
