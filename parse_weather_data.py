import os
import datetime
from Weather import Weather
from typing import List, Dict, Any
from datetime import date

import requests as requests
from dotenv import load_dotenv

load_dotenv()
WEATHER = os.getenv("WEATHER_TOKEN")

url = f"https://api.openweathermap.org/data/2.5/onecall?lat=43.66097263251249" \
      f"&lon=-79.3959447315859&exclude=current,minutely&appid={WEATHER}"

r = requests.get(url)
data = r.json()

# print(data['daily'])
# print(datetime.datetime.now().timestamp())
# ts1 = datetime.datetime.now().timestamp()
# ts2 = datetime.datetime.now().timestamp()
# # print(datetime.datetime.fromtimestamp(ts1))
# print(type(datetime.datetime.fromtimestamp(ts2).time()))
# today = datetime.date.today()
# print(today.strftime('%B'))

def get_weather_data(d: date) -> List[Any]:
      """Return 3 things:
            - Temperature values on date <d>
            - feels_like values on date <d>
            - Probability of precipitation on date <d>
      """

      #Loop through days in data['daily'] to get list of todays weather data
      todays_data = 0
      for i in range(len(data['daily'])):
            temp_d = datetime.datetime.fromtimestamp(data['daily'][i]['dt'])
            if temp_d.year == d.year and temp_d.month == d.month and temp_d.day\
                  == d.day:
                  todays_data = data['daily'][i]
            break

      return [todays_data['temp'], todays_data['feels_like'],
              todays_data['pop'], todays_data['sunset']]

if __name__ == "__main__":
      curr_date = date.today()
      weather_data = get_weather_data(curr_date)

      Forecast = Weather(weather_data)
      print(Forecast)


