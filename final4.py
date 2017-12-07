import numpy as np
import matplotlib.pyplot as plt
import random

#using algorithm
def generateGaussianRandomNum() :
	
	mu, sigma = 0, 1 # mean and standard deviation
	randGaussianNums = np.random.normal(mu, sigma, 5000)
	
	#plots histogram
	plt.hist(randGaussianNums, bins=np.arange(-5, 5, 0.05))  
	plt.title("Algorithm Generated Gaussian Random Numbers (mu = 0, sigma = 1)")
	plt.show()

if __name__ == "__main__": 
	generateGaussianRandomNum()

