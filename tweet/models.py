from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(null = True)
    tag = models.CharField(max_length=50 , null = True)
    country = models.CharField(max_length=30, null = True)
    taster_name = models.CharField(max_length=20, null=True)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.TextField(null = True)

    def __str__(self):
        return str(self.name)