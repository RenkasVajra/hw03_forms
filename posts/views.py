from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect,render
#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView
#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
from django.urls import reverse_lazy
from django.urls import reverse
#  импортируем класс формы, чтобы сослаться на неё во view-клаccf
from .forms import PostForm
from .models import Group, Post
from posts.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") #  где login — это параметр "name" в path()
    template_name = "signup.html" 


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
    
def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('index')

    return render(request, 'new.html', {  
                'form': form
            })

    if request.method == 'GET':
        form = PostForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'new.html', {  
                'form': form
            })       
    form = PostForm
