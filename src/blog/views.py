from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Blog
from django.contrib import messages

from django.urls import reverse

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blog = Blog.objects.all()[:3]
    context = {
        'blogs': blog,
    }
    return render(request, 'blog/index.html', context=context)

def author_list(request):
    author = Author.objects.all()
    context = {
        'authors': author,
    }
    return render(request, 'blog/author_list.html', context=context)

def author_detail(request, author_id):
    detail = get_object_or_404(Author, id=author_id)
    context = {
        'details': detail,
    }
    return render(request, 'blog/author_detail.html', context=context)

def blog_list(request):
    # blog = Blog.objects.all()

    p = Paginator(Blog.objects.all(), 3)
    page = request.GET.get('page')
    blog_page = p.get_page(page)

    context = {
        # 'blogs': blog,
        'blog_pages': blog_page,
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_detail(request, blog_id):
    detail = get_object_or_404(Blog, id=blog_id)
    context = {
        'details': detail,
    }
    return render(request, 'blog/detail.html', context=context)

def add_blog(request):

    author = Author.objects.all()
    context = {
        'authors': author,
    }
    
    if request.method == "POST":
        data = {
            'title': request.POST.get('title'),
            'author_id': request.POST.get('author_id'),
            'content': request.POST.get('content')
        }

        # print(data)

        empty_fields = None
        for k in data.keys():
            if not data[k]:
                empty_fields = True

        if not empty_fields:
            Blog.objects.create(**data)
            return redirect('blog:index')
        else:
            return render(request, 'blog/add_blog.html', context=context)
        
    return render(request, 'blog/add_blog.html', context=context)

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    author = Author.objects.all()

    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'author_id': request.POST.get('author_id'),
            'content': request.POST.get('content')
        }

        # print(data)

        empty_fields = None
        for k in data.keys():
            if not data[k]:
                empty_fields = True

            blog.__dict__.update(data)
            blog.save()

        return redirect('blog:blog-list')

    context = {
        'blogs': blog,
        'authors': author,
    }
    return render(request, 'blog/update_blog.html', context=context)

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    
    # Add a message to the messages framework
    messages.success(request, 'Successfully Deleted')

    return redirect(reverse('blog:blog-list'))
