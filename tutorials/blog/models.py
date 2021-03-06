from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()    #이미지 필드 생성
    lnglat = models.CharField(max_length=40, blank=True)
    is_public = models.BooleanField(default=False)    #공개여부 선택
    created_at = models.DateTimeField(auto_now_add=True)    #글 올린 시간
    updated_at = models.DateTimeField(auto_now=True)    #글 수정한 시간

    def __str__(self):
        return self.title    #리스트에 제목 출력

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
