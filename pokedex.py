import requests
from ascii_art import POKEDEX_ASCII
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
    print("\n")
    pass


def display_main_menu() -> str:
    print(POKEDEX_ASCII)
    print("Welcome to the Pokedex! Please select an option using the numbers:")
    print("\n")
    print("1. Look up Pokémon")
    print("2. Exit \n")
    user_response = input("Enter your choice: ").strip()
    return user_response

def display_pokemon_submenu() -> str:
    print("1. Look up another Pokémon")
    print("2. Return to main menu")
    print("\n")
    user_response = input("Enter your choice: ").strip()
    return user_response

def fetch_and_display_pokemon():
    pokemon_name = input("Enter Pokémon name: ")
    print("\n")
    response = fetch_pokemon_data(pokemon_name)
    if response:
        processed_data = process_pokemon_data(response)
        if processed_data:
            display_pokemon_data(processed_data)
        else:
            print("Error processing Pokémon data.")
    else: 
        print("Failed to fetch Pokémon data.")

def main():
    while True:
        user_choice = display_main_menu()
        if user_choice == '1':
            fetch_and_display_pokemon()
            while True:
                submenu_choice = display_pokemon_submenu()
                if submenu_choice == '1':
                    fetch_and_display_pokemon()
                elif submenu_choice == '2':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif user_choice == '2':
            print("Thank you for using the Pokédex. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        

            
if __name__ == "__main__":
    main()
