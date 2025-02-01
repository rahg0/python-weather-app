import requests
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display the weather in a formatted way
def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(Fore.GREEN + f"Weather in {city}:")
        print(Fore.CYAN + f"Temperature: {temp}°C")
        print(Fore.YELLOW + f"Condition: {description.capitalize()}")
    else:
        print(Fore.RED + "Error: Unable to fetch weather data. Please check your city name or API key.")

# Main function
if __name__ == "__main__":
    city = input("Enter the city name: ")
    api_key = 'xxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your OpenWeatherMap API key
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)
