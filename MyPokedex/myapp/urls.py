from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.index, name="index"),
    path('search_pokemon/', views.search_pokemon, name="search"),
    path('previous/<int:id>/', views.previous_pokemon, name='previous_pokemon'),
    path('next/<int:id>/', views.next_pokemon, name='next_pokemon'),
    path('team/', views.team, name='team'),
    path('add/<int:id>/', views.add_team, name="add_team"),
    path('remove/<int:key>/', views.remove_team, name="remove_team"),
]