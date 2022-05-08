from postapp.models import Post
from django.http import HttpResponseForbidden

def post_ownership_required(func):
    def decorated(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if not post.creator == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated