# <author>James Benson</author>
# <date>2015-04-29</date>
# <summary>Generates random numbers (quantity that you specify) between 
# 2 points that you specify for.  For unlimited generation, use 0 </summary>
# 
# To execute: python randNumFileOutput.py
# Specify number of points to print (0 for unlimited)
# Specify lower bound
# Specify upper bound
# Specify delay between points (whole seconds only)

import random
import time

afile = open("Random_Num.txt","w")

try:
	j = int(input("How many random numbers would you like to print? (Hint: use 0 for unlimited) "))
	low = int(input("What is the lower bound on the numbers? "))
	high = int(input("What is the upper bound on the numbers? "))
	nTime = int(input("What delay would you like between values printing (in integer seconds)? "))
	print("The numbers will be stored in Random_Num.txt")
	if j == 0:
		while True:
			line = str(random.randint(low, high))
			afile.write(line+'\n')
			print(line)
			time.sleep(nTime)
	else:
		for i in range(j):
			line = str(random.randint(low, high))
			afile.write(line+'\n')
			print(line)
			time.sleep(nTime)
except ValueError:
	# error handling
	print("Error occurred")
afile.close()