import requests
import pandas as pd

# Coordinates for desired City, State
lat = 
lon = 
API_KEY = '' #<<<Insert your api key here

# API call
url = f'' #insert api endpoint which can be found on https://openweathermap.org/api

response = requests.get(url)
data = response.json()

print(response.status_code)
print(response.json())

# Extract pollution data
pollution = data['list'][0]
components = pollution['components']
aqi = pollution['main']['aqi']

# Build DataFrame
df = pd.DataFrame([{
    'AQI Level': aqi,
    'CO (μg/m³)': components['co'],
    'NO (μg/m³)': components['no'],
    'NO₂ (μg/m³)': components['no2'],
    'O₃ (μg/m³)': components['o3'],
    'SO₂ (μg/m³)': components['so2'],
    'NH₃ (μg/m³)': components['nh3'],
    'PM2.5 (μg/m³)': components['pm2_5'],
    'PM10 (μg/m³)': components['pm10']
}])

# Save to Excel
df.to_excel('City_Air_Pollution.xlsx', index=False)

