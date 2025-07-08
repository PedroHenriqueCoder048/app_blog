from django.shortcuts import render
from blog.models import Blog

def home(request):
    if request.method == "GET":
        blogs = range(1000)
        print("view blog chamada")
        context = {
            'blogs':blogs
        }
        return render(request, 'home.html',context)