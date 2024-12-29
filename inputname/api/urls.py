from django.urls import path
from .views import create_title, get_titles, title_details

urlpatterns = [
    path('titles/', get_titles, name='get_titles'),
    path('titles/create', create_title, name='create_title'),
    path('titles/<int:pk>', title_details, name='title_details')
]
