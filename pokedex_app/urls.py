"""
urls.py - URL patterns for the Pokedex application.

This file defines the URL patterns for different views in the Pokedex application.

URL Patterns:
- /: Display a list of Pokemon.
- /weight/: Display a list of Pokemon within a specified weight range.
- /grass/: Display a list of Grass-type Pokemon.
- /flying/: Display a list of Flying-type Pokemon with height greater than 10.
- /reverse/: Display a list of Pokemon names with reversed names.

"""

from django.urls import path

from .views import list_pokemon_weight_range, list_grass_type_pokemon, flying_height_gt_10, reverse_names, list_pokemon

urlpatterns = [
    path('', list_pokemon, name='pokemon_list'),
    path('weight/', list_pokemon_weight_range, name='pokemon_weight_range'),
    path('grass/', list_grass_type_pokemon, name='grass_type'),
    path('flying/', flying_height_gt_10, name='flying_height_gt_10'),
    path('reverse/', reverse_names, name='reverse_names'),
]