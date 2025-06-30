from django.urls import path
from user.views import login,recover_password

urlpatterns = [
    path('login/',login,name='login'),
    path('forgotPws/',recover_password,name='forgotPws')
]