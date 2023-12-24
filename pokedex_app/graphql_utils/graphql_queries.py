"""
Predefined GraphQL queries for obtaining lists of Pokémon.

This module contains predefined GraphQL queries that can be used
to obtain lists of Pokémon based on specific criteria.
"""

LIST_50_QUERY = '''
query {
  pokemon_list: pokemon_v2_pokemon(limit: 50) {
    id
    name
    types: pokemon_v2_pokemontypes {
      pokemon_v2_type {
        name
      }
    }
    height
    weight
  }
}
'''

LIST_BTW_30_80_QUERY = '''
query {
  pokemon_list: pokemon_v2_pokemon(where: { weight: { _gt: 30, _lt: 80 } }) {
    id
    name
    types: pokemon_v2_pokemontypes {
      pokemon_v2_type {
        name
      }
    }
    height
    weight
  }
}
'''

LIST_GRASS_TYPE_QUERY = '''
query {
  pokemon_list: pokemon_v2_pokemon(where: { pokemon_v2_pokemontypes: { pokemon_v2_type: { name: { _eq: "grass" } } } }) {
    id
    name
    types: pokemon_v2_pokemontypes {
      pokemon_v2_type {
        name
      }
    }
    height
    weight
  }
}
'''

LIST_FLYING_TYPE_MIN10HEIGHT_QUERY = '''
query {
  pokemon_list: pokemon_v2_pokemon(
    where: {
      pokemon_v2_pokemontypes: {
        pokemon_v2_type: { name: { _eq: "flying" } }
      },
      height: { _gt: 10 }
    }
  ) {
    id
    name
    types: pokemon_v2_pokemontypes {
      pokemon_v2_type {
        name
      }
    }
    height
    weight
  }
}
'''

LIST_NAMES_QUERY = '''
query {
  pokemon_name_list: pokemon_v2_pokemon {
    id
    name
  }
}
'''
