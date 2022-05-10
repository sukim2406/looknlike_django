from django.urls import path
from likeapp.views import LikePostView

app_name = 'likeapp'

urlpatterns = [
    path('post/like/<int:pk>', LikePostView.as_view(), name='post_like'),
]
