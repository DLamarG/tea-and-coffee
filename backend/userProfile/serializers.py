from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields=['id','first_name','last_name','about_me']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1



class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields=['id','user','first_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1