import requests

def get_address_from_coordinates(latitude, longitude, api_key):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        results = response.json()
        if results['status'] == 'OK':
            address = results['results'][0]['formatted_address']
            return address
        else:
            return f"Error: {results['status']}"
    else:
        return "Error: Unable to fetch the address"

# Example usage:
api_key = "AIzaSyCgfsuJW7hN4Z4uklF3TWqbdxizLA17DaA"

# List of coordinates as (latitude, longitude) pairs that the script will look up adresses for 
coordinates_list = [
        (33.7804036, -118.0009846),
        (33.8968684, -117.9207581),
        (33.6736658, -117.9052314),
        (33.7253784, -117.951292),
        (33.8000648, -117.9947016),
        (33.7004843, -118.0033368),
        (33.8486569, -118.0601521),
        (33.6836103, -117.8544035),
        (33.8197637, -117.8535794),
        (33.6996835, -118.0049837),
        (33.714247, -117.8028181),
        (33.6752051, -117.7407189),
        (33.6731561, -117.7391977),
        (33.7136349, -117.9250483),
        (33.7641383, -117.9663724),
        (33.672152, -117.9098818),
        (33.6745412, -117.7398831),
        (33.8348083, -118.0786819),
        (33.6741496, -117.8896973),
        (33.7943103, -117.8508151)

    # Add more coordinate pairs as needed
]
#Loop through each coordinate and print their address 
for latitude, longitude in coordinates_list:
    address = get_address_from_coordinates(latitude, longitude, api_key)
    print(f"The address for coordinates ({latitude}, {longitude}) is: {address}")