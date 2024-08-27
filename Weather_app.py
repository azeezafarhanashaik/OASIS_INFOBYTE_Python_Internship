import requests

def get_weather_data(location, api_key):
    # API endpoint for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q=hyderabad&appid=9cfeb474614e6054f523937fc95332c4&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def display_weather_info(weather_data):
    if weather_data:
        city = weather_data.get("name")
        country = weather_data.get("sys", {}).get("country")
        temperature = weather_data.get("main", {}).get("temp")
        humidity = weather_data.get("main", {}).get("humidity")
        weather_description = weather_data.get("weather", [])[0].get("description")

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Could not retrieve weather data. Please check the location or try again later.")

def main():
    api_key = '9cfeb474614e6054f523937fc95332c4'

    location = input("Enter the city name or ZIP code: ")
    weather_data = get_weather_data(location, api_key)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
