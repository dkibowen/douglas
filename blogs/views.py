from django.shortcuts import render,redirect
from .models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect

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
    if request.method =='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=post)
    comments_count = comments.count()
    context = {
        "post":post,
        "comments":comments,
        "comments_count":comments_count
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status="Published")
    context = {
        "blogs":blogs,
        "keyword":keyword,
    }
    return render(request,'search.html',context)