from django.shortcuts import render


def show_news_page(request):
    context = {
        "firstNewCard": {
            "tittle": "Идёт подготовка к турниру",
            "imageURL": "https://cybersport.metaratings.ru/_images/insecure/w-680:h-512/bG9jYWw6Ly8vdXBsb2FkL3NwcmludC5lZGl0b3IvMWRiLzFkYmRlN2RiNzg5MmE5OWU4Mjg0NGZjNzc5YjFkNzdhLmpwZw==.webp",
            "GameName": "DOTA 2",
            "NewDate": "22.1111.2024",
        },
        "news_cards": [
            {
                "tittle": "Баба сеня обосрался, турнир отменяется",
                "imageURL": "https://rg.ru/uploads/images/2023/10/05/kybersport_60c.jpg",
                "gameName": "Standoff2",
                "date": "1991.21.12"
            },

        ],
    }
    return render(request, './index.html', context)
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
