import time
import datetime
import gspread
import os
import Adafruit_DHT
import urllib2
import json

#### Settings ####
username = 'you@gmail.com'
password = 'supersecret'
worksheet = 'cpu_temperature'
sensor = Adafruit_DHT.DHT22
pin = 4

def get_weather():
	response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?id=2748000') # id = your openweathermap location
	data = json.load(response)
	temp_outside = float(data['main']['temp'] - 273.15)
	return (temp_outside)

def get_temp():
	dht22 = Adafruit_DHT.read_retry(sensor, pin)
	cpu_temp_read = os.popen('cat /sys/class/thermal/thermal_zone0/temp')
	cpu = float(cpu_temp_read.read())/1000
	return (round(dht22[0],2),round(dht22[1],2),cpu)

def upload():
	# Login with your Google account
	gc = gspread.login(username, password)

	# Open a worksheet from spreadsheet with one shot
	wks = gc.open(worksheet).sheet1

	# Add readings to sheet
	values = [datetime.datetime.now(), temperature,humidity, temp_outside, cpu_temp]
	wks.append_row(values)
	wks.update_cell('2','6', datetime.datetime.now())
        wks.update_cell('2','7', temperature)
	wks.update_cell('2','8', humidity)

reading = get_temp()
temp_outside = get_weather()
temperature = reading[1]
humidity = reading[0]
cpu_temp = reading[2]
print reading
print temperature
print humidity
print cpu_temp
print temp_outside
upload()
