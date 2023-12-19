from django.shortcuts import render, get_object_or_404
from blogApp.models import Category, Post

# Create your views here.
def index(request):
    hero_posts = Post.objects.all().order_by('-created_at')[0:3]
    lg_posts = Post.objects.all().order_by('-created_at')[0:1]
    entry_posts = Post.objects.all().order_by('-created_at')[1:4]
    entry2_posts = Post.objects.all().order_by('-created_at')[4:8]
    recent_posts = Post.objects.all().order_by('-created_at')[0:4]
    all_posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    context = {
        'hero_posts': hero_posts,
        'lg_posts': lg_posts,
        'entry_posts': entry_posts,
        'entry2_posts': entry2_posts,
        'recent_posts': recent_posts,
        'all_posts': all_posts,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def single_post(request, slug):
    categories = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-created_at')[0:4]
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'posts/single-post.html', context)

def category(request):
    return render(request, 'posts/category.html')