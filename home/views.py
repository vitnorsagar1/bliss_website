from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about_view(request):
    return render(request, 'home/about.html')

def services_view(request):
    return render(request, 'home/services.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def careers_view(request):
    return render(request, 'home/careers.html')

def blog_view(request):
    return render(request, 'home/blog.html')
