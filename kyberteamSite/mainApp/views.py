from django.shortcuts import render


def show_news_page(request):
    return render(request, './index.html')
# Create your views here.
def show_match_page(request):
    return render(request, './match_centre.html')

def show_results_page(request):
    return render(request, './results.html')

def show_form_page(request):
    return render(request, './form.html')

def show_about_page(request):
    return render(request, './about.html')

def show_contacts_page(request):
    return render(request, './contacts.html')
