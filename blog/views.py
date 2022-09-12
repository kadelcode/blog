from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model= Post
    template_name= 'blog/post_detail.html'

class PostCreateView(CreateView):
    model= Post
    template_name = 'blog/post_new.html'
    fields= "__all__"

class PostUpdateView(UpdateView):
    model= Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model= Post
    template_name = 'blog/post_delete.html'
    success_url= reverse_lazy('posts')