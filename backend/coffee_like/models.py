from django.db import models


# Create your views here.
class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=False)
