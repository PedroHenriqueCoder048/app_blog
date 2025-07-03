from django.urls import path
from user.views import login,recover_password,home

urlpatterns = [
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('forgotPws/',recover_password,name='forgotPws'),
]