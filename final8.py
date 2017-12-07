import numpy as np
import matplotlib.pyplot as plt
import math
# Time steps
n = 500. # Set the number of steps per unit of time
T = 10.   # Length of [0,T] in time units
Delta = T/n # Scale each steps to unit of time

t = np.arange(10, step=Delta)
S = np.zeros(n, np.dtype(float))
x = range(1, len(S))

# Define a function to simulate one path
def Wiener():
	for i in x:
		dW = np.random.normal(0., 1.) #gaussian(0, 1)
		dt = np.sqrt(Delta)
		dS = dW*dt
		S[i] = S[i-1] + dS
		print i
		print S[i]

	return S

def priceOfStock(S) : 
	s0 = 90
	sigma = .25
	r = .04

	prices = np.zeros(n, np.dtype(float))

	for i in x :
		prices[i] = s0*math.exp(sigma*S[i] + ((r - (sigma**2)/2.0))*(i*Delta));


	plt.plot(t, prices)


def priceOfEuropeanCall(sims, S, K, r, v, T) : 

  mu, sigma = 0, 1 # mean and standard deviation
  randGaussianNums = np.random.normal(mu, sigma, sims)

  S_adjust = S * math.exp(T*(r-0.5*(v**2)));
  S_cur = 0.0;
  payoff_sum = 0.0;

  for i in range(0, sims) :
    S_cur = S_adjust * math.exp(math.sqrt((v**2)*T)*randGaussianNums[i]);
    payoff_sum += max(S_cur - K, 0.0);
  

  return (payoff_sum / sims) * math.exp(-r*T);


if __name__ == "__main__": 
	for i in range (0, 1) : 
		S = Wiener()
		priceOfStock(S)

	plt.title('Price of 1 Stock')
	#plt.show()

	print priceOfEuropeanCall(1000000, 90, 100, .04, .25, 10)

