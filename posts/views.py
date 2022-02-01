from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Post


# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostsListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'create_post.html'
