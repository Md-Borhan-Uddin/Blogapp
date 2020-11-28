from django.shortcuts import render
from .models import Post, Category, Author
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')



def single(request):
    return render(request, 'blog/single.html')


def login(request):
    return render(request, 'blog/login.html')