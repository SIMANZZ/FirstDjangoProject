from django.shortcuts import render

posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста.',
        'date_posted': '13 мая, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'firstsite/home.html', context)


def about(request):
    return render(request, 'firstsite/about.html', {'title': 'О клубе Python Bytes'})
