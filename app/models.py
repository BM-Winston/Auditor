from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auditor(models.Model):
    image=models.ImageField(upload_to='images/',null=True)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    url= models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def save_auditor(self):
        self.save()

    def delete_auditor(self):
        self.delete()

    def update_auditor(self):

        self.update()

    @classmethod
    def search_auditor(cls,searchTerm):
        titles=cls.objects.filter(title__icontains=searchTerm)
        return titles


class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True)
    bio = models.TextField()
    email=models.EmailField(null=True)
    auditor =models.ForeignKey('Auditor',on_delete=models.CASCADE, null=True)
    score= models.IntegerField(default=0)


    def __str__(self):
        return self.user.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

        






