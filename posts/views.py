from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/posts_list.html', {'posts': posts}  )

def post_detail(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug = slug)
    return render(request, "posts/post_detail.html", {'post':post})


@login_required(login_url="/accounts/login")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    
    return render(request, "posts/post_create.html", {'form': form})