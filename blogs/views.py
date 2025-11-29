from django.shortcuts import render,redirect
from .models import Blog, Category

# Create your views here.
def posts_by_category(request,pk):
    posts = Blog.objects.filter(status='Published',category=pk)
    try:
        category = Category.objects.get(pk=pk)
    except: 
        return redirect('home')

    context = {
        "posts":posts,
        "category":category,
    }
    return render(request,'posts_by_category.html',context)

def single_blog(request,slug):
    post = Blog.objects.get(status='Published',slug=slug)
    context = {
        "post":post,
    }
    return render(request,'blogs.html',context)
