from django.shortcuts import render
from .models import Posts
from django.contrib.auth.decorators import login_required
from .forms import PostsForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_home(request):
    posts = Posts.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def blog_detail(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'post': post})
