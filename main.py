import pandas as pd
import matplotlib.pyplot as plt
from weather_apis import get_weather_by_city

cities_info = []
cities_info.append(get_weather_by_city("Kyiv"))
cities_info.append(get_weather_by_city("London"))
cities_info.append(get_weather_by_city("Paris"))

df = pd.DataFrame(cities_info)

plt.bar(df['city'], df['temp_c'], color='skyblue')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.title('Current Temperature in Different Cities')
plt.savefig("temperature.png")


