from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'community/index.html')

def conservation(request):
    return render(request, 'community/conservation.html')

def mentoring(request):
    return render(request, 'community/mentoring.html')

def mypage(request):
    return render(request, 'community/mypage.html')