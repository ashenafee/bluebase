import os
import requests as requests

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
WEATHER = os.getenv("WEATHER_TOKEN")

# Get weather data from API for University of Toronto
url = f"https://api.openweathermap.org/data/2.5/onecall?lat=43.66097263251249" \
      f"&lon=-79.3959447315859&exclude=current,minutely&appid={'a1e7432aa61d866426416d903dded9f8'}"

# response = requests.get(url)

ts = 1643994000
print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



# print(response.text)
