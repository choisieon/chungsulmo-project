from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),

    path('conservation/', views.conservation, name='conservation'),
    path('mentoring/', views.mentoring, name='mentoring'),
    path('mypage/', views.mypage, name='mypage'),
]