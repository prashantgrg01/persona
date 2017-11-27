from django.shortcuts import render, redirect
from .models import Post
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("-post_date")
    return render(request, "blog/post_list.html", {"page":"blog", "posts": posts})

def post_detail(request, post_id):
    post = get_post(post_id)
    if post == None:
        return render(request, "404.html")
    return render(request, "blog/post_detail.html", {"page":"blog", "post": post})

def get_post(post_id):
    try:
        return Post.objects.get(id=post_id)
    except ObjectDoesNotExist:
        return None

def page_not_found(request):
    return render(request, "404.html")