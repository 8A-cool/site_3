from django.shortcuts import render


def show_news_page(request):
    return render(request, './index.html')
# Create your views here.
def show_match_page(request):
    return render(request, './match_centre.html')

def show_results_page(request):
    return render(request, './results.html')