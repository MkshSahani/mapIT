from django.contrib import admin

# Register your models here.

from .models import Friends

admin.site.register(Friends)  # register the Friends Model in the WebSite DataBase.
