import requests
import json
from datetime import datetime
import time
#import os

weather_params = {
	'lat' 	: '-34',
	'lon'	: '-58',
	'appid' : "e4b4296abeb04c526aad6e8905314af0", # os.environ.get("OWM_API_KEY")
	'exclude' : 'current,minutely,daily,alerts'
}

clima = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_params)
clima.raise_for_status()

with open('weather_data.json', 'w') as weather:
	weather.write(json.dumps(clima.json()['hourly']))

with open('weather_data.json', 'r') as weather:
	data = json.loads(weather.read())

def alert(forecast):
	return True if 'Clouds' in forecast	else False

forecast = [data[n]['weather'][0]['main'] for n in range(12)]

while True:
	hour = (datetime.now().hour, datetime.now().minute)
	if hour == (7, 0) and alert(forecast):
		print("IT'S GON RAIN")
		time.sleep(60*60*23)

