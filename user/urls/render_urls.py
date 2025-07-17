
from django.urls import include, path

urlpatterns = [
    path('', include('user.urls.views_urls')),
    path('', include('user.urls.api_urls')),
]
