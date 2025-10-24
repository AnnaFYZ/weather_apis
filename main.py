import os
from dotenv import load_dotenv
import requests

load_dotenv()
response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q=Kyiv')
print(response)