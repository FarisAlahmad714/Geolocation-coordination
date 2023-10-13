#HTTP library for making requests to web servers.
import requests

# interact with Google Places API:Places to fetch information about indoor soccer places in Orange County.
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
params = {
    'query': 'indoor soccer in Orange County',
    'key': 'AIzaSyCgfsuJW7hN4Z4uklF3TWqbdxizLA17DaA'
}
# Send a GET request to the API & A GET request is made to the Google Places API using the URL and parameters.
#The API response is converted from a JSON string into a Python dictionary and stored in data.
response = requests.get(url, params=params)

data = response.json()

# Extract and print the name and coordinates of each park
for place in data['results']:
    name = place['name']
    latitude = place['geometry']['location']['lat']
    longitude = place['geometry']['location']['lng']
    print(f"Latitude: {latitude} ,Longitude: {longitude}")

    # print(f"Park Name: {name}\nLatitude: {latitude}\nLongitude: {longitude}\n")