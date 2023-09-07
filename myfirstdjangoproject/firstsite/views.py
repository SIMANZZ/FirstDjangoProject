from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'firstsite/home.html', context)


def about(request):
    return render(request, 'firstsite/about.html', {'title': 'О клубе Python Bytes'})
