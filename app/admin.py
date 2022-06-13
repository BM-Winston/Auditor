from django.contrib import admin

# Register your models here.
from .models import Project, Profile

admin.site.register(Project)
admin.site.register(Profile)
