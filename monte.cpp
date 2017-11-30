#include <cmath>
#include <iostream>
#include <vector>
#include <random>

using namespace std;

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
		cout << li << endl;
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


int main(){
	srand(time(NULL));
	vector<double> randNumbers = generateRandNumbs();

	for (int i = 0; i < 10000; i++){
		cout << randNumbers[i] << endl;
	}

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
	cout << countLessThan50 << endl;
	double probLessThan50 = (double)countLessThan50/5000;
	cout << "4a. P(X < 50) = " << probLessThan50 << endl;


	
}