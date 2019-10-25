from django.contrib import admin
from .models import Vendor, Food

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Food)