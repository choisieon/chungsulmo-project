from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),           # 글 목록
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 글 상세
    path('post/new/', views.post_new, name='post_new'),    # 글쓰기
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('category/<str:category>/', views.category_posts, name='category_posts'),
    path('category/<str:category>/<str:subcategory>/', views.subcategory_posts, name='subcategory_posts'),
]
