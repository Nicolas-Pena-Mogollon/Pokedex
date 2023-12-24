"""
views.py - Defines views for the Pokedex application.

This file contains view functions for different pages in the Pokedex application.
Each view corresponds to a specific URL pattern defined in urls.py.

Views:
1. list_pokemon(request): Display a paginated list of Pokémon.
2. list_pokemon_weight_range(request): Display a paginated list of Pokémon within a specified weight range.
3. list_grass_type_pokemon(request): Display a paginated list of Grass-type Pokémon.
4. flying_height_gt_10(request): Display a paginated list of Flying-type Pokémon with height greater than 10.
5. reverse_names(request): Display a paginated list of Pokémon names with reversed names.

"""

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from pokedex_app.graphql_utils.api_queries import get_pokemon_list, get_pokemon_name_list
from pokedex_app.graphql_utils.graphql_queries import LIST_50_QUERY, LIST_BTW_30_80_QUERY, LIST_GRASS_TYPE_QUERY, \
    LIST_FLYING_TYPE_MIN10HEIGHT_QUERY, LIST_NAMES_QUERY


def list_pokemon(request):
    """
    Display a paginated list of Pokémon.

    This view retrieves a list of Pokémon from the GraphQL API and displays them in a paginated manner.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML template displaying a paginated list of Pokémon.
    """
    poke_list = get_pokemon_list(LIST_50_QUERY)
    paginator = Paginator(poke_list, 10)
    page = request.GET.get('page')
    try:
        paginated_pokemon_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_pokemon_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_pokemon_list = paginator.page(paginator.num_pages)

    return render(request, 'pokedex_app/pokemon_list.html', {'list_pokemon': paginated_pokemon_list})


def list_pokemon_weight_range(request):
    """
    Display a paginated list of Pokémon within a specified weight range.

    This view retrieves a list of Pokémon within a specified weight range from the GraphQL API and displays them
    in a paginated manner.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML template displaying a paginated list of Pokémon within a specified weight range.
    """
    # Intentar obtener la lista de Pokémon desde la caché
    filtered_pokemon = get_pokemon_list(LIST_BTW_30_80_QUERY)
    paginator = Paginator(filtered_pokemon, 10)
    page = request.GET.get('page')
    try:
        paginated_filtered_pokemon = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_filtered_pokemon = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_filtered_pokemon = paginator.page(paginator.num_pages)

    return render(request, 'pokedex_app/pokemon_weight.html', {'filtered_pokemon': paginated_filtered_pokemon})


def list_grass_type_pokemon(request):
    """
    Display a paginated list of Grass-type Pokémon.

    This view retrieves a list of Grass-type Pokémon from the GraphQL API and displays them in a paginated manner.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML template displaying a paginated list of Grass-type Pokémon.
    """
    grass_pokemon = get_pokemon_list(LIST_GRASS_TYPE_QUERY)

    paginator = Paginator(grass_pokemon, 10)
    page = request.GET.get('page')

    try:
        paginated_pokemon_grass = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_pokemon_grass = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_pokemon_grass = paginator.page(paginator.num_pages)

    return render(request, 'pokedex_app/pokemon_grass.html', {'pokemon_grass': paginated_pokemon_grass})


def flying_height_gt_10(request):
    """
    Display a paginated list of Flying-type Pokémon with height greater than 10.

    This view retrieves a list of Flying-type Pokémon with height greater than 10 from the GraphQL API and displays them
    in a paginated manner.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML template displaying a paginated list of Flying-type Pokémon with height greater than 10.
    """
    flying_pokemon = get_pokemon_list(LIST_FLYING_TYPE_MIN10HEIGHT_QUERY)
    paginator = Paginator(flying_pokemon, 10)
    page = request.GET.get('page')

    try:
        paginated_flying_pokemon = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_flying_pokemon = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_flying_pokemon = paginator.page(paginator.num_pages)

    return render(request, 'pokedex_app/pokemon_flying_ht10.html', {'flying_pokemon': paginated_flying_pokemon})


def reverse_names(request):
    """
    Display a paginated list of Pokémon names with reversed names.

    This view retrieves a list of Pokémon names from the GraphQL API, reverses the names, and displays them in a paginated manner.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML template displaying a paginated list of Pokémon names with reversed names.
    """
    pokemon_name_list = get_pokemon_name_list(LIST_NAMES_QUERY)

    # Get reversed names
    reversed_pokemones = [{'id': pokemon['id'], 'name': pokemon['name'], 'reverse_name': pokemon['name'][::-1]} for
                          pokemon in pokemon_name_list]

    paginator = Paginator(reversed_pokemones, 10)
    page = request.GET.get('page')
    try:
        paginated_reversed_pokemones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_reversed_pokemones = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_reversed_pokemones = paginator.page(paginator.num_pages)

    return render(request, 'pokedex_app/pokemon_reversed_names.html', {
        'reversed_pokemones': paginated_reversed_pokemones,
    })
