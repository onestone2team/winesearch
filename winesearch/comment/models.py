from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User
from tweet.models import Tweet


# Create your models here

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)   #유저이름
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    comment = models.TextField() #리뷰내용
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) #평점
    created_time = models.DateTimeField(auto_now_add=True) #댓글작성
    update_time = models.DateTimeField(auto_now=True) #댓글수

    def __str__(self):
        return str(self.username)
