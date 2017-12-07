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
	
	return randNums


def dailyPriceFluctuation(randPriceFluctuation) :

	dailyPrice = []
	day = [0]
	price = 100000;

	dailyPrice.append(price)
	print "Day 0 ending price: " + str(price);

	for i in range (1, 10000) : 

		#increase 100 with probability .45
		if randPriceFluctuation[i] < .45 :
			price += 100;
		

		#decrease 200 with probability .25
		elif randPriceFluctuation[i] >= .45 and randPriceFluctuation[i] <= .7 :
			price -= 200;
		

		#else stays same with probability .3
		print "Day " + str(i+1) + " ending price: " + str(price)
		dailyPrice.append(price)
		day.append(i)


	#plots histogram
	#plt.hist(randPriceFluctuation, bins='auto')  
	#plt.title("Prices of the asset")
	#plt.show()

	plt.plot(day, dailyPrice)
	plt.axis([0, 10000, 0, 120000])
	plt.show()



	


if __name__ == "__main__": 
	randNums = generateRandomNum()
	dailyPriceFluctuation(randNums)

