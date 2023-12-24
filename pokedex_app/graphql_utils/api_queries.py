"""
Function module to get Pokémon lists from the GraphQL API.

This module provides functions to query the Pokémon GraphQL API
and get Pokémon lists based on specific queries.

Example:
     from pokemon_api_functions import get_pokemon_list, get_pokemon_name_list

     # Get the list of Pokémon with detailed information
     pokemon_list = get_pokemon_list(LIST_50_QUERY)

     # Get list of Pokémon names
     pokemon_names = get_pokemon_name_list(LIST_NAMES_QUERY)
"""

from django.conf import settings
import requests

"""
Get a list of Pokémon with detailed information.

"""
def get_pokemon_list(graphql_query):
    """
    Get a list of Pokémon with detailed information.

    Args:
        graphql_query (str): The GraphQL query to get the list.

    Returns:
        list: A list of dictionaries representing Pokémon with detailed information.
    """
    # Configure GraphQL request
    graphql_data = {'query': graphql_query}
    headers = {'Content-Type': 'application/json'}

    # Send GraphQL request
    response = requests.post(settings.POKEMON_API_URL, json=graphql_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Get the Pokémon list
        pokemon_list = data.get('data', {}).get('pokemon_list', [])
        # Adjust type structure
        for pokemon in pokemon_list:
            pokemon['types'] = [type_info['pokemon_v2_type']['name'] for type_info in pokemon.get('types', [])]
        return pokemon_list

    return []


def get_pokemon_name_list(graphql_query):
    """
    Get a list of Pokémon names.

    Args:
        graphql_query (str): The GraphQL query to get the namelist.

    Returns:
        list: A list of Pokémon names.
    """
    graphql_data = {'query': graphql_query}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(settings.POKEMON_API_URL, json=graphql_data, headers=headers)

    pokemon_list = []
    if response.status_code == 200:
        data = response.json()
        pokemon_list = data.get('data', {}).get('pokemon_name_list', [])

    return pokemon_list
