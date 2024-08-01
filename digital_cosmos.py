
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets  = response.json()['bodies']
    return planets 

def print_planet_data(planets): 
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            massValue = planet['mass']['massValue']
            massExponent = planet['mass']['massExponent']
            orbit_period = planets['Orbit Period']
            mass = str(f"{massValue} * 10^{massExponent}")
            print(f"\nPlanet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    
       
def find_heaviest_planet(planets):   
    heaviest_planet_name  = None
    greatest_mass = 0
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            massValue = planet['mass']['massValue']
            massExponent = planet['mass']['massExponent']
            mass = massValue * (10 ** massExponent)
            
            if mass > greatest_mass:
                greatest_mass = mass
                heaviest_planet_name = planet

    if heaviest_planet_name:
        name = heaviest_planet_name['englishName']
        mass = f"{heaviest_planet_name['mass']['massValue']} * 10^{heaviest_planet_name['mass']['massExponent']}"
        orbit_period = heaviest_planet_name['sideralOrbit']
        print(f"\nPlanet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
        return name, mass
    else:
        return None, None
    

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with mass of {mass} kg.")


fetch_planet_data()
