import pandas as pd
import numpy as np
import os

from pandas.compat import StringIO, BytesIO




data = pd.read_csv("data.csv", usecols=[2])


array1 = data.values

counter = 0
for j in array1:
	j = (j-500)* 10000;

	if j > 500:
		array1[counter] = 500;
	elif j < -500: 
		array1[counter] = -500;
	else:
		array1[counter] = j;

	counter = counter + 1

for j in array1:
	print(j)

array2 = []
counter1 = 0
for i in range(1,len(array2)):
	if array2[i] == array2[i-1]:
		counter1 = counter1 + 1
	else:
		array2.append(counter1)
	

np.savetxt("test.csv", zip(array1,array2), delimiter = ",")



	
	

