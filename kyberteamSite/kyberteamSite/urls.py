"""
URL configuration for kyberteamSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_news_page, name="NewsPage"),
    path('match_centre/', views.show_match_page, name="MatchCentrePage"),
    path('results/', views.show_results_page, name="ResultsPAge"),
    path('form/', views.show_form_page, name="FormPage"),
    path('about/', views.show_about_page, name="AboutPage"),
    path('contacts/', views.show_contacts_page, name="ContactsPage"),
]
