import numpy as np
import matplotlib.pyplot as plt
import random



def generateBinomialRandNumbers() :
	nums = []
	#simulate 5000 times
	for i in range(0, 5000) : 

		numSuccess = 0;

		for j in range(0, 70) :
			#generates random number from 0 to 1
			r = random.uniform(0, 1)
			#success
			if r < .7 :
				numSuccess += 1;
		
		nums.append(numSuccess);

	
	return nums;

def probabilityLessThan50(binomialNumbers) :
	
	#using these binomials, calculate probability P ( X < 50 )
	countLessThan50 = 0
	for i in range(0, 5000) : 
		if binomialNumbers[i] < 50 :
			countLessThan50 += 1

	print countLessThan50
	probabilityLessThan50 = countLessThan50 / 5000.0
	print "4a. P(X < 50) = " + str(probabilityLessThan50)

#dynamic programming alogorithm to find factorial used for combinations
def factorial(n) :
	nums = []
	nums.append(1)
	for i in range(1, n+1) :
		nums.append(i * nums[i-1])

	return nums[-1]

def theoreticalAnswer() : 

	#sum of all binomial probabilies P (X = r) for r = 0 to 49
	#X ~ Bin(n = 70, p = .7)
	probability = 0
	n = 70
	for r in range (0,50) :
		x = (1.0*factorial(n)/(1.0*factorial(r)*factorial(n-r)))*(.7**r)*(.3**(n-r))
		probability += x

	print "theoretical answer: ", probability
	


if __name__ == "__main__": 
	randBinNums = generateBinomialRandNumbers()
	probabilityLessThan50(randBinNums)

	theoreticalAnswer()

