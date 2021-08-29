from django.contrib import admin

from .models import New, Keyword # Import from models.py class we created

admin.site.register(New)
admin.site.register(Keyword)