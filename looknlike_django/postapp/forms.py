from django.forms import ModelForm
from postapp.models import Post
from django import forms
from projectapp.models import Project


class PostCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable', 'style': 'height: auto; text-align: left;'}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'project', 'content', ]

class PostUpdateForm(PostCreationForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable', 'style': 'height: auto; text-align: left;'}))
    
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].disabled = True