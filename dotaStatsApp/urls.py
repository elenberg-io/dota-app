from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('<int:hero_id>/', views.hero_detailed, name='hero_detailed')
]
