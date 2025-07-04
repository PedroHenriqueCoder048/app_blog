from django.shortcuts import render
from user.models import User
from blog.models import Blog

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    user_input =request.POST.get("user-login")
    # user_psw = request.POST.get("user-psw-login")

    if not user_input:
        return render(request, 'login.html')
    
    if user_input:
        user = User.get_user(user_input)

        if user:
            context = {
                'encontrado':True
            }
            return render(request, 'home.html',context)
        else:
            context = {
                'encontrado':False
            }
            return render(request, 'login.html',context)

def home(request):

    blogs = Blog.objects.all()

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
