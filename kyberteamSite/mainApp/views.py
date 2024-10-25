from django.shortcuts import render


def show_news_page(request):
    return render(request, '../templates/index.html')
# Create your views here.
