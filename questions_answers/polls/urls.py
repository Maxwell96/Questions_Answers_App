from xml.dom.minidom import NamedNodeMap
from django.urls import path
from .views import index, detail, results, vote

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/results', results, name='results'),
    path('<int:pk>/vote', vote, name='vote')
]