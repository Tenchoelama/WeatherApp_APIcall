import requests 
import os 
from datetime import datetime 

api_key = '1e8730fa150fbd01ef6b439fd4967625'
city = input("Enter the city name: ")

api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

get_api = requests.get(api_link)
data = get_api.json()

def start_app():
    
    
    if data['cod'] == '404':
        print (f"Invalid City: {city}, Please check your City name and try again.")
        
        
    else:
        #create variables to store and display data
        temp_city = (data['main']['temp']) - 273.15
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed'] 
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p") 
        
        print("------------------------------------------------------------")
        print("Weather Stats for - {} || {} ".format(city.upper(), date_time))
        print("------------------------------------------------------------")
        
        print("Current temperature is: {: .2f} deg C".format(temp_city))
        print("Current weather desc :", weather_desc)
        print("Current Humidity: ", humidity, "%")
        print("Current wind speed: ", wind_speed, "kmph" )
        
        print("----------------Thank you for using our App-------------------")
        

start_app()