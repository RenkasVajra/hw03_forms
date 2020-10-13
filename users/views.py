from django.shortcuts import render
#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView
#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
from django.urls import reverse_lazy

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm
from .forms import ExchangeForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") #  где login — это параметр "name" в path()
    template_name = "signup.html" 
# for page /new/
def new_post(request):
    if request.method == 'PostForm':
        form = ExchangeForm(request.PostForm)
        if form.is_valid():
            group = form.cleaned_data['group']
            posts = form.cleaned_data['posts']
            return redirect('new_post')
        return render(request, 'index.html', {'form': form})
    form = ExchangeForm()
    return render(request, 'index.html', {'form': form})
