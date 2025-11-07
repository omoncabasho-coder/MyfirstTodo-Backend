from django.contrib import admin

# Register your models here.

# anytime you create a model you must register the model in your admin.py file
from . models import Todo

admin.site.register(Todo)