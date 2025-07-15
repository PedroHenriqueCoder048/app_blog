from django.urls import path
from user.views.render_views import login,recover_password,home
from user.views import api_views

urlpatterns = [
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('forgotPws/',recover_password,name='forgotPws'),
    path('api/users/',api_views.get_users,name='get_all_users')
]