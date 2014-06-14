import time
import datetime
import gspread
import os
import Adafruit_DHT

#### Settings ####
username = 'you@gmail.com'
password = 'supersecretpassword'
worksheet = 'temperature'
sensor = Adafruit_DHT.DHT22
pin = 4

def get_temp():
	reading = Adafruit_DHT.read_retry(sensor, pin)
	print reading
	return (reading)

def upload():
	# Login with your Google account
	gc = gspread.login(username, password)

	# Open a worksheet from spreadsheet with one shot
	wks = gc.open(worksheet).sheet1

	# Add readings to sheet
	values = [datetime.datetime.now(), temperature, humidity]
	wks.append_row(values)
        wks.update_cell('2','4', temperature)
	wks.update_cell('2','5', humidity)

reading = get_temp()
temperature = reading[1]
humidity = reading[0]
upload()
