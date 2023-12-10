from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_home(request):
	blog_posts = BlogPost.objects.order_by('-date')
	return render(request, 'blog_home.html', {"blog_posts": blog_posts})

def detail(request, post_id):
	post = get_object_or_404(BlogPost, pk=post_id)
	return render(request, 'detail.html', {"post": post})