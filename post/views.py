from django.shortcuts import render
from django.views.generic import (
CreateView,
UpdateView,
ListView,
DetailView,
DeleteView
)
from hitcount.views import HitCountDetailView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'body', 'photo']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    count_hit = True
    login_url = 'login'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body', 'photo']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostRemoveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_remove.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'post_create_comment.html'
    fields = ['comment']
    login_url = 'login'

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'post_update_comment.html'
    fields = ['comment']
    login_url = 'login'

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        form.instance.post = post
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




