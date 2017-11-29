#include <cmath>
#include <iostream>
#include <vector>

using namespace std;


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

int main(){
	vector<double> randNumbers = generateRandNumbs();

	for (int i = 0; i < 10000; i++){
		cout << randNumbers[i] << endl;
	}
	
}