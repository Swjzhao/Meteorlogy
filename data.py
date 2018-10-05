import pandas as pd
import numpy as np
import os
import serial
import syslog
import time

from pandas.compat import StringIO, BytesIO


#The following line is for serial over GPIO
port = '/dev/ttyACM0'
ard = serial.Serial(port,9600,timeout=5)
i = 0

data = pd.read_csv("data.csv", usecols=[2])

#arrays
dataWGain = []
width = []
period = []
dataIN = []


widthCounter = 0
periodCounter = 0
isPeriod = 0
last = 0
withoutFirstPeriod = 0; #disregard first period (3 changes) 0 > - 500 > 500> -500

while 0 < 1:
	msg = ard.readline()
	msg1 = int(msg)
	dataIN.append(msg1)
	j = (msg1-500)* 10000
	if j > 500:
		dataWGain.append(1)
	else: 
		dataWGain.append(0)
	
	if last == msg1:
		counter+=1
		deleteFirstPeriod += 1
	else:
		width.append(counter)
		counter = 0
		if (withoutFirstPeriod > 1):
			isPeriod += 1
		
			
	if withoutFirstPeriod > 1:
		if isPeriod:	
			period.append(width[periodCounter] + width[periodCounter-1])
			print period[len(period)-1]
			isPeriod = 0
			
	last = msg1






#for i in range(len(array1) - len(array2)):
#	array2.append(0)
#for i in range(len(array1) - len(array3)):
#	array3.append(0)
#array1 = array1.ravel()
for j in len(range(dataWGain) - range(width)):
	width.append(0)


for j in len(range(dataWGain) - range(period)):
	width.append(0)

df = pd.DataFrame({"Data" : dataWGain, "Width" : width, "Period" : period})
df.to_csv("test.csv", index=False)



	
	

