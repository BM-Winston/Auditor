from django.contrib import admin

# Register your models here.
from .models import Auditor, Profile

admin.site.register(Auditor)
admin.site.register(Profile)
