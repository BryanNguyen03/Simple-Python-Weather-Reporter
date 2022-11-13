import requests
import datetime as dt

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#Insert your API Key
API_KEY = ''


def kelvinToCelsius(temp_kelvin):
    '''
    Converts temperature in Kelvin to Celsius
    Parameters:
    temp_kelvin: the temperature in Kelvin

    Returns:
    The temperature in celsius
    '''
    return temp_kelvin - 273.15


def kelvinToFahrenheit(temp_kelvin):
    '''
    Converts temperature in Kelvin to Fahrenheit
    Parameters:
    temp_kelvin (int): the temperature in Kelvin

    Returns:
    The temperature in fahrenheit
    '''
    return kelvinToCelsius(temp_kelvin) * (9/5) + 32

def printWeatherLog(city):
    '''
    Prints the weather forecast
    Parameters:
    city (string): the name of the city
    '''

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    temp = response['main']['temp']
    #temp in celcius and fahrenheit
    temp_celsius = kelvinToCelsius(temp)
    temp_fahrenheit = kelvinToFahrenheit(temp)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = kelvinToCelsius(feels_like_kelvin)
    feels_like_fahrenheit = kelvinToFahrenheit(feels_like_kelvin)

    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    country = response['sys']['country']

    print(f"Today's Weather Forecast in {city} {country}:\n")
    #Format so that the temperature only has 2 decimal places
    print(f"Temperature: {temp_celsius:.2f} °C / {temp_fahrenheit:.2f} °F")
    print(f"Feels like: {feels_like_celsius:.2f}°C / {feels_like_fahrenheit:.2f} °F")
    print(f"Humidity: {humidity}%")
    print(f"General Weather in {city}: {description}")
    print(f"Wind Speed: {wind_speed}m/s")
    print(f"Sunrise: {sunrise_time}")
    print(f"Sunset: {sunset_time}\n")

def main():
    active=True
    while(active):
        user_input = input("Enter City Name: ")
        printWeatherLog(user_input)
        user_input = input("View Another city? (Y or N)")
        if user_input == 'N' or user_input == 'n':
            active = False
        elif user_input != 'y' and user_input != 'Y':
            print("Invalid Option")
            active = False

main()