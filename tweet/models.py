from django.db import models
# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(null = True)
    tag = models.CharField(max_length=50 , null = True)
    country = models.CharField(max_length=30, null = True)

    def __str__(self):
        return str(self.name)