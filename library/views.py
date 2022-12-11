from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/index.html', {'posts': posts})

def authorization(request):
    return render(request, 'library/authorization.html', {})

def registration(request):
    return render(request, 'library/registration.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'library/post_detail.html', {'post': post})