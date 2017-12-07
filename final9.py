import numpy as np
import matplotlib.pyplot as plt
import random
import math

def priceOfEuropeanCall(sims, S, K, r, v, T, typeOfVariable) : 

  mu, sigma = 0, 1 # mean and standard deviation
  randGaussianNums = np.random.normal(mu, sigma, sims)

  S_adjust = S * math.exp(T*(r-0.5*(v**2)));
  S_cur = 0.0;
  payoff_sum = 0.0;

 
  #antithetic variable 
  if typeOfVariable == 2 :
  	for i in range(0, sims) :
  		randGaussianNums[i] = -1*(randGaussianNums[i]);
  	

  for i in range(0, sims) :
    S_cur = S_adjust * math.exp(math.sqrt((v**2)*T)*randGaussianNums[i]);
    payoff_sum += max(S_cur - K, 0.0);
  

  return (payoff_sum / sims) * math.exp(-r*T);

if __name__ == "__main__": 
  print priceOfEuropeanCall(1000000, 90, 100, .04, .25, 10, 1) 