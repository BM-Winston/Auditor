from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Models):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image = models.ImageFiel(upload_to='profile_pics/', null=True)
    bio = models.TextField()


