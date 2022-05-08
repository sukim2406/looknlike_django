from django.forms import ModelForm
from postapp.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']

class PostUpdateForm(PostCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].disabled = True