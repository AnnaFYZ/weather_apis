import os
from dotenv import load_dotenv
import requests

load_dotenv()
base_url = f'https://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}'

def get_weather_by_city(city):
    try:
        response = requests.get(f'{base_url}&q={city}')
        data = response.json()
        if response.status_code == 200:
            city_info = {
                'city': data['location']['name'],
                'region': data['location']['region'],
                'country': data['location']['country'],
                'local_time': data['location']['localtime'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
                'wind_mph': data['current']['wind_mph'],
                'wind_kph': data['current']['wind_kph'],
                'humidity': data['current']['humidity'],
                'feelslike_c': data['current']['feelslike_c'],
                'feelslike_f': data['current']['feelslike_f'],
                'temp_c': data['current']['temp_c'],
                'temp_f': data['current']['temp_f']
            }
            return city_info
        else:
            print(f'Error: {response.status_code} - {response.text}')
            return None
    except requests.RequestException as e:
        print(f'HTTP Request failed: {e}')
        return None