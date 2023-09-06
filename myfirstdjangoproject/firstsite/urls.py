from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='firstsite-home'),
    path('about/', views.about, name='firstsite-about'),
]
