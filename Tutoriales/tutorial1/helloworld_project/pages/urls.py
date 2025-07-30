from django.urls import path
from .views import HomePageView  # Importar la clase

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]