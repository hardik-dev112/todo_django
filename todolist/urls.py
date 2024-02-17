
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home),
    path("register/",register),
    path("signin/", signin),
    path("signout/",signout),
    path("signup/",signup),
    path("add/",add),
    path('status/<int:id>',status),
    path('delete/<int:id>',delete),
    path('edit/<int:id>',edit),
]
