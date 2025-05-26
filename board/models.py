from django.db import models
from django.contrib.auth.models import User  # User 모델 임포트 추가
# Create your models here.
class Post(models.Model):  # 이 부분이 반드시 있어야 함
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User 모델 사용
    pub_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # 조회수
    likes = models.ManyToManyField(User, related_name='liked_posts')  # 좋아요
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # 이미지 필드 추가

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.content[:20]}"