from typing import List
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from projectapp.models import Project
from projectapp.forms import ProjectCreationForm
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from postapp.models import Post
from subscriptionapp.models import Subscription

# Create your views here.

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    context_object_name = 'target_project'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.creator = self.request.user
        temp_project.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk}) 


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    template_name = 'projectapp/detail.html'
    context_object_name = 'target_project'
    paginated_by = 25
 
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)

        object_list = Post.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)
