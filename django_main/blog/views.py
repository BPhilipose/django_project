from django.shortcuts import render
from .models import Post

#Manually inputed dummy data from post class. 
"""
posts = [
    {
        'author': 'Benson P',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 2020'
    }
]
"""

def home(request):
    context = {
        'posts': Post.objects.all() #changed to input data from included database
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

