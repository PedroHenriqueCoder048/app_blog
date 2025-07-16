from django.shortcuts import render,redirect
from user.models import User

def login(request):
    
    if request.method == "GET":
        context = {'user_exist':None}
        return render(request, 'login.html')

    if request.method == "POST":
        user_login =request.POST.get("user-login")
        user_psw = request.POST.get("user-psw")

        if not user_login or not user_psw:
            return render(request, 'login.html')
        
        user = User.get_user(user_login,user_psw)
        print('usuario',user)

        if user:
            return redirect('home')
        else:
            context = {'user_exist':False}
            return render(request, 'login.html',context)

def recover_password(request):
    if request.method == "GET":
        context = {
            'user_exist': None 
        }
        return render(request, 'forgot_password.html', context)

    email_user_input = request.POST.get('email_user_input')
    user_exist = User.objects.filter(email=email_user_input).first()

    if user_exist:
        user_exist.recover_password()
        context = {
            'user_exist': user_exist,
            'mensege': 'verifique sua caixa de email'
        }
    else:
        context = {
            'user_exist': False,  
            'mensege': 'email não existe'
        }

    return render(request, 'forgot_password.html', context)
