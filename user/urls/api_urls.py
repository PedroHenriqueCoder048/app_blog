from django.urls import path

from user.views.api import get_users,user_manager

urlpatterns = [
    path('api/users/', get_users, name='get_all_users'),
    path('api/user',user_manager,name='get_user_name')
]

