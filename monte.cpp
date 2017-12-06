#include <cmath>
#include <iostream>
#include <vector>
#include <random>

using namespace std;

double varianceCalculationDouble(vector<double> v){
	double sum = 0; 
	for (unsigned int i = 0; i < v.size(); i++){
		sum += v[i];
	}

	double variance = 0;
	for (unsigned int i = 0; i < v.size(); i++){
		variance += pow((sum - v[i]), 2);
	}

	return variance/(v.size() - 1);

}


//part 1a
vector<double> generateRandNumbs(){
	vector<double> v;
	for (int i = 0; i < 10000; i++){
		v.push_back(0);
	}

	long l0 = 52598126; //arbitrary number between 1 and 2^31 - 1
	v[0] = l0;
	for (int i = 1; i < 10000; i++){
		long li = long(pow(7,5)*v[i-1])%long(pow(2,31) - 1);
		//cout << li << endl;
		v[i] = li;
	}
	for (int i = 0; i < 10000; i++){
		v[i] /= (pow(2, 31) - 1);
	}
	return v;
}

//part 4
vector<int> generateBinomialRandNumbers(){

	

	vector<int> nums;
	//simulate 5000 times
	for (int i = 0; i < 5000; i++){

		int numSuccess = 0;

		for (int j = 0; j < 70; j++){
			
			double r = ((double) rand() / (RAND_MAX));
			//success
			if(r < .7)
				numSuccess++;
		}
		nums.push_back(numSuccess);

	}
	return nums;
}

//part 2
void dailyPriceFluctuation(vector<double>* randomNumberVector){
	vector<double> randPriceFluctuation = *(randomNumberVector);

	int price = 100000;
	cout << "Day 0 ending price: " << price;

	for (int i = 0; i < 10000; i++){

		//increase 100 with probability .45
		if (randPriceFluctuation[i] < .45){
			price += 100;
		}

		//decrease 200 with probability .25
		else if (randPriceFluctuation[i] >= .45 && randPriceFluctuation[i] <= .7){
			price -= 200;
		}

		//stays same with probability .3
		else{
			//price stays same
		}

		cout << "Day " << i+1 << " ending price: " << price << endl;
	}

}

//Problem 8, Wt follows a wiener process
void generateWienerProcess(){

	int T = 10; //time
    double n = 100000; //number of simulations
    double dT = T/n; //step size

	//generates normally distributed variables
	default_random_engine generator1;
    normal_distribution<double> distribution(0.0,1.0);

    //vector<double> w;
   for (int i = 0; i < 10000; i++){
   	distribution(generator1);
   }

    double sigma = .25;
    double r = .04;


    //w.push_back(0); //starts wiener process at W[0] = 0
    double w = 0;
    //dw = sqrt(dt) * N(0, 1)
    double sqrtdT = sqrt(dT);
    double s0 = 90;
    double s;

    for(int i = 1; i < 10/dT; i++){
    	double dW = sqrtdT * distribution(generator1);
    	//w.push_back(w[i-1] + dW);
    	w += dW;
    	cout << "time: " << i*dT << " , w: " << w << endl;
    	s = s0*exp(sigma*w + (r - pow(sigma, 2)/2.0)*i*dT);
    	cout << "stock price: " << s << endl;


    }

}



double priceOfEuropeanCall(int sims, double S, double K, double r, double v, double T, int typeOfVariable){

	//generates normally distributed variables
	default_random_engine generator;
    normal_distribution<double> distribution(0.0,1.0);

    double S_adjust = S * exp(T*(r-0.5*pow(v, 2)));
  	double S_cur = 0.0;
  	double payoff_sum = 0.0;

  	vector<double> randomVariables;
  	for (int i = 0; i< sims; i++){
  		randomVariables.push_back(distribution(generator));
  	}

  	//antithetic variable 
  	if (typeOfVariable == 2){
  		for (int i = 0; i < sims; i++){
  			randomVariables[i] = -1*(randomVariables[i]);
  		}
  	}


  	for (int i=0; i<sims; i++) {
    	S_cur = S_adjust * exp(sqrt(pow(v,2)*T)*randomVariables[i]);
    	payoff_sum += max(S_cur - K, 0.0);
  	}

  	return (payoff_sum / sims) * exp(-r*T);
}

int main(){
	srand(125);
	vector<double> randNumbers = generateRandNumbs();

	for (int i = 0; i < 10000; i++){
		cout << randNumbers[i] << endl;
	}

	//calls part 2
	dailyPriceFluctuation(&randNumbers);



	//generate 5000 binomial random numbers (n = 70, p = .7)
	vector<int> binomialRandNumbs = generateBinomialRandNumbers();
	for (int i = 0; i < 5000; i++){
		cout << binomialRandNumbs[i] << endl;
	}

	//using these binomials, calculate probabilitiy P(X < 50)
	int countLessThan50 = 0;
	for (int i = 0; i < 5000; i++){
		if(binomialRandNumbs[i] < 50){
			countLessThan50++;
		}
	}
	//cout << countLessThan50 << endl;
	double probLessThan50 = (double)countLessThan50/5000;
	cout << "4a. P(X < 50) = " << probLessThan50 << endl;


	//int sims, double S, double K, double r, double v, double T, int typeofvariable
	//9a cout << priceOfEuropeanCall(1000000, 300, 310, .02, 1.287, .079365, 1) << endl;
	cout << priceOfEuropeanCall(1000000, 90, 100, .04, .25, 10, 1) << endl;
	//cout << monte_carlo_call_price(1000000, 90, 100, .04, .25, 10) << endl;
	generateWienerProcess();
	
}