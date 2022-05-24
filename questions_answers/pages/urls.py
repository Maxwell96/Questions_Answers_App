from django.urls import path
from .views import landingpage

urlpatterns = [
    path('', landingpage, name='landing_page'),
]