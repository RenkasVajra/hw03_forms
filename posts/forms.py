from django import forms


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from . import views
from posts.models import Post 


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = {"first_name", "last_name", "username", "email"}
# forms for /new/
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'group', 'text',}
        labels = {
            'group': 'Группа',
            'text': 'Текст',
        }
        help_text = {'name': 'Создайте свой новый пост.'}