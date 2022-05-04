import imp
import re
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from blog.forms import FeedBackForm
from django.contrib import messages

from blog.forms import PostForm
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html', {})


def contacts(request):
    form = FeedBackForm()
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                messages.add_message(
                    request, messages.ERROR, "Ваш прошлый запрос еще не обработан")
                messages.add_message(
                    request, messages.ERROR, "Попробуйте позже")

            return redirect(reverse("contacts"))

    context = {
        "feedback_form": form,
        "address": "200 N. Spring Street Los Angeles CA 90012 United States",
        "phone": "+1(800) 000-00-00",
        "email": "support@blog.com"
    }
    return render(request, 'blog/contacts.html', context)
