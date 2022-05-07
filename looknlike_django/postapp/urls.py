from django.urls import path
from django.views.generic import TemplateView

app_name = 'postapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='postapp/list.html'), name='list'),
]