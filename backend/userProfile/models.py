from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    first_name=models.TextField(max_length=50,blank=True)
    last_name=models.TextField(max_length=50,blank=True)
    about_me = models.CharField(max_length=250, blank=True)
    picture = models.FileField(upload_to="profile_pics", blank=True, null=True)

    def __str__(self):
        return self.user.username