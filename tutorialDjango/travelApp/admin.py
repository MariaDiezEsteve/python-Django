from django.contrib import admin

# Register your models here.

from .models import City, Monument

admin.site.register(City)
admin.site.register(Monument)