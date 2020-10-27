from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.checks.messages import Error
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Group, Post


User = get_user_model()

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {
        "group": group, 
        "posts": posts,
    })  

def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number)
    return render(
         request,
         'index.html',
         {'page': page, 'paginator': paginator}
    )

@login_required
def new_post(request): 
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form}) 

    post = form.save(commit=False)
    post.author = request.user
    post.save()
      
    return redirect('index')

def profile(request, username):

    post = get_object_or_404(Post, author__username=username) 
    if post is None:
        return redirect('signup')
 
    post_list = post.posts.all()[:10]
    post_count = post_list.count()
    paginator = Paginator(post_list, 10)
    post_latest = post_list.latest('pub_date')
    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number)
    context = {"post": post,
              "post_latest":post_latest,
              "post_count":post_count,
              "page":page,
              "paginator":paginator}
    return render(request, 'profile.html', context)
 
 
def post_view(request, username, post_id):
    post = get_object_or_404(Post,author__username=username,pk=post_id,)
    author = post.author
    return render(request, 'post.html', {'post': post,
                                        'author': author})

def post_edit(request, username, post_id):

    post = get_object_or_404(Post,author__username=username,pk=post_id,)
    if request.user.username != username: 
        return redirect('post', kwargs={
                                'username':username,
                                'post_id':post.pk
    })
  
    if not request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        return render(request,"new_post.html", {
                                              'form':form,
                                              'post':post,
                                              'edit_post':'Редактировать пост',
    })
    form = PostForm(request.POST)

    if form.is_valid():
        post = Post.objects.get(id=post_id)
        post.group = form.cleaned_data['group']
        post.text = form.cleaned_data['text']
        post.save()
        return redirect('post',kwargs={'username':username,
                                       'post_id':post_id, 
    })
    return render(request, 'new_post.html', {
                                            'form':form,
                                            'post':post,
                                            'edit_post':'Редактировать пост',
    })