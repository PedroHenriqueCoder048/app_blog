from django.urls import path
from blog.views.api import get_blogs,blog_manage,reactios_manage

urlpatterns = [
    path("api/blogs/",get_blogs,name="get_blogs"),
    path("api/blog/",blog_manage,name="blog_manager"),
    path("api/blog/<int:blog_id>/reactions/",reactios_manage,name="reactions_manager"),
]