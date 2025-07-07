from django.shortcuts import render
from user.models import User
from blog.models import Blog

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    user_login =request.POST.get("user-login")
    user_psw = request.POST.get("user-login-psw")

    if not user_login or not user_psw:
        return render(request, 'login.html')
    
    if user_login:
        user = User.get_user(user_login)
        print("user",user)

        if user:
            context = {
                'user_exist':True
            }
            return render(request, 'home.html',context)
        else:
            context = {
                'user_exist':False
            }
            return render(request, 'login.html',context)

def home(request):

    # if request.method == "GET":

        blogs = Blog.objects.all()
        print('lista d blogs',blogs)
        context = {
            'blogs':blogs
        }
        return render(request, 'home.html',context)


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
