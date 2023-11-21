from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from tea_reviews.models import TeaReview

class Tea(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to="tea/", blank=True, null=True)
    caffeine = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=3.00)



    