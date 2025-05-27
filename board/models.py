from django.db import models
from django.contrib.auth.models import User  # User 모델 임포트 추가
# Create your models here.
class Post(models.Model):  # 이 부분이 반드시 있어야 함
    CATEGORY_CHOICES = [
        ('home', '홈'),
        ('review', '후기'),
        ('question', '궁금해'),
        ('share', '자료공유'),
        ('chat', '잡담'),
    ]
    SUBCATEGORIES = {
        'review': [
            ('home', '홈'),
            ('life', '인생'),
            ('living', '자취'),
            ('univ', '대학'),
            ('money', '지갑'),
            ('sport', '운동'),
            ('love', '연애'),
            ('comp', '직장'),
    ],
        'question': [
            ('home', '홈'),
            ('life', '인생'),
            ('living', '자취'),
            ('univ', '대학'),
            ('money', '지갑'),
            ('sport', '운동'),
            ('love', '연애'),
            ('comp', '직장'),
    ],
        'share': [
            ('home', '홈'),
            ('life', '인생'),
            ('living', '자취'),
            ('univ', '대학'),
            ('money', '지갑'),
            ('sport', '운동'),
            ('love', '연애'),
            ('comp', '직장'),
    ],
        'chat': [
            ('home', '홈'),
            ('life', '인생'),
            ('living', '자취'),
            ('univ', '대학'),
            ('money', '지갑'),
            ('sport', '운동'),
            ('love', '연애'),
            ('comp', '직장'),
    ],
    }
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='home')  # 카테고리 필드
    subcategory = models.CharField(max_length=20, choices=SUBCATEGORIES, blank=True, null=True)
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