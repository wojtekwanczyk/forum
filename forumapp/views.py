from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.models import User



from .models import Thread, Post, Message
from .forms import ThreadForm, PostForm, UserForm

# Create your views here.


def thread_list(request):
    threads = Thread.objects.order_by('-last_modified')
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
    return render(request, 'forumapp/thread.html', {'thread': thread, 'posts': posts, 'thread_pk': pk})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'forumapp/signup.html', {'form': form})
'''
def login_view(request, user):
    login(request, user)


def logout_view(request):
    logout(request)
'''

def post_new(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.thread = Thread.objects.get(pk=pk)
            post.thread.last_modified = timezone.now()
            post.thread.save()
            post.created_date = timezone.now()
            post.save()
            return redirect('thread', pk=pk)
    else:
        form = PostForm()
    return render(request, 'forumapp/post_new.html', {'form': form})


def delete_post(request, pk, th_pk):
    Post.objects.get(pk=pk).delete()
    return redirect('thread', pk=th_pk)


def delete_thread(request, pk):
    Thread.objects.get(pk=pk).delete()
    return redirect('/')


def user(request, pk):
    user1 = User.objects.get(pk=pk)
    messages = Message.objects.filter(to_user=user1)
    return render(request, 'forumapp/user.html', {'user1': user1, 'messages': messages})


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user', pk=pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'forumapp/user_edit.html', {'form': form})