from django.urls import path
from user.views.views import login, recover_password

urlpatterns = [
    path('index/login/', login, name='login'),
    path('index/forgot-password', recover_password, name='forgot-password'),
]
