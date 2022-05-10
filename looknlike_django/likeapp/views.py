from xml.dom import ValidationErr
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from postapp.models import Post
from likeapp.models import LikeRecord
from django.contrib import messages
from django.db import transaction

# Create your views here.

@transaction.atomic
def db_transaction(user, post):

    post.like += 1
    post.save()

    if LikeRecord.objects.filter(user=user, post=post).exists():
        raise ValidationError('Like already exists')
    else :
        LikeRecord(user=user, post=post).save()

@method_decorator(login_required, 'get')
class LikePostView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('postapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        user = self.request.user
        post = get_object_or_404(Post, pk=kwargs['pk'])

        try:
            db_transaction(user, post)
            messages.add_message(self.request, messages.SUCCESS, 'Post liked')
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, 'Already liked this post')
            return HttpResponseRedirect(reverse('postapp:detail', kwargs={'pk': kwargs['pk']}))

        return super(LikePostView, self).get(self.request, *args, **kwargs)