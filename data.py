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
for i in range(1,len(array1)):
	if array1[i] == array1[i-1] and array1[i] != 0:
		counter1 = counter1 + 1
	elif array1[i] == 0:
		continue
	else:
		array2.append(counter1)
		counter1 = 0

array3 = []
a = False
for i in range(2,len(array2)-2):
	
	if(a):
		a = False
		continue	
	
	if(array2[i] != 0):
		array3.append(array2[i] + array2[i+1])
		a = True
	




for i in range(len(array1) - len(array2)):
	array2.append(0)
for i in range(len(array1) - len(array3)):
	array3.append(0)
array1 = array1.ravel()
#array3 = np.array(array2)
#array3 = array3.ravel()
for j in array1:
	print(j)
#np.savetxt("test.csv", array1, delimiter=",")

df = pd.DataFrame({"Data" : array1, "Counter" : array2, "Col3" : array3})
df.to_csv("test.csv", index=False)



	
	

