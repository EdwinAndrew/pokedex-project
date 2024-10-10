import requests
from typing import Optional

pokeBaseURL = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(pokemonName: str) -> Optional[dict]:
    pokemonName = pokemonName.lower()
    pokemonEndpoint = pokeBaseURL + f"pokemon/{pokemonName}"
    try:
        response = requests.get(pokemonEndpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("Pokemon not found")
        else:
            print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except ValueError as e:
        print(f"JSON decoding error: {e}")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
    
    
    return None


def process_pokemon_data(json_data: dict) -> dict:
    if not json_data:
        return None
    
    return {
        "name": json_data.get('name', 'Unknown'),
        "id": json_data.get('id', 'Unknown'),
        "height": json_data.get('height', 'Unknown'),
        "weight": json_data.get('weight', 'Unknown'),
        "types": [t['type']['name'] for t in json_data.get('types', [])],
        "abilities": [a['ability']['name'] for a in json_data.get('abilities', [])]
    }

def display_pokemon_data(pokemon_data: dict) -> None:

    print(f"Name: {pokemon_data['name'].capitalize()}")
    print(f"ID: {pokemon_data['id']}")
    print(f"Height: {pokemon_data['height']} dm")
    print(f"Weight: {pokemon_data['weight']} hg")
    print(f"Types: {', '.join(pokemon_data['types'])}")
    print(f"Abilities: {', '.join(pokemon_data['abilities'])}")
    pass


def display_main_menu() -> str:
    print("Welcome to the Pokedex! Please select an option using the numbers:")
    print("1. Look up Pokémon")
    print("2. Exit")
    user_response = input("Enter your choice: ").strip()
    return user_response

def display_pokemon_submenu() -> str:
    print("1. Look up another Pokémon")
    print("2. Return to main menu")
    user_response = input("Enter your choice: ").strip()
    return user_response

def main():
    while True:
        user_choice = display_main_menu() 
        if user_choice == '1':
            pokemon_name = input("Enter Pokémon name: ")
            response = fetch_pokemon_data(pokemon_name)
            processed_data = process_pokemon_data(response)
            display_pokemon_data(processed_data)
            pass
        elif user_choice == '2':
            break

            




if __name__ == "__main__":
    main()
