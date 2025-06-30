from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','user_name')
    search_fields = ('name','sur_name','user_name')
    list_filter= ('name','user_name')