from django.contrib import admin
from .models import UserTask

# Register your models here.

class UserTaskadmin(admin.ModelAdmin):
    list_display=("user","title")

    

admin.site.register(UserTask,UserTaskadmin)


