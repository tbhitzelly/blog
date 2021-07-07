from django.views.generic import ListView, DetailView
from .models import Post


class HomeViews(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class HomeDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
    

