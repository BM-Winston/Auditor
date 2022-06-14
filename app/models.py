from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auditor(models.Model):
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    url= models.URLField(max_length=200)


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True)
    bio = models.TextField()


    def __str__(self):
        return self.user.username






