from django import forms


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from . import views
from posts.models import Post 


User = get_user_model()

#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username", "email") 
# forms for /new/
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text',)    
        labels = {
            'group': 'Группа',
            'text': 'Текст',
            'author': 'Автор',
        }
