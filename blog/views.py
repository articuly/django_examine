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


@login_required
def blog_post(request):
    if request.method == "GET":
        form = PostsForm()
        return render(request, 'blog/post.html', {'form': form})
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
            except Exception as e:
                print(str(e))
            else:
                return HttpResponseRedirect('/blog/')
