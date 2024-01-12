import requests
from .models import *

def get_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(id)
    response = requests.get(url)
    pokemon_data = response.json()

    specie = get_pokemon_specie(pokemon_data['species']['url'])
    description_list = specie['flavor_text_entries']
    description = get_pokemon_description(description_list)

    pokemon = Pokemon.__new__(Pokemon)

    pokemon.name = pokemon_data['name']
    pokemon.id_pokemon = pokemon_data['id']
    if pokemon.id_pokemon >= 650:
        pokemon.img = pokemon_data['sprites']['other']['official-artwork']['front_default']
    else:
        pokemon.img = pokemon_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
    pokemon.types = pokemon_data['types']
    pokemon.weight = pokemon_data['weight']
    pokemon.height = pokemon_data['height']
    pokemon.description = description
    return pokemon


def get_pokemon_specie(url_specie: str) -> dict:
    response = requests.get(url_specie)
    specie = response.json()
    return specie


def get_pokemon_description(list_of_descriptions: list) -> str:
    for description in list_of_descriptions:
        if description['language']['name'] == 'en':
            pokemon_description = description['flavor_text']
            break

    pokemon_description = pokemon_description.replace('\n', ' ')
    pokemon_description = pokemon_description.replace('\f', ' ')
    pokemon_description = pokemon_description.replace('POKéMON', 'pokemon')
    return pokemon_description