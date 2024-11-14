from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def my_project(request):
    return render(request, 'portfolio/project_list.html')

def fashion_mart_details(request):
    return render(request, 'portfolio/fashionmart_details.html')

def blog_details(request):
    return render(request, 'portfolio/blog_details.html')

def note_details(request):
    return render(request, 'portfolio/note_details.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

