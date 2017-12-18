from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth import login, authenticate

from blog.forms import SignUpForm



def index(request):
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    """
    return render(request, 'blog/index.html')

def examples(request):
    return render(request, 'blog/examples.html', {})

def newUser(request):
    return render(request, 'blog/newUser.html', {})

def discover(request):
    return render(request, 'blog/discover.html', {})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('newUser')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
