from rest_framework import serializers
from .models import  Auditor, Profile



class AuditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditor
        fields = ('title', 'description', 'url', 'image')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'image', 'user')
