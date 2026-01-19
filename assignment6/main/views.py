from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

def posts_by_author(request, username):
    posts = Post.objects.filter(author__username=username)
    return render(request, 'main/posts.html', {'posts': posts})

def api_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        if 'author' in request.GET:
            posts = posts.filter(author__username=request.GET['author'])
        if 'category' in request.GET:
            posts = posts.filter(category__name=request.GET['category'])

        data = list(posts.values(
            'id',
            'title',
            'content',
            'author__username',
            'category__name',
            'created_at'
        ))
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        author = User.objects.get(id=data['author'])
        category = Category.objects.get(id=data['category'])

        post = Post.create(
            title=data['title'],
            content=data['content'],
            author=author,
            category=category
        )
        return JsonResponse({'id': post.id, 'message': 'Created'})


# Create your views here.
