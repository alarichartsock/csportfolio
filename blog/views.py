from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    return render(request, "blog.html")


class BlogHome(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetail(DetailView):
    model = Post
    template_name = "blog_detail.html"
