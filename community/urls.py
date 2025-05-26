from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls'))
]