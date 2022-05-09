from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from postapp.forms import PostCreationForm, PostUpdateForm
from postapp.models import Post
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from postapp.decorators import post_ownership_required
from django.views.generic.edit import FormMixin
from commentapp.forms import CommentCreationForm
# Create your views here.


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'
    context_object_name = 'target_post'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.creator = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentCreationForm
    template_name = 'postapp/detail.html'
    context_object_name = 'target_post'


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'postapp/update.html'
    context_object_name = 'target_post'

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'postapp/delete.html'
    success_url = reverse_lazy('postapp:list')


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'postapp/list.html'
    paginate_by= 10