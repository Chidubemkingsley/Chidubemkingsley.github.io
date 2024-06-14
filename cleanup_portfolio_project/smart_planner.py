# Import necessary libraries
import requests  # Library to handle HTTP requests
import json  # Library to handle JSON data

# Function to get routes from Google Maps API
def get_routes(start_location, end_location):
    """
    Fetches potential routes from Google Maps API between the start and end locations.

    Parameters:
    start_location (str): Starting point in the format 'latitude,longitude'
    end_location (str): Ending point in the format 'latitude,longitude'

    Returns:
    list: A list of routes with their respective segments
    """
    # Define API endpoint and parameters
    api_endpoint = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': start_location,
        'destination': end_location,
        'key': 'YOUR_API_KEY'
    }

    # Make an HTTP GET request to the API
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract routes
        routes = data.get('routes', [])
        return routes
    else:
        # Log error if request failed
        print(f"Error fetching routes: {response.status_code}")
        return []

# Function to get elevation data for a route
def get_elevation(route):
    """
    Fetches elevation data for a given route from Google Elevation API.

    Parameters:
    route (list): A list of lat/lng points representing the route

    Returns:
    list: A list of elevation data points
    """
    # Define API endpoint and parameters
    api_endpoint = "https://maps.googleapis.com/maps/api/elevation/json"
    params = {
        'locations': '|'.join([f"{point['lat']},{point['lng']}" for point in route]),
        'key': 'YOUR_API_KEY'
    }

    # Make an HTTP GET request to the API
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract elevation data
        elevation_data = data.get('results', [])
        return elevation_data
    else:
        # Log error if request failed
        print(f"Error fetching elevation data: {response.status_code}")
        return []

# Example usage
if __name__ == "__main__":
    # Define start and end locations
    start = "37.7749,-122.4194"  # San Francisco, CA
    end = "34.0522,-118.2437"  # Los Angeles, CA
    
    # Get routes between the locations
    routes = get_routes(start, end)
    if routes:
        # Select the first route for simplicity
        first_route = routes[0]['legs'][0]['steps']
        # Get elevation data for the first route
        elevation_data = get_elevation(first_route)
        # Print the elevation data
        print(elevation_data)
    else:
        print("No routes found.")

