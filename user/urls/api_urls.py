from django.urls import path
from user.views import api_views
   
urlpatterns =[
    path('api/users/',api_views.get_users,name='get_all_users'),
    path('user/<str:user_name>',api_views.get_user)
]