from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','autor')
    # search_fields = ('name','surname','user_name')
    # list_filter= ('name','user_name')