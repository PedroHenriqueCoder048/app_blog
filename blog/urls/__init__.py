from .api_urls import urlpatterns as api_patterns
from .views_urls import urlpatterns as views_patterns

urlpatterns = api_patterns + views_patterns