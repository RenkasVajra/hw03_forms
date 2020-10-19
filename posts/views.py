from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Group, Post


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {
        "group": group, 
        "posts": posts,
    })  

def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {
        "posts": latest,
    })

@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    if not request.method == 'POST':
        if not form.is_valid():
            form.save()
        else: 
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    return render(request, 'new.html', {'form': form})
    if not request.method == 'GET':
        form = PostForm(request.GET)
        if not form.is_valid():
            form = PostForm()
            return redirect('index')
        else:
            form.save(form)
    form = PostForm()
    return render(request, 'new.html', {'form': form})       
