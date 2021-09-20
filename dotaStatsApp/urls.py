from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('hero_suggestion', views.hero_suggestion, name='hero_suggestion'),
    # path('hero_suggestion_produce/', views.hero_suggestion_produce, name='hero_suggestion_produce'),
    path('<str:dname>/', views.hero_detailed, name='hero_detailed'),
]
