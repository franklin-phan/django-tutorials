from django.contrib import admin

#we need to tell the admin that Question objects have an admin interface
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
