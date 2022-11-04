from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Comment(models.Model):
    username = models.CharField(max_length=20)   #유저이름
    comment = models.TextField(null=True, blank=True) #리뷰내용
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #평점
    created_time = models.DateTimeField(auto_now_add=True) #댓글작성
    update_time = models.DateTimeField(auto_now=True) #댓글수정
