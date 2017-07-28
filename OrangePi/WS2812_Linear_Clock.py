# -*- coding: iso-8859-15 -*-

# 34 led
# 0,1,2  4,5,6  8,9,10 				-> 00:0*
# 12,13  15,16,17				-> 00:*0
# 19,20,21  23,24,25  27,28,29  31,32,33	-> **:00

import serial
import time
import datetime

#Serial string identifier
IDENTIFIER = '$'

#Open the serial port and wait the arduino startup
ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(5)

#led status matrix
led_matrix = [[0]*3 for i in range(35)]

#Set the min "unit" colour
min_unit_r = 10
min_unit_g = 10
min_unit_b = 255

#Set the min "decimal" colour
min_dec_r = 0
min_dec_g = 255
min_dec_b = 0

#Set the hour colour
hour_r = 255
hour_g = 127
hour_b = 0

#brightness from 0 to 1
bri = 0.1

#GO!
while True:
	now = datetime.datetime.now()
	minuti = now.minute
	for i in range(1,10):
		if i<4:
			if((minuti%10) / i >=1):
				led_matrix[i-1][0] = int(min_unit_r * bri)
				led_matrix[i-1][1] = int(min_unit_g * bri)
				led_matrix[i-1][2] = int(min_unit_b * bri)
			else:
				led_matrix[i-1][0] = 0
				led_matrix[i-1][1] = 0
				led_matrix[i-1][2] = 0
		if i>3 and i < 7:
			if((minuti%10) / i >=1):
				led_matrix[i][0] = int(min_unit_r * bri)
				led_matrix[i][1] = int(min_unit_g * bri)
				led_matrix[i][2] = int(min_unit_b * bri)
			else:
				led_matrix[i][0] = 0
				led_matrix[i][1] = 0
				led_matrix[i][2] = 0
		if i>6 and i < 10:
			if((minuti%10) / i >=1):
				led_matrix[i+1][0] = int(min_unit_r * bri)
				led_matrix[i+1][1] = int(min_unit_g * bri)
				led_matrix[i+1][2] = int(min_unit_b * bri)
			else:
				led_matrix[i+1][0] = 0
				led_matrix[i+1][1] = 0
				led_matrix[i+1][2] = 0


	for i in range(1,5):
		if i<4:
			if((minuti/10) / i >=1):
				led_matrix[i+11][0] = int(min_dec_r * bri)
				led_matrix[i+11][1] = int(min_dec_g * bri)
				led_matrix[i+11][2] = int(min_dec_b * bri)
			else:
				led_matrix[i+11][0] = 0
				led_matrix[i+11][1] = 0
				led_matrix[i+11][2] = 0
		if i>3 and i < 6:
			if((minuti/10) / i >=1):
				led_matrix[i+12][0] = int(min_dec_r * bri)
				led_matrix[i+12][1] = int(min_dec_g * bri)
				led_matrix[i+12][2] = int(min_dec_b * bri)
			else:
				led_matrix[i+12][0] = 0
				led_matrix[i+12][1] = 0
				led_matrix[i+12][2] = 0


	ore = now.hour
	if ore > 12:
		ore = ore - 12

	for i in range(1,12):
		if i<4:
			if(ore / i >=1):
				led_matrix[i+18][0] = int(hour_r * bri)
				led_matrix[i+18][1] = int(hour_g * bri)
				led_matrix[i+18][2] = int(hour_b * bri)
			else:
				led_matrix[i+18][0] = 0
				led_matrix[i+18][1] = 0
				led_matrix[i+18][2] = 0
		if i>3 and i < 7:
			if(ore / i >=1):
				led_matrix[i+19][0] = int(hour_r * bri)
				led_matrix[i+19][1] = int(hour_g * bri)
				led_matrix[i+19][2] = int(hour_b * bri)
			else:
				led_matrix[i+19][0] = 0
				led_matrix[i+19][1] = 0
				led_matrix[i+19][2] = 0
		if i>6 and i < 10:
			if(ore / i >=1):
				led_matrix[i+20][0] = int(hour_r * bri)
				led_matrix[i+20][1] = int(hour_g * bri)
				led_matrix[i+20][2] = int(hour_b * bri)
			else:
				led_matrix[i+20][0] = 0
				led_matrix[i+20][1] = 0
				led_matrix[i+20][2] = 0
		if i>9 and i < 13:
			if(ore / i >=1):
				led_matrix[i+20][0] = int(hour_r * bri)
				led_matrix[i+20][1] = int(hour_g * bri)
				led_matrix[i+20][2] = int(hour_b * bri)
			else:
				led_matrix[i+20][0] = 0
				led_matrix[i+20][1] = 0
				led_matrix[i+20][2] = 0




	buff = "%s" %IDENTIFIER
	for i in range(35):
		for j in range(3):
			buff = buff + "%s," %(chr(led_matrix[i][j]))
	buff = buff[:-1]
	ser.write(buff)
	time.sleep(5)

ser.close()









