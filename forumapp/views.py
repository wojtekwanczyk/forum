from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Thread, Post
from .forms import ThreadForm

# Create your views here.


def thread_list(request):
    threads = Thread.objects.order_by('-created_date')
    return render(request, 'forumapp/thread_list.html', {'threads': threads})


def thread_new(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.created_date = timezone.now()
            thread.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'forumapp/thread_new.html', {'form': form})


def thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forumapp/thread.html', {'thread': thread, 'posts': posts})
