from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def my_project(request):
    return render(request, 'portfolio/project_list.html')

def fashion_mart_details(request):
    return render(request, 'portfolio/fashionmart_details.html')

def blog_detail(request):
    return render(request, 'portfolio/blog_details.html')

def note_details(request):
    return render(request, 'portfolio/note_details.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

from .models import Blog
def explore_blog(request):
    blogs = Blog.objects.all()

    return render(request, 'portfolio/explore_blog.html', {'blogs':blogs})

def blog_details(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'portfolio/blogP_details.html', {'blog':blog})

