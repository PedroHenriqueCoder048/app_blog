from django.urls import path

from user.views.api import get_users,get_user

urlpatterns = [
    path('api/users/', get_users, name='get_all_users'),
    path('api/user',get_user,name='get_user_name')
]

