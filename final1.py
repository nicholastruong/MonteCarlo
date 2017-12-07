import numpy as np
import matplotlib.pyplot as plt

def generateRandomNum() :
	
	randNums = []

	l0 = 52598126; #arbitrary number between 1 and 2^31 - 1

	randNums.append(l0);

	#generates random numbers based on algorithm
	for x in range(1, 10000) :
		newRandNum = (7**5 * randNums[x-1]) % (2**31 - 1)
		randNums.append(newRandNum) 

	#normalizes them from 0 to 1
	for x in range(1, 10000) :
		randNums[x] = 1.0 * randNums[x] / (pow(2, 31) - 1)
		print randNums[x]
	
	#plots histogram
	plt.hist(randNums, bins=np.arange(0, 1, 0.01))  
	plt.title("Generated random numbers from 0 to 1")
	plt.show()


generateRandomNum()
