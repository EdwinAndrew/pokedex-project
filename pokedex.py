import requests
from typing import Optional, Dict

pokeBaseURL = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(pokemonName: str) -> Optional[dict]:
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
        

def main():
    pokemonName = input("Enter a pokemon name to return data on: ")
    result = fetch_pokemon_data(pokemonName)
    if result:
        print(f"Data for {pokemonName}:")
        print(result)
    else:
        print("Failed to fetch Pokemon data")


if __name__ == "__main__":
    main()
