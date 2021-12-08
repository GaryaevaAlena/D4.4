from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name = 'news/post_list.html'
    queryset = Post.objects.all().order_by('-pk')
    paginate_by = 10



class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'
    queryset = Author.objects.all()

class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()

class Search(ListView):
    model = Post
    context_object_name = 'Search'
    template_name = 'news/search.html'
    queryset = Post.objects.all().order_by('-dateCreation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context

class Add(CreateView):
    model = Post
    template_name = 'news/Add.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

class Edit(UpdateView):

    template_name = 'news/Add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class Delete(DeleteView):
    model = Post
    template_name = 'news/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

