import tweepy
from pyowm.owm import OWM
from datetime import datetime
from pytz import timezone

# Twitter API keys
consumer_key = 'GN3KZZirKI1egrEviS0DRf7yL'
consumer_secret = '0XHG0xR0aObaXtWUlGBovQY7TCjuTdmnivffHKqSYfQEbLuE7d'
key = '1315679401053282304-NEJLiokINOcAOZqB7mHztGNk4sGhgI'
secret = 'ybgihG10nIAwxqXfYVZBaqQB8BJSKLi8vbsVIMOUqthRE'

# Open Weather Map API keys
owm = OWM('5f28773b1305282ee6f786650679a41e')

# Confirms my API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
mgr = owm.weather_manager()

# Defines the locations
one_call = mgr.one_call(lat=38.5816, lon=-121.4944)
weather = mgr.weather_at_place('Sacramento,US').weather

# Current temperature
currenttemp = weather.temperature('fahrenheit').get('temp')

# Maximum temperature
temp_max = one_call.forecast_daily[0].temperature('fahrenheit').get('max')

# Minimum temperature
temp_min = one_call.forecast_daily[0].temperature('fahrenheit').get('min')

# Sunrise time
srdt = one_call.forecast_daily[0].sunrise_time("date")
srpst = srdt.astimezone(timezone('America/Los_Angeles'))
srstr = srpst.strftime('%Y-%m-%d-%H-%M')
srt = datetime.strptime(srstr, '%Y-%m-%d-%H-%M')
srhms = srt.time()
sunrise = srhms.strftime('%H:%M')

# Sunset time
ssdt = one_call.forecast_daily[0].sunset_time('date')
sspst = ssdt.astimezone(timezone('America/Los_Angeles'))
ssstr = sspst.strftime('%Y-%m-%d-%H-%M')
sst = datetime.strptime(ssstr, '%Y-%m-%d-%H-%M')
sshms = sst.time()
ss24 = sshms.strftime('%H:%M')
ss24str = datetime.strptime(ss24, "%H:%M")
sunset = ss24str.strftime('%I:%M')

# Forming the final tweet
tweet = "The current temperature in Sacramento is " + str(currenttemp) + "F. The sun is going to rise at " + str(
    sunrise) + "am and will set at " + str(sunset) + "pm. The high today is " + str(temp_max) + "F and the low is " + str(temp_min) + "F."

# Sends the tweet
api = tweepy.API(auth)
api.update_status(tweet)
