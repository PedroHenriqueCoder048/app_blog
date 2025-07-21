from django.urls import path
from blog.views.views import home

urlpatterns = [
    path('home/',home ,name='home'),
]