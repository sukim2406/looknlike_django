from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from commentapp.models import Comment
from commentapp.forms import CommentCreationForm
from django.urls import reverse
from postapp.models import Post
from django.utils.decorators import method_decorator
from commentapp.decorators import comment_ownership_required
# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.post = Post.objects.get(pk=self.request.POST['post_pk'])
        temp_comment.creator = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.post.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.post.pk})
