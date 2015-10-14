import urllib.request as u
import json
import subprocess
import os

url = 'http://api.wunderground.com/api/b0966060ea6d2b7e/geolookup/conditions/q/CO/Denver.json'

weather = u.urlopen(url)
weather = weather.read()
weather = weather.decode('utf-8')
weather = json.loads(weather)
icon = weather['current_observation']['icon']
print (icon)

imageLocation = os.path.abspath(os.path.dirname(__file__))+'/'
fehcmd = 'feh --bg-fill '+imageLocation
partlycloudy = 'PartlyCloudy.png'
rainy = 'Rainy.png'
sunny = 'Sunny.png'
cloudy = 'Cloudy.png'
other = 'SexySexySergal.jpg'

if icon in ('sunny', 'clear'):
	fehcmd += sunny
elif icon == 'partlycloudy':
	fehcmd += partlycloudy
elif icon == 'cloudy':
	fehcmd += cloudy
elif icon == 'rainy':
	fehcmd += rainy
else:
	fehcmd += other

print(fehcmd)
subprocess.call(fehcmd, shell=True)
