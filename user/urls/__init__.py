from .views_urls import urlpatterns as html_urlpatterns
from .api_urls import urlpatterns as api_urlpatterns

urlpatterns = html_urlpatterns + api_urlpatterns
