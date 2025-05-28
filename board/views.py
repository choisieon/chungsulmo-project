from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'board/post_list.html', {'posts': posts, 'current_category': None})

def category_posts(request, category):
    posts = Post.objects.filter(category=category).order_by('-pub_date')
    category_name = dict(Post.CATEGORY_CHOICES).get(category, '전체')
    subcategories = Post.SUBCATEGORIES.get(category, [])
    return render(request, 'board/post_list.html', {
        'posts': posts,
        'current_category': category,
        'category_name': category_name,
        'subcategories': subcategories,
    })

def subcategory_posts(request, category, subcategory):
    posts = Post.objects.filter(category=category, subcategory=subcategory).order_by('-pub_date')
    subcategories = Post.SUBCATEGORY_CHOICES
    return render(request, 'board/post_list.html', {
        'posts': posts,
        'current_category': category,
        'current_subcategory': subcategory,
        'subcategories': subcategories,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가(본인 제외)
    if request.user != post.author:
        post.views += 1
        post.save()

    comments = post.comments.filter(parent__isnull=True)
    comment_form = CommentForm(request.POST or None)
    
    if request.method == 'POST' and comment_form.is_valid():
        parent_id = comment_form.cleaned_data.get('parent_id')
        parent = None
        
        if parent_id:
            try:
                parent = Comment.objects.get(id=parent_id, post=post)
            except Comment.DoesNotExist:
                parent = None

        Comment.objects.create(
            post=post,
            author=request.user,
            content=comment_form.cleaned_data['content'],
            parent=parent
        )
        return redirect('post_detail', pk=pk)

    return render(request, 'board/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 로그인한 사용자가 있으면 그 유저를, 아니면 임시로 첫 번째 유저를 author로 지정
            if request.user.is_authenticated:
                post.author = request.user
            else:
                post.author = User.objects.first() # 임시로 첫 번째 유저 지정
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})



@require_POST
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=post.pk)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        # 권한 없음 처리 (예: 403 에러)
        return redirect('post_list')
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    # GET 요청 시 삭제 확인 페이지로 이동 (선택)
    return render(request, 'board/post_confirm_delete.html', {'post': post})

def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            post.likes.remove(user)   # 이미 좋아요 눌렀으면 취소
        else:
            post.likes.add(user)    # 안 눌렀으면 추가
    return redirect('post_detail', pk=pk)