import numpy as np
import matplotlib.pyplot as plt
import math
n = 500. # number of steps
T = 10.   # Length of T
Delta = T/n # Lenght of step

t = np.arange(10, step=Delta)
S = np.zeros(n, np.dtype(float))
x = range(1, len(S))

# Wiener process to simulate one path
def Wiener():
	for i in x:
		dW = np.random.normal(0., 1.) #gaussian(0, 1)
		dt = np.sqrt(Delta)
		dS = dW*dt
		S[i] = S[i-1] + dS

	return S

def priceOfStock(w) : 
	s0 = 90
	sigma = .25
	r = .04

	prices = np.zeros(n, np.dtype(float))

	#generates array of stock price at t
	for i in x :
		prices[i] = s0*math.exp(sigma*w[i] + ((r - (sigma**2)/2.0))*(i*Delta));


	#plt.plot(t, prices)
	#returns price of stock at time T
	return prices[-1]


def priceOfEuropeanCall(sims, S, K, r, v, T) : 

  payoff_sum = 0.0;

  #simulates stock at time T, and calculates payoff
  for i in range(0, sims) :
	a = Wiener()
	S_cur = priceOfStock(a)
	payoff_sum += max(S_cur - K, 0.0)
  
  #averages payoff and accounts for risk free interest rate
  return (payoff_sum / sims) * math.exp(-r*T);

if __name__ == "__main__": 
	
	print priceOfEuropeanCall(10000, 90, 100, .04, .25, 10)

