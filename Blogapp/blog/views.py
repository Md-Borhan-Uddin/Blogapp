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



def single(request, id):
    post =  Post.objects.get(id=id)
    author = Author.objects.get(id=post.post_author.id)
    category = Category.objects.get(name=post.post_category)
    related_cat = Post.objects.filter(post_category=category)
    top_posts = Post.objects.filter(post_author=author)[:2]
    context = {
        'post':post,
        'top_posts':top_posts,
        'cats':related_cat,
        'category':category
    }
    return render(request, 'blog/single.html', context)


def author(request):
    return render(request, 'blog/author.html')

def category(request):
    return render(request, 'blog/category.html')

def login(request):
    return render(request, 'blog/login.html')