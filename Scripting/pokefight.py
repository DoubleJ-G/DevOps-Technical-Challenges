import sys
import requests


def fetch_pokemon(name):
    url = "http://pokeapi.co/api/v2/pokemon/" + name
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Unexpected error with PokeAPI:\n" + str(e))
        sys.exit(1)


def get_stats(pokemon_data):
    stats = pokemon_data["stats"]
    return stats


def get_attack_stat(stats):
    for stat in stats:
        if stat["stat"]["name"] == "attack":
            return stat["base_stat"]


def get_pokemon_or_exit(name):
    pokemon_data = fetch_pokemon(name)
    if pokemon_data is None:
        print("Pokemon: " + name + " was not found")
        sys.exit(1)
    return pokemon_data


# Check two arguments were provided
if len(sys.argv) != 3:
    print("Usage: pokefight.py <pokemon1> <pokemon2>")
    sys.exit(1)

name1 = sys.argv[1].lower()
name2 = sys.argv[2].lower()

pokemon1 = get_pokemon_or_exit(name1)
pokemon2 = get_pokemon_or_exit(name2)

stats1 = get_stats(pokemon1)
stats2 = get_stats(pokemon2)

attack1 = get_attack_stat(stats1)
attack2 = get_attack_stat(stats2)

print(name1 + " (" + str(attack1) + ") vs " +
      name2 + " (" + str(attack2) + ")")

if attack1 > attack2:
    print(name1 + " wins!")
elif attack1 < attack2:
    print(name2 + " wins!")
else:
    print("It's a tie!")
