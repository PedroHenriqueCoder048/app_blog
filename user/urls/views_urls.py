from django.urls import path
from user.views.views import login, recover_password, create_user

urlpatterns = [
    path('index/login/', login, name='login'),
    path('index/forgot-password', recover_password, name='forgot-password'),
    path('index/create-user',create_user,name="create-user")
]
