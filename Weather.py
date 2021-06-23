import requests
#import os
from datetime import datetime
import json

api_key = 'fa66e9afdae1e380d417998a70bd8a4e'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("------------------------------------------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city)) #.2f - upto 2 decimal points
print("Current weather desc :",weather_desc)
print("Current Humidity      :",hmdt, '%')
print("Current wind speed   :",wind_spd, 'kmph')
with open("Weathertextfile.txt", "w") as file:
   json.dump( api_data,file)
