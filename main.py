import os

import requests as requests
from dotenv import load_dotenv

load_dotenv()
WEATHER = os.getenv("WEATHER_TOKEN")

# Get weather data from API for University of Toronto
url = f"https://api.openweathermap.org/data/2.5/onecall?lat=43.66097263251249" \
      f"&lon=-79.3959447315859&exclude=current,minutely&appid={WEATHER}"

response = requests.get(url)

print(response.text)
