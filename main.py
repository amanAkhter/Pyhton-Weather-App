# Author : Aman Akhter

# Importing the required modules
import os
import requests as req
from dotenv import load_dotenv

# Loading the .env file into the environment
load_dotenv()

# Taking user input of city
city = input("Enter the name of the city : ")

# Getting the API KEY from the environment
api_key = os.getenv("API_KEY")

# GETTING THE GEOLOCATION (Latitude and Longitude)

# URL for getting location
url_location = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"

# sending the 'get' request and converting the response to json
req_geolocation = req.get(url_location).json()

# response of the geolocation request (Note : This response is embedded json inside a list)
# print(req_geolocation)

city_lat = ""
city_lon = ""

# iterating the list to get in the json and extracting the latitude and longitude
for x in req_geolocation:
    city_lat = x['lat']
    city_lon = x['lon']


# GETTING THE WEATHER

# URL for getting the weather
url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}"

# sending the 'get' request and converting the response to json
req_weather = req.get(url_weather).json()

# response of the weather request
# print(req_weather)

# Extracting city temperature from [main's -> temp's -> value] | and converting it from kelvin to celcius
city_temp = req_weather['main']['temp'] - 271

# Extracting the city name from response
city_name = req_weather['name']


# Printing the output
print(f"City : {city_name} \n"
      f"Temperature : {city_temp} °C")
