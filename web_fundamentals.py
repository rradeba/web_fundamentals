import requests 
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text 

pikachu_data = json.loads(json_data)

print(pikachu_data["name"])


abilities  = pikachu_data['abilities']


for ability in abilities: 
    ability_name = ability['ability']['name']
    print(f"* {ability_name}")





def fetch_pokemon_data(pokemon_names):
    for name in pokemon_names: 
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        json_data = response.text 
        pok_data = json.loads(json_data)
        weight  = pok_data['weight']
        print(f"\nName: {name} - {weight} Hectares")




def calculate_average_weight(pokemon_names):
    weights_list = []
    
    for name in pokemon_names: 
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        json_data = response.text 
        pok_data = json.loads(json_data)
        weight = pok_data['weight']
        weights_list.append(weight)
    
    if not weights_list:
        print("No weights to calculate.")
        return
    
    total_sum = sum(weights_list)
    count = len(weights_list)
    average = total_sum / count
    rounded_average = round(average, 1)
    
    print(f"\nThe average weight is: {rounded_average} Hectograms")

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

fetch_pokemon_data(pokemon_names)

calculate_average_weight(pokemon_names)