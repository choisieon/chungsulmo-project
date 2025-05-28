from django.contrib import admin
from .models import Comment, Post  # Post도 같이 보고 싶으면 추가

# Register your models here.
admin.site.register(Comment)
# admin.site.register(Post)   # 필요하면 Post도 등록